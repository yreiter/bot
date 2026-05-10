#!/bin/bash
# Run the Telegram AI Bot

# Try different Python versions and configurations
echo "🤖 Starting Telegram AI Bot..."
echo ""

# Check if .env exists
if [ ! -f .env ]; then
    echo "❌ .env file not found!"
    echo "Run: python setup.py"
    exit 1
fi

echo "✅ Configuration file found"
echo "🔌 Connecting to Telegram..."
echo ""

# Try to run with available Python
python3 bot.py 2>&1 &
BOT_PID=$!
echo "Bot started with PID: $BOT_PID"

# Keep script running
wait $BOT_PID
