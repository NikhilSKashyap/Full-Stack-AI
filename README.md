# Simple Vision-AI-as-a-service <!-- omit in toc -->

This mini project aims to build a very minimal-viable-product (MVP) for a Vision-AI-as-a-service prototype. 


### Background
The requirements and the provided sample codes serve a purpose to simulate a typical scenario when AI/ML engineers in a MLOps team pass a working deep learning model to a DevOps team to deploy it on production. We expect a Full Stack AI Engineer can **independently** handle this end-to-end development and deployment journey.

### How we evaluate the submission
Our evaluation process focuses on the Full Stack AI Engineer candidate being able to set up a stateless backend sever hosting an inference engine and receiving requests via RESTful API. The backend server is containerised and served in a Kubernetes cluster.


## Table of content <!-- omit in toc -->

- [Requirement](#requirement)
  - [Challenges](#challenges)
  - [How the service is tested](#how-the-service-is-tested)
  - [Submission](#submission)
- [Guideline](#guideline)
  - [Timeline](#timeline)
  - [Ask for help](#ask-for-help)
- [Sample codes](#sample-codes)
  - [Setup Streamlit](#setup-streamlit)
    - [Install dependencies](#install-dependencies)
    - [Train and save a MNIST model](#train-and-save-a-mnist-model)
    - [Launch the Streamlit server](#launch-the-streamlit-server)

## Requirement

The candidate will need to come up with an online service fulfilling requirements as follows:

1. Prepare a MNIST deep learning model
   - 📝 Checkpoint: Very basic deep learning skill
   - 💡 Hint: While you can use the sample codes `mnist.py` to train a PyTorch model or directly download it from [here](https://artifacts.instill.tech/mnist_cnn.pt), you are free to use any other framework that you are familiar with, such as TensorFlow, Caffe2, etc. 
2. Initiate a simple RESTful API backend server for hosting the model
   - 📝 Checkpoint: Backend skill
   - 💡 Hint: You can use any language and framework that you are familiar with, such as Python Flask, Go Gin, Node.js, etc. 
3. Containerise the backend server
   - 📝 Checkpoint: Container skill
   - 💡 Hint: You can use any OCI-standard technique that you familiar with, such as Docker, Podman, Buildah, etc.
4. Set up a local Kubernetes cluster and deploy the service on it
   - 📝 Checkpoint: Very basic Kubernetes skill
   - 💡 Hint: You can use any lightweight local Kubernetes solution that you are familiar with, such as `KinD`, `K3s`, `minikube`, etc.
5. Compile a `README.md` file to document the requirement 1 to 4 together with paragraphs discussing the strength and weakness of the MVP design in terms of its scalability, reliability, modifiability, observability and any security concerns (Kubernetes setup, TLS, etc.)
   - 📝 Checkpoint: Documentation skill
   - 💡 Hint: Please be concise and address as many concerns as you can.

### Challenges

The candidate can consider challenging themselves with these extra features:

1. An extra endpoint for serving a fine-tuned [FashionMNIST](https://pytorch.org/vision/stable/datasets.html#fashion-mnist) model.
2. A frontend web page for a simple UI for sending the image request and showing the response.
3. Self-host the service in your local Kubernetes cluster and use Cloudflare Argo Tunnel, ngrok or Inlets to expose your local resources.

### How the service is tested

We will locally build the backend server image and deploy the service on our local Kubernetes cluster using the manifest YAML files you provide.

Once the service has been successfully deployed, we will send requests with base64 image payload to test the endpoint using cURL:
```
curl -X POST "<the accessible endpoint of the inference service>" \
  --header "Content-Type: application/json" \
  -d '{
    "base64": <image base64>      
  }'
```

The response can be free-form as long as it contains the image classification result. 

### Submission

Wrap up everything into a zip/tar file containing all the source codes, the Kubernetes manifest YAML files, and the `README.md` file, and submit it via [here](https://forms.clickup.com/f/2e88k-2101/NDHDDFZAFYZMNL33HA).

## Guideline

### Timeline

While this mini project should take less than **5 hours**, we do not set a hard deadline for you to accomplish it. Generally we suggest you submit whatever you have achieved within a week after the assignment.

### Ask for help

Feel free to raise any questions and topic to discuss further with us. We will try to provide prompt helps and hints. The entire development process including the communication of the mini project does play a role in the evaluation process.


## Sample codes

The sample codes include a dummy PyTorch model in `model.py` in which the script `mnist.py` can use it to train a MNIST model and fine-tune the last layers of the model on the FashionMNIST dataset. A simple visualisation result based on streamlit can be found in `streamlit.py`.

### Setup Streamlit

#### Install dependencies
Under your favourite Python virtualenv (e.g., virtualenv, anaconda) with Python 3.8:

```bash
pip3 install torch torchvision streamlit torchinfo
```

#### Train and save a MNIST model

```bash
python mnist.py --save-model
```

#### Launch the Streamlit server

```bash
streamlit run simple_ui.py
```

You can now access the Streamlit server via `http://localhost:8501`