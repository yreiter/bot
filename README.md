# Telegram AI Bot 🤖

Personal assistant bot for Telegram with Claude AI support, reminders, and optional group management.

## Quick Start

### 1. Get Your API Keys

**Telegram Bot Token:**
- Go to [@botfather](https://t.me/botfather) on Telegram
- Send `/newbot`
- Follow the steps to create a bot
- Copy your token (looks like `123456789:ABCdefGHIjklmNOPqrstuVWXyz`)

**Anthropic API Key (Claude):**
- Go to [console.anthropic.com](https://console.anthropic.com/)
- Create an API key
- Copy it

### 2. Configure the Bot

Edit the `.env` file:
```bash
TELEGRAM_BOT_TOKEN=123456789:ABCdefGHIjklmNOPqrstuVWXyz
ANTHROPIC_API_KEY=sk-ant-v4-xxxxxxxxxxxxxxxxxxxxxxxxxxxx
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the Bot

```bash
python bot.py
```

The bot will start and wait for messages. Send it a message from Telegram to test!

## Features

### AI Chat
- **Claude (Default):** Use Anthropic's Claude Opus for intelligent conversations
- **ChatGPT:** Optional support for OpenAI's GPT-4o (add `OPENAI_API_KEY` to .env)
- Switch models with `/claude` or `/gpt`

### Reminders
```
/remind 30m Buy milk
/remind 2h Meeting with John
/remind 1d Renew subscription
/reminders  # See active reminders
```

### OpenClaw AI Agent
Execute autonomous AI tasks with OpenClaw:
```
/openclaw list files in current directory
/openclaw search for TODO comments in my code
/openclaw create a new file with sample content
```
The bot uses OpenClaw's AI agent to autonomously execute tasks. Results are sent back via Telegram.

**Setup:**
- Ensure `ANTHROPIC_API_KEY` is configured (same as Claude)
- See [OPENCLAW_INSTALLATION.md](OPENCLAW_INSTALLATION.md) for detailed setup

### Group Management
Two options:

**Option A: Via Personal Account (Recommended)**
- Get API credentials from [my.telegram.org/apps](https://my.telegram.org/apps)
- Add `TELEGRAM_API_ID` and `TELEGRAM_API_HASH` to .env
- Use `/login` to authenticate (one-time setup)
- Use `/mygroups` to see all your groups
- Send messages to any group: `/send GroupName | Your message`

**Option B: Bot Added to Groups**
- Add the bot to your groups
- Use `/addgroup FriendlyName` from within the group
- Send messages: `/send FriendlyName | Your message`

### Commands
```
/start     - New conversation
/clear     - Clear chat history
/claude    - Switch to Claude
/gpt       - Switch to ChatGPT
/openclaw  - Execute autonomous AI task
/help      - Show all features
/login     - Connect to personal account (userbot)
/mygroups  - List your groups (requires /login)
/send      - Send message to group
/remind    - Set a reminder
/reminders - View active reminders
```

## Configuration (.env)

| Variable | Required | Example |
|----------|----------|---------|
| `TELEGRAM_BOT_TOKEN` | Yes | `123456:ABC...` |
| `ANTHROPIC_API_KEY` | Yes | `sk-ant-...` |
| `OPENAI_API_KEY` | No | `sk-...` |
| `TELEGRAM_API_ID` | No* | `1234567` |
| `TELEGRAM_API_HASH` | No* | `abcd1234...` |
| `TELEGRAM_PHONE` | No | `+972501234567` |
| `TELEGRAM_2FA_PASSWORD` | No | Your 2FA password |
| `ALLOWED_USER_IDS` | No | `123456,789012` |
| `MAX_HISTORY_MESSAGES` | No | `40` |

*Required only if using `/login` for group access.

## Troubleshooting

### "Phone number is invalid"
- For `/login`, use full international format: `+1234567890`
- Or set `TELEGRAM_PHONE` in .env

### "Error communicating with AI"
- Check that `ANTHROPIC_API_KEY` is valid and hasn't expired
- Verify you have API credits at [console.anthropic.com](https://console.anthropic.com/)

### Bot doesn't respond
- Check that `TELEGRAM_BOT_TOKEN` is correct
- Make sure bot is running: `python bot.py`
- Check logs for errors

## Notes

- Conversations are kept in memory (default: 40 messages)
- Messages are NOT persisted to a database
- Clear history with `/clear` or `/start`
- Hebrew language is fully supported
