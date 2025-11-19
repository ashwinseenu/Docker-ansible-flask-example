FROM python:3.9-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
EXPOSE 5000
# Runs 4 worker processes for real-time concurrency
CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:5000", "app:app"]
