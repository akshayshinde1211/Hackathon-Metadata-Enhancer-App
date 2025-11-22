#!/bin/bash

# Check if kubectl is installed
if ! command -v kubectl &> /dev/null
then
    echo "kubectl could not be found. Please install it first."
    exit 1
fi

# Create secret for API key if it doesn't exist
# NOTE: In a real production environment, use a more secure way to manage secrets (e.g., Vault, SealedSecrets)
if ! kubectl get secret app-secrets &> /dev/null; then
    echo "Creating secret 'app-secrets'..."
    read -p "Enter your Gemini API Key: " api_key
    kubectl create secret generic app-secrets --from-literal=gemini-api-key=$api_key
else
    echo "Secret 'app-secrets' already exists."
fi

# Apply manifests
echo "Applying Kubernetes manifests..."
kubectl apply -f k8s/deployment.yaml
kubectl apply -f k8s/service.yaml

echo "Deployment complete!"
echo "Check status with: kubectl get pods"
