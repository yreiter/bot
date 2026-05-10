#!/usr/bin/env python3
"""
Test bot functionality without requiring real API keys.
Validates that bot logic works correctly.
"""

import os
import sys
from pathlib import Path
from unittest.mock import Mock, patch, MagicMock
import asyncio

# Add repo to path
sys.path.insert(0, str(Path(__file__).parent))

os.environ.setdefault("TELEGRAM_BOT_TOKEN", "123456789:test_token")
os.environ.setdefault("ANTHROPIC_API_KEY", "sk-ant-test-key-for-unit-tests")

def test_claude_call():
    """Test Claude API call without real keys"""
    print("Testing Claude API call...")

    # Create mock response
    mock_response = Mock()
    mock_response.content = [Mock(type="text", text="Hello from Claude!")]

    mock_client = Mock()
    mock_client.messages.create.return_value = mock_response

    with patch('bot.claude_client', mock_client):
        from bot import _call_claude
        result = _call_claude([{"role": "user", "content": "Hi"}])

        assert result == "Hello from Claude!", f"Expected greeting, got: {result}"
        mock_client.messages.create.assert_called_once()
        assert mock_client.messages.create.call_args.kwargs["model"] == "claude-opus-4-1-20250805"
        print("  ✅ Claude call works correctly")
        return True

def test_gpt_call():
    """Test GPT API call without real keys"""
    print("Testing GPT API call...")

    mock_client = Mock()
    mock_response = Mock()
    mock_response.choices = [Mock(message=Mock(content="Hello from GPT!"))]
    mock_client.chat.completions.create.return_value = mock_response

    with patch('bot.openai_client', mock_client):
        from bot import _call_gpt
        result = _call_gpt([{"role": "user", "content": "Hi"}])

        assert result == "Hello from GPT!", f"Expected greeting, got: {result}"
        print("  ✅ GPT call works correctly")
        return True

def test_message_splitting():
    """Test message splitting functionality"""
    print("Testing message splitting...")

    from bot import _split_message

    # Test normal message
    short = "Hello"
    assert _split_message(short) == ["Hello"]

    # Test long message
    long_msg = "x" * 5000
    chunks = _split_message(long_msg, limit=1000)
    assert len(chunks) > 1, "Should split long message"
    assert all(len(c) <= 1000 for c in chunks), "Chunks should respect limit"

    print("  ✅ Message splitting works correctly")
    return True

def test_reminder_parsing():
    """Test reminder time parsing"""
    print("Testing reminder parsing...")

    from bot import _parse_remind_seconds

    assert _parse_remind_seconds("30m") == 1800
    assert _parse_remind_seconds("2h") == 7200
    assert _parse_remind_seconds("1d") == 86400
    assert _parse_remind_seconds("invalid") is None

    print("  ✅ Reminder parsing works correctly")
    return True

def test_authorization():
    """Test user authorization logic"""
    print("Testing authorization...")

    from bot import is_authorized, allowed_user_ids

    # With no restrictions
    assert is_authorized(123456) == True, "Should allow all when no restrictions"

    # Add restrictions
    allowed_user_ids.add(111)
    allowed_user_ids.add(222)

    assert is_authorized(111) == True, "Should allow authorized user"
    assert is_authorized(999) == False, "Should deny unauthorized user"

    allowed_user_ids.clear()  # Reset

    print("  ✅ Authorization works correctly")
    return True

def main():
    print("\n" + "="*60)
    print("  Bot Test Suite")
    print("="*60 + "\n")

    tests = [
        test_message_splitting,
        test_reminder_parsing,
        test_authorization,
        test_claude_call,
        test_gpt_call,
    ]

    passed = 0
    failed = 0

    for test in tests:
        try:
            if test():
                passed += 1
        except Exception as e:
            print(f"  ❌ {test.__name__} failed: {e}")
            failed += 1

    print("\n" + "="*60)
    print(f"  Results: {passed} passed, {failed} failed")
    print("="*60 + "\n")

    if failed == 0:
        print("✅ All tests passed! Bot is ready to use.\n")
        print("Next steps:")
        print("  1. Run: python setup.py")
        print("  2. Add your API keys")
        print("  3. Run: python bot.py\n")
        return 0
    else:
        print("❌ Some tests failed. Check the errors above.\n")
        return 1

if __name__ == "__main__":
    sys.exit(main())
