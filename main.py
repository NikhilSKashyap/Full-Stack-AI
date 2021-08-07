from fastapi.logger import logger
import io
import json
import base64
import uuid
import logging
import sys
from io import BytesIO
import base64
from typing import List
from PIL import Image
import uvicorn
from fastapi import FastAPI, File
from starlette.responses import StreamingResponse
from fastapi.responses import FileResponse
from fastapi.encoders import jsonable_encoder

import logging
import torch
from model import Net
from torchvision import datasets, transforms

logging.basicConfig(stream=sys.stdout, level=logging.INFO)

import os
from pydantic import BaseModel

app = FastAPI()

gunicorn_logger = logging.getLogger('gunicorn.error')
logger.handlers = gunicorn_logger.handlers

class Data(BaseModel):
    base64str: str

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.post("/predict")
async def main(data:Data):
    model = Net()
    model.load_state_dict(torch.load(
        'mnist_cnn.pt', map_location=torch.device('cpu')))
    model.eval()

    # mnist_dts_val = datasets.MNIST('data', train=False, download=False)

    transform = transforms.Compose([
        transforms.Resize((28, 28)),
        transforms.ToTensor(),
        transforms.Normalize((0.1307,), (0.3081,)),
    ])

    base64_img_bytes =data.base64str.encode('utf-8')
    img = Image.open(BytesIO(base64.b64decode(base64_img_bytes)))

    output = model(torch.unsqueeze(
        transform(img.convert('L')), 0))
    
    pred = int(output.argmax(dim=1, keepdim=True))

    return {"pred":str(pred)}

if __name__ != '__main__':
    logger.setLevel(gunicorn_logger.level)
else:
    uvicorn.run("main:app", host='127.0.0.1', port=8080)
    logger.setLevel(logging.DEBUG)

