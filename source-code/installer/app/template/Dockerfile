FROM python:3.11-slim

WORKDIR /app

COPY website/ ./website
COPY docker/ ./docker
COPY components/ ./components

RUN pip install -r docker/requirements.txt

EXPOSE 80

CMD ["python", "docker/app.py"]