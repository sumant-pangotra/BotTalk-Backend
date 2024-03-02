#!/bin/bash

# Source the secret script
source .secret/.secret.sh

# Start Python processes in the background with log redirection
python3 vertex_ai/api.py > vertex_ai_api.log 2>&1 &
python3 open_ai/api.py > open_ai_api.log 2>&1 &

# Print message indicating server start
echo "Started Servers"
