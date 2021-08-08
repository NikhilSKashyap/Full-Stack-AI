# Simple Vision-AI-as-a-service <!-- omit in toc -->

[Instill](https://instill.tech/) Full Stack AI Engineer assignment. 

## Problem Statement
The requirements and the provided sample codes serve a purpose to simulate a typical scenario when AI/ML engineers in a MLOps team pass a working deep learning model to a DevOps team to deploy it on production. We expect a Full Stack AI Engineer can independently handle this end-to-end development and deployment journey.

## Table of content <!-- omit in toc -->

- [Project Setup](#project-setup)
- [Architecture](#architecture)
- [Tasks](#tasks)
    1. [Prepare a MNIST deep learning model](#prepare-a-mnist-deep-learning-model).
    2. Fine-tune [FashionMNIST](https://pytorch.org/vision/stable/datasets.html#fashion-mnist) model.]
    3. Initiate a simple RESTful API backend server for hosting the model.
    4. Containerise the backend server.
    5. Set up a local Kubernetes cluster and deploy the service on it. 

## Project Setup

Run the following comands to set-up this project. 

Start Minikube.

```
minikube start
```

Now ssh/log in to Minikube VM and create the docker image.

```
minikube ssh
```

!['Minikube'](Images/minikube.png)

Before creating the docker image, clone the repository containing the application’s source code inside minikube and cd into the folder.

```
git clone <repo http>
```

Assuming the repo name is full-stack-ai

```
cd full-stack-ai
```

Generate a docker image using the Dockerfile.

```
docker build -t <docker-hub id>/mnist:latest .
```

Check if the image was created with the command below.

```
docker images
```

You should get an output similar to this -

!['Docker'](Images/docker.png)

Log in to your [Docker Hub](https://hub.docker.com/) account from your terminal using the following command.

```
docker login
```

Now, the image can be pushed to Docker Hub. Replace <dockerhub_username> with your Docker Hub username.

```
docker push <dockerhub_username>/mnist:latest
```

Exit from the VM before doing the next step. 

```
exit
```

**Deployment**

To create the service and the deployment, we use the command below and deploy the application to Kubernetes.

```
kubectl apply -f manifest.yaml
```

You should get an output similar to this - 

```
service/flask-test-service created
deployment.apps/flask-test-app created
```

To check if everything is running we need to check the pods and the service.

```
kubectl get pods
```

You should get an output similar to this.

!['Kubernetes'](Images/kubernetes_pods.png)

Checking the service.

```
kubectl get svc
```

!['Kubernetes'](Images/kubernetes_service.png)

Run this command to access the access the application thorugh tunnel URL. 

```
minikube service full-stack-ai
```

!['Kubernetes'](Images/tunnel.png)

If the service is successfully deployed, you should be able to view "Hello World" message in your brower - 

!['Kubernetes'](Images/Mozilla.png)

You can view the deployment and pods on the Kubernetes dashboard

You can convert the image to base64 [here](https://codebeautify.org/image-to-base64-converter).

You can access the endpoint using cURL.

```
curl -X POST "<Tunnel URL>/mnist" \\
  --header "Content-Type: application/json" \\
  -d '{
    "base64": <image base64>      
  }'
```
## Architecture

!['Full Stack AI Architecure'](Images/Architecture.png)

This MVP consists of a **PyTorch** inference module, **FastAPI** as RESTful API for backend server, **Docker** for containerisation and deployed on a **Kubernetes Cluster**. 

## Tasks

### 1. Prepare a MNIST deep learning model.

### 2. Fine-tune [FashionMNIST](https://pytorch.org/vision/stable/datasets.html#fashion-mnist) model.
