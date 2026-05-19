#!/bin/bash

# Configures security group rules required for EC2 ambient mesh integration.
# Adds inbound port 15008 (HBONE) on both the EC2 instance security group
# (for EKS-to-EC2 traffic) and the EKS node security group (for EC2-to-EKS traffic).

set -euo pipefail

for var in AWS_ACCOUNT AWS_REGION CLUSTER_NAME EC2_INSTANCE_ID; do
  if [ -z "${!var:-}" ]; then
    echo "Error: $var is not set."
    exit 1
  fi
done

echo "========================================="
echo "Configuring security groups for EC2 ambient mesh"
echo "========================================="
echo ""
echo "Cluster:     $CLUSTER_NAME"
echo "Instance:    $EC2_INSTANCE_ID"
echo "Region:      $AWS_REGION"
echo ""

VPC_ID=$(aws eks describe-cluster \
  --name "$CLUSTER_NAME" \
  --region "$AWS_REGION" \
  --query 'cluster.resourcesVpcConfig.vpcId' \
  --output text)

VPC_CIDR=$(aws ec2 describe-vpcs \
  --vpc-ids "$VPC_ID" \
  --region "$AWS_REGION" \
  --query 'Vpcs[0].CidrBlock' \
  --output text)

EC2_SG_ID=$(aws ec2 describe-instances \
  --instance-ids "$EC2_INSTANCE_ID" \
  --region "$AWS_REGION" \
  --query 'Reservations[0].Instances[0].SecurityGroups[0].GroupId' \
  --output text)

EKS_NODE_SG_ID=$(aws eks describe-cluster \
  --name "$CLUSTER_NAME" \
  --region "$AWS_REGION" \
  --query 'cluster.resourcesVpcConfig.clusterSecurityGroupId' \
  --output text)

echo "VPC CIDR:        $VPC_CIDR"
echo "EC2 SG:          $EC2_SG_ID"
echo "EKS node SG:     $EKS_NODE_SG_ID"
echo ""

add_rule_if_missing() {
  local sg_id=$1
  local cidr=$2
  local description=$3

  existing=$(aws ec2 describe-security-group-rules \
    --filters "Name=group-id,Values=${sg_id}" \
    --region "$AWS_REGION" \
    --query 'SecurityGroupRules[?FromPort==`15008` && ToPort==`15008` && IsEgress==`false`]' \
    --output text)

  if [ -n "$existing" ]; then
    echo "✓ Port 15008 inbound rule already exists on $sg_id ($description)"
  else
    echo "Adding port 15008 inbound rule to $sg_id ($description)..."
    aws ec2 authorize-security-group-ingress \
      --group-id "$sg_id" \
      --protocol tcp \
      --port 15008 \
      --cidr "$cidr" \
      --region "$AWS_REGION"
    echo "✓ Added port 15008 inbound rule to $sg_id ($description)"
  fi
}

# EC2 SG: allow inbound 15008 from VPC (EKS → EC2 HBONE)
add_rule_if_missing "$EC2_SG_ID" "$VPC_CIDR" "EC2 instance, allows EKS-to-EC2 HBONE"

# EKS node SG: allow inbound 15008 from VPC (EC2 → EKS HBONE)
add_rule_if_missing "$EKS_NODE_SG_ID" "$VPC_CIDR" "EKS nodes, allows EC2-to-EKS HBONE"

echo ""
echo "========================================="
echo "Security group configuration complete!"
echo "========================================="
