#!/bin/bash

# Package the Python app with dependencies
echo "Packaging application for AWS Lambda..."

# Remove old deployment packages
rm -rf package
rm function.zip

# Install dependencies locally
pip install --target ./package -r requirements.txt

# Copy source files to package directory
cp -r src app.py tracking_data.json package/

# Navigate to the package directory
cd package

# Zip all files to create a Lambda deployment package
zip -r ../function.zip .

# Move back to project root
cd ..

# Deploy using AWS CLI
echo "Deploying to AWS Lambda..."
aws lambda update-function-code \
    --function-name shipment-tracker-lambda \
    --zip-file fileb://function.zip

echo "Deployment complete!"
