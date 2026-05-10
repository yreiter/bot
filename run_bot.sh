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

# Load environment
export $(grep -v '^#' .env | xargs)

# Validate API keys
if [ -z "$TELEGRAM_BOT_TOKEN" ] || [ "$TELEGRAM_BOT_TOKEN" = "your_telegram_bot_token_here" ]; then
    echo "❌ TELEGRAM_BOT_TOKEN not set"
    exit 1
fi

if [ -z "$ANTHROPIC_API_KEY" ] || [ "$ANTHROPIC_API_KEY" = "your_anthropic_api_key_here" ]; then
    echo "❌ ANTHROPIC_API_KEY not set"
    exit 1
fi

echo "✅ Configuration loaded"
echo "🔌 Connecting to Telegram..."
echo ""

# Try to run with available Python
python3 bot.py 2>&1 &
BOT_PID=$!
echo "Bot started with PID: $BOT_PID"

# Keep script running
wait $BOT_PID
