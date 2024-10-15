# setup the kuberne# Setup the Kubernetes environment for Windows
# Create namespace
kubectl create namespace blog-namespace

# Deploy MongoDB
kubectl apply -f "$(pwd)\mongodb-express-rest-api-example\k8s\mongodb\statefulset.yaml" -n blog-namespace
kubectl apply -f "$(pwd)\mongodb-express-rest-api-example\k8s\mongodb\\service.yaml" -n blog-namespace

# Deploy server (Backend)
kubectl apply -f "$(pwd)\mongodb-express-rest-api-example\k8s\server\deployment.yaml" -n blog-namespace
kubectl apply -f "$(pwd)\mongodb-express-rest-api-example\k8s\server\service.yaml" -n blog-namespace

# Deploy app (Frontend)
kubectl apply -f "$(pwd)\mongodb-express-rest-api-example\k8s\app\deployment.yaml" -n blog-namespace
kubectl apply -f "$(pwd)\mongodb-express-rest-api-example\k8s\app\service.yaml" -n blog-namespace

Write-Host "All resources have been deployed successfully."