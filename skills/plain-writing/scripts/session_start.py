#!/usr/bin/env python3
"""SessionStart hook: print the plain-writing rules into the session context.

Prints nothing when the user set the plugin option always_on to false.
Usage: session_start.py | session_start.py --selftest
The hook mode never fails: it always exits 0.
"""
import os
import sys
from pathlib import Path

RULES = Path(__file__).resolve().parent.parent / "references" / "rules.md"


def enabled(value):
    """Option value from CLAUDE_PLUGIN_OPTION_ALWAYS_ON. Unset means on."""
    return (value or "").strip().lower() not in ("false", "0", "no", "off")


def selftest():
    assert enabled(None) and enabled("") and enabled("true") and enabled("1")
    assert not enabled("false") and not enabled(" False ") and not enabled("0")
    text = RULES.read_text(encoding="utf-8")
    assert "\u2014" not in text, "rules.md contains an em dash"
    assert "## All writing" in text and "## Technical writing" in text
    print("ok")


def main(argv):
    if "--selftest" in argv:
        selftest()
        return
    try:
        if enabled(os.environ.get("CLAUDE_PLUGIN_OPTION_ALWAYS_ON")):
            print(RULES.read_text(encoding="utf-8"))
    except Exception:  # the SessionStart hook must never fail the session
        pass


if __name__ == "__main__":
    main(sys.argv[1:])
