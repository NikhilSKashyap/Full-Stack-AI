import torch
from model import Net
from torchvision import datasets, transforms
from io import BytesIO
from PIL import Image
import base64

def infer_mnist(base64str):
    """
    This script infers MNIST dataset.
    Args:
        base64str (str): Base64 byte string of the mnsit image. 
    Returns:
        pred (dict): Predicted value of mnist input.
    """
    model = Net()
    model.load_state_dict(torch.load(
        'mnist_cnn.pt', map_location=torch.device('cpu')))
    model.eval()

    transform = transforms.Compose([
        transforms.Resize((28, 28)),
        transforms.ToTensor(),
        transforms.Normalize((0.1307,), (0.3081,)),
    ])

    base64_img_bytes = base64str.encode('utf-8')
    img = Image.open(BytesIO(base64.b64decode(base64_img_bytes)))

    output = model(torch.unsqueeze(
        transform(img.convert('L')), 0))
    
    pred = int(output.argmax(dim=1, keepdim=True))

    return {"pred":pred}