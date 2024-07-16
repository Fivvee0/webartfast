FROM python:3.11-slim

WORKDIR /app

COPY website/ /website
COPY components/ /components
COPY docker/ /app

RUN pip install --no-cache-dir -r /app/requirements.txt

EXPOSE 80

CMD ["python", "/app/app.py"]
