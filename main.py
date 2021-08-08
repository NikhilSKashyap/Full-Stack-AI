from fastapi import FastAPI
from infer_mnist import infer_mnist
from infer_fmnist import infer_fmnist

from pydantic import BaseModel

app = FastAPI()

class Data(BaseModel):
    base64str: str

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.post("/mnist")
async def main(data:Data):
    return infer_mnist(data.base64str)

@app.post("/fmnist")
async def main(data:Data):
    return infer_fmnist(data.base64str)

