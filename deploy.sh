#!/bin/bash
set -e # stop on first error

# --- CONFIGURATION ---
FUNCTION_NAME="scheduled-lambda"
PY_FILE="lambda.py"
BUILD_DIR="./build"
ZIP_FILE="$BUILD_DIR/lambda.zip"
AWS_REGION="us-east-1" # change if needed

# Ensure build directory exists
mkdir -p "$BUILD_DIR"

echo "==> Packaging Lambda function..."
zip -j "$ZIP_FILE" "$PY_FILE"

echo "==> Deploying to AWS Lambda: $FUNCTION_NAME..."
aws lambda update-function-code \
  --function-name "$FUNCTION_NAME" \
  --zip-file "fileb://$ZIP_FILE" \
  --region "$AWS_REGION"

echo "==> Deployment complete."
