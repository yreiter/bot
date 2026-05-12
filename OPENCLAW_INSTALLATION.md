# OpenClaw / Claw Code Installation Guide

This guide covers installing **Claw Code** (the Rust CLI) locally on your machine and integrating it with the Telegram bot.

## Part 1: Local Installation of Claw Code CLI

### Prerequisites
- Git
- Rust toolchain
- An Anthropic API key (with credits)
- 10-15 minutes for initial build

### Installation Steps

#### Step 1: Install Rust
Rust is required to build Claw Code from source.

**On Linux/macOS:**
```bash
curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh
source $HOME/.cargo/env
```

**On Windows (PowerShell):**
```powershell
irm https://astro.build/install/windows.ps1 | iex
```

Verify installation:
```bash
rustc --version
cargo --version
```

#### Step 2: Clone Claw Code Repository
```bash
git clone https://github.com/ultraworkers/claw-code
cd claw-code/rust
```

#### Step 3: Build the Project
```bash
cargo build --workspace --release
```

This will take 5-10 minutes on first build. The binary will be created at:
- Linux/macOS: `./target/release/claw`
- Windows: `.\target\release\claw.exe`

#### Step 4: Configure Anthropic API Key

**On Linux/macOS:**
```bash
export ANTHROPIC_API_KEY="your-api-key-here"
```

**On Windows (PowerShell):**
```powershell
$env:ANTHROPIC_API_KEY = "your-api-key-here"
```

To make this permanent, add it to your shell profile (`.bashrc`, `.zshrc`, PowerShell profile, etc.)

#### Step 5: Verify Installation
```bash
./target/release/claw doctor
```

You should see output confirming:
- ✓ Claw environment detected
- ✓ API key configured
- ✓ All systems operational

#### Step 6: Optional - Create Alias for Easy Access

**On Linux/macOS:**
Add to `~/.bashrc` or `~/.zshrc`:
```bash
alias claw=/path/to/claw-code/rust/target/release/claw
```

**On Windows (PowerShell):**
Add to PowerShell profile:
```powershell
Set-Alias claw "C:\path\to\claw-code\rust\target\release\claw.exe"
```

### Testing Your Installation

Try a simple command:
```bash
claw exec-command "what time is it?"
claw exec-command "list files in my current directory"
```

### Troubleshooting

| Issue | Solution |
|-------|----------|
| `cargo: command not found` | Add Rust to PATH: `source $HOME/.cargo/env` |
| Build fails with dependency errors | Update Rust: `rustup update` |
| API key not found | Check: `echo $ANTHROPIC_API_KEY` (Linux/macOS) or `$env:ANTHROPIC_API_KEY` (Windows) |
| Permission denied (Linux/macOS) | Run: `chmod +x ./target/release/claw` |
| `claw: command not found` | Use full path or create alias (see Step 6) |

---

## Part 2: Bot Integration

The Telegram bot now supports OpenClaw integration. See the **OpenClaw Commands** section in the main [README.md](./README.md) for usage.

### Quick Start with Bot

Once the bot is running, you can use the `/openclaw` command:

```
/openclaw list files in my documents folder
/openclaw search for TODO comments in my code
/openclaw create a new text file with hello world
```

### For Developers: Installing Dependencies

To run the bot with OpenClaw support:

```bash
pip install -r requirements.txt
python bot.py
```

The claw-code-agent Python SDK is already included in `requirements.txt`.

---

## Resources

- [Claw Code Official Site](https://claw-code.codes/)
- [Anthropic API Documentation](https://docs.anthropic.com/)
- [OpenClaw Skills Registry](https://clawhub.ai/)
- [GitHub Repository](https://github.com/ultraworkers/claw-code)

## Next Steps

1. Complete the local installation above
2. Start using `claw` commands in your terminal
3. Use the bot's `/openclaw` command for automated tasks via Telegram
4. Explore available skills at [ClawHub](https://clawhub.ai/)

---

**Questions?** Check the troubleshooting section or visit the [GitHub repository](https://github.com/ultraworkers/claw-code/issues) for issues.
