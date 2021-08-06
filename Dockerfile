FROM tiangolo/uvicorn-gunicorn-fastapi:python3.8

COPY * .

RUN pip install -r requirements.txt

RUN pip install torch==1.7.1+cpu torchvision==0.8.2+cpu torchaudio==0.7.2 -f https://download.pytorch.org/whl/torch_stable.html

EXPOSE 80

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]

