# Claw Code CLI - Local Installation ✅

## Installation Status

✅ **Claw Code CLI is installed and ready to use!**

### Details:
- **Location**: `/tmp/claw-code/rust/target/release/claw`
- **Version**: 0.1.0
- **Built**: 2026-05-12
- **Alias**: `claw` (available in bash)

## Quick Start

### 1. Set Your API Key

```bash
export ANTHROPIC_API_KEY="sk-ant-v4-xxxxxxxxxxxxxxxxxxxxx"
```

Or add to `~/.bashrc` to make it permanent:
```bash
echo 'export ANTHROPIC_API_KEY="sk-ant-v4-xxxxxxxxxxxxxxxxxxxxx"' >> ~/.bashrc
source ~/.bashrc
```

### 2. Verify Installation

```bash
claw doctor
```

Expected output:
```
Doctor

Summary
  OK               5
  Warnings         0
  Failures         0
```

### 3. Try a Command

```bash
claw exec-command "list files in current directory"
claw exec-command "what time is it?"
```

## Using with Telegram Bot

Your Telegram bot already has OpenClaw integrated!

Just send:
```
/openclaw list files in my home directory
/openclaw search for python files
/openclaw create a new text file
```

## Command Examples

```bash
# List files
claw exec-command "list all files in current directory"

# Search for files
claw exec-command "search for TODO comments in my code"

# Create files
claw exec-command "create a file named test.txt with hello world"

# Web operations
claw exec-command "search for information about rust programming"

# Execute shell commands
claw exec-command "show me the current date and time"
```

## Binary Location

If you want to move it elsewhere or create a symlink:

```bash
# Option 1: Create symlink in /usr/local/bin
sudo ln -s /tmp/claw-code/rust/target/release/claw /usr/local/bin/claw

# Option 2: Copy to home directory
mkdir -p ~/.local/bin
cp /tmp/claw-code/rust/target/release/claw ~/.local/bin/
export PATH="$HOME/.local/bin:$PATH"
```

## Troubleshooting

### "claw: command not found"
```bash
# Add alias to bashrc
echo 'alias claw="/tmp/claw-code/rust/target/release/claw"' >> ~/.bashrc
source ~/.bashrc
```

### "no supported auth env vars were found"
```bash
# Set API key
export ANTHROPIC_API_KEY="your-key-here"

# Verify
claw doctor
```

### Build Source Code Again
```bash
cd /tmp/claw-code/rust
cargo build --workspace --release
```

## Resources

- [Claw Code Official Site](https://claw-code.codes/)
- [GitHub Repository](https://github.com/ultraworkers/claw-code)
- [Usage Guide](https://claw-code.codes/getting-started)

---

**Installed**: 2026-05-12
**Build Time**: 1m 33s
**Status**: ✅ Ready to use
