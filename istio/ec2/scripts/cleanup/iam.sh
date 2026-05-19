#!/bin/bash

for var in AWS_ACCOUNT CLUSTER_NAME AWS_REGION; do
  if [ -z "${!var:-}" ]; then
    echo "Error: $var is not set."
    exit 1
  fi
done

echo "Starting cleanup of Istio IAM roles and policies..."

# Delete the pod identity association before removing the IAM role it references
ASSOC_ID=$(aws eks list-pod-identity-associations \
  --cluster-name "${CLUSTER_NAME}" \
  --namespace istio-system \
  --region "${AWS_REGION}" \
  --query 'associations[?serviceAccount==`istiod`].associationId | [0]' \
  --output text 2>/dev/null)

if [ -n "${ASSOC_ID}" ] && [ "${ASSOC_ID}" != "None" ]; then
  echo "Deleting pod identity association ${ASSOC_ID}..."
  aws eks delete-pod-identity-association \
    --cluster-name "${CLUSTER_NAME}" \
    --association-id "${ASSOC_ID}" \
    --region "${AWS_REGION}" > /dev/null
  echo "Deleted pod identity association"
else
  echo "No pod identity association found for istio-system/istiod. Skipping."
fi

# Cleanup istiod role
if aws iam get-role --role-name istiod > /dev/null 2>&1; then
    echo "Detaching policies from istiod role..."

    ISTIOD_POLICY_ARN="arn:aws:iam::${AWS_ACCOUNT}:policy/istiod-${AWS_ACCOUNT}"
    if aws iam get-policy --policy-arn $ISTIOD_POLICY_ARN > /dev/null 2>&1; then
        aws iam detach-role-policy \
            --role-name istiod \
            --policy-arn $ISTIOD_POLICY_ARN > /dev/null 2>&1
        echo "Detached policy istiod-${AWS_ACCOUNT} from istiod role"

        echo "Deleting policy istiod-${AWS_ACCOUNT}..."
        aws iam delete-policy --policy-arn $ISTIOD_POLICY_ARN
        echo "Deleted policy istiod-${AWS_ACCOUNT}"
    fi

    echo "Deleting istiod role..."
    aws iam delete-role --role-name istiod
    echo "Deleted istiod role"
else
    echo "istiod role does not exist."
fi

# Cleanup istiod-ec2 role
if aws iam get-role --role-name istiod-ec2 > /dev/null 2>&1; then
    echo "Detaching policies from istiod-ec2 role..."

    EC2_READ_POLICY_ARN="arn:aws:iam::${AWS_ACCOUNT}:policy/ec2-read-only"
    if aws iam get-policy --policy-arn $EC2_READ_POLICY_ARN > /dev/null 2>&1; then
        aws iam detach-role-policy \
            --role-name istiod-ec2 \
            --policy-arn $EC2_READ_POLICY_ARN > /dev/null 2>&1
        echo "Detached policy ec2-read-only from istiod-ec2 role"

        echo "Deleting policy ec2-read-only..."
        aws iam delete-policy --policy-arn $EC2_READ_POLICY_ARN
        echo "Deleted policy ec2-read-only"
    fi

    echo "Deleting istiod-ec2 role..."
    aws iam delete-role --role-name istiod-ec2
    echo "Deleted istiod-ec2 role"
else
    echo "istiod-ec2 role does not exist."
fi

echo ""
echo "All IAM cleanup completed successfully."
echo "Deleted resources:"
echo "  - IAM Role: istiod"
echo "  - IAM Role: istiod-ec2"
echo "  - IAM Policy: ec2-read-only"
echo "  - IAM Policy: istiod-${AWS_ACCOUNT}"
