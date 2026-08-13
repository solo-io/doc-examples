---
description: Greet the user and confirm the plugin is loaded.
argument-hint: "[your name]"
allowed-tools: Bash(echo:*)
---
Greet the user by name if `$ARGUMENTS` was provided, otherwise use "there".

Then confirm the plugin is active by saying "hello-plugin v1.0.0 is loaded" and
list each slash command available in this session with a one-line description.

Keep the response to three sentences or fewer.