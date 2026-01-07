FROM python:3.11-slim

WORKDIR /app
COPY rerquirements.txt .
RUN pip install --no-cache-dir -r rerquirements.txt

COPY app ./app
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]