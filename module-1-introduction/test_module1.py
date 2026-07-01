"""Tests for Module 1 acceptance criteria."""

import importlib.util
import sys
from pathlib import Path

MODULE_DIR = Path(__file__).parent
sys.path.insert(0, str(MODULE_DIR))

spec = importlib.util.spec_from_file_location("game", MODULE_DIR / "game.py")
game = importlib.util.module_from_spec(spec)
spec.loader.exec_module(game)


def test_main_is_callable():
    assert callable(game.main)


def test_prints_title(capsys, monkeypatch):
    monkeypatch.setattr(sys, "stdin", __import__("io").StringIO("River\n"))
    game.main()
    captured = capsys.readouterr().out
    assert "TODO" not in captured, "Replace the placeholder title with your game title"
    assert captured.strip()


def test_asks_name_with_input():
    source = (MODULE_DIR / "game.py").read_text()
    assert "input(" in source


def test_greets_player_by_name(capsys, monkeypatch):
    monkeypatch.setattr(sys, "stdin", __import__("io").StringIO("River\n"))
    game.main()
    captured = capsys.readouterr().out
    assert "River" in captured
    assert "What's your name?" in captured or "name" in captured.lower()
