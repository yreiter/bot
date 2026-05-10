FROM python:3.11-slim

WORKDIR /app

# Copy requirements and config
COPY requirements.txt .
COPY .env .
COPY bot.py .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Run bot
CMD ["python", "bot.py"]
