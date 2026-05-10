FROM python:3.11-slim

WORKDIR /app

# Copy only application files. Secrets such as .env should be supplied by the
# runtime environment, not baked into the Docker image.
COPY requirements.txt .
COPY bot.py .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Run bot
CMD ["python", "bot.py"]
