"""Tests for Module 3 acceptance criteria."""

import importlib.util
import sys
from pathlib import Path

MODULE_DIR = Path(__file__).parent
sys.path.insert(0, str(MODULE_DIR))

spec = importlib.util.spec_from_file_location("game", MODULE_DIR / "game.py")
game = importlib.util.module_from_spec(spec)
spec.loader.exec_module(game)


def test_choice_1_and_2_produce_different_output(capsys, monkeypatch):
    def run_with(choice):
        monkeypatch.setattr(
            sys, "stdin", __import__("io").StringIO(f"Sam\n{choice}\n")
        )
        game.main()
        return capsys.readouterr().out

    out1 = run_with("1")
    out2 = run_with("2")
    assert out1 != out2, "Each choice should lead to different follow-up text"
    assert "TODO" not in out1 and "TODO" not in out2


def test_uses_if_elif():
    source = (MODULE_DIR / "game.py").read_text()
    assert "if " in source
    assert "elif " in source


def test_invalid_choice_handled(capsys, monkeypatch):
    monkeypatch.setattr(sys, "stdin", __import__("io").StringIO("Sam\n9\n"))
    game.main()
    out = capsys.readouterr().out.lower()
    assert "valid" in out or "invalid" in out or "not" in out
