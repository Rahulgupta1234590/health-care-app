FROM python:3.11-slim

WORKDIR /app

# ✅ Correct file name
COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 5000

# ✅ Use the correct entrypoint (check if your app starts with run.py or app.py)
CMD ["python", "app.py"]
