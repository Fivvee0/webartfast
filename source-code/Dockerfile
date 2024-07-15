FROM python:3.11-slim

WORKDIR /app

COPY website/ ./website
COPY python/ ./python
COPY components/ ./components

RUN pip install -r python/requirements.txt

EXPOSE 80

CMD ["python", "python/app.py"]