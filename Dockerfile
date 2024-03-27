FROM python:3.11-slim

COPY ..

RUN pip install -r requirements.txt

CMD['uvicron', 'main:app', '--host', '0.0.0.0', '--potr', '80']