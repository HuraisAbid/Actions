# Use official Python image
FROM python:3.10-slim

WORKDIR /app

# Copy files
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Run Flask app
CMD ["python", "app/app.py"]

