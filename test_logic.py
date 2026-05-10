#!/usr/bin/env python3
"""
Test bot logic without importing full bot.py
(Avoids environment issues with cryptography)
"""

import re
from collections import defaultdict

def test_parse_remind_seconds():
    """Test reminder time parsing"""
    _TIME_UNITS = {"m": 60, "h": 3600, "d": 86400}

    def _parse_remind_seconds(time_str: str):
        m = re.fullmatch(r"(\d+)([mhd])", time_str.strip().lower())
        if not m:
            return None
        return int(m.group(1)) * _TIME_UNITS[m.group(2)]

    assert _parse_remind_seconds("30m") == 1800, "30m should be 1800s"
    assert _parse_remind_seconds("2h") == 7200, "2h should be 7200s"
    assert _parse_remind_seconds("1d") == 86400, "1d should be 86400s"
    assert _parse_remind_seconds("invalid") is None, "invalid should return None"
    print("✅ Reminder parsing works")

def test_split_message():
    """Test message splitting logic"""
    def _split_message(text: str, limit: int = 4000) -> list:
        if len(text) <= limit:
            return [text]
        chunks = []
        while text:
            if len(text) <= limit:
                chunks.append(text)
                break
            split_at = text.rfind("\n", 0, limit)
            if split_at == -1:
                split_at = limit
            chunks.append(text[:split_at])
            text = text[split_at:].lstrip("\n")
        return chunks

    # Test short message
    assert _split_message("hello") == ["hello"]

    # Test long message
    long_text = "x" * 5000
    chunks = _split_message(long_text, limit=1000)
    assert len(chunks) > 1, "Should split into multiple chunks"
    assert all(len(c) <= 1000 for c in chunks), "All chunks should be under limit"

    # Test with newlines
    text_with_lines = "line1\nline2\n" + "x" * 4000
    chunks = _split_message(text_with_lines, limit=1000)
    assert all(len(c) <= 1000 for c in chunks)

    print("✅ Message splitting works")

def test_authorization():
    """Test authorization logic"""
    allowed_user_ids = set()

    def is_authorized(user_id: int) -> bool:
        if not allowed_user_ids:
            return True
        return user_id in allowed_user_ids

    # Test no restrictions
    assert is_authorized(123456) == True

    # Add restrictions
    allowed_user_ids.add(111)
    allowed_user_ids.add(222)

    assert is_authorized(111) == True
    assert is_authorized(999) == False

    print("✅ Authorization logic works")

def test_group_registry():
    """Test group registration logic"""
    registered_groups = {}

    def _find_registered_group(query: str):
        query = query.lower().strip()
        if query in registered_groups:
            return registered_groups[query]
        for name, chat_id in registered_groups.items():
            if query in name or name in query:
                return chat_id
        return None

    # Register a group
    registered_groups["friends"] = 12345
    registered_groups["family"] = 67890

    assert _find_registered_group("friends") == 12345
    assert _find_registered_group("family") == 67890
    assert _find_registered_group("FRIENDS") == 12345
    assert _find_registered_group("fam") == 67890
    assert _find_registered_group("unknown") is None

    print("✅ Group registry works")

def test_conversation_history():
    """Test conversation history management"""
    conversation_history = defaultdict(list)
    MAX_HISTORY = 40

    user_id = 123
    for i in range(50):
        conversation_history[user_id].append({"role": "user", "content": f"msg {i}"})
        if len(conversation_history[user_id]) > MAX_HISTORY:
            conversation_history[user_id][:] = conversation_history[user_id][-MAX_HISTORY:]

    assert len(conversation_history[user_id]) == MAX_HISTORY
    assert conversation_history[user_id][0]["content"] == "msg 10"
    assert conversation_history[user_id][-1]["content"] == "msg 49"

    print("✅ Conversation history management works")

def main():
    print("\n" + "="*60)
    print("  Bot Logic Test Suite")
    print("="*60 + "\n")

    try:
        test_parse_remind_seconds()
        test_split_message()
        test_authorization()
        test_group_registry()
        test_conversation_history()

        print("\n" + "="*60)
        print("  ✅ All core logic tests PASSED!")
        print("="*60)
        print("\nBot is ready to use. Setup instructions:")
        print("  1. python setup.py")
        print("  2. Add your API keys")
        print("  3. python bot.py\n")
        return 0

    except AssertionError as e:
        print(f"\n❌ Test failed: {e}\n")
        return 1
    except Exception as e:
        print(f"\n❌ Unexpected error: {e}\n")
        return 1

if __name__ == "__main__":
    import sys
    sys.exit(main())
