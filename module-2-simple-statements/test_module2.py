"""Tests for Module 2 acceptance criteria."""

import importlib.util
import re
import sys
from pathlib import Path

MODULE_DIR = Path(__file__).parent
sys.path.insert(0, str(MODULE_DIR))

spec = importlib.util.spec_from_file_location("game", MODULE_DIR / "game.py")
game = importlib.util.module_from_spec(spec)
spec.loader.exec_module(game)


def test_main_runs(capsys, monkeypatch):
    monkeypatch.setattr(sys, "stdin", __import__("io").StringIO("Alex\n"))
    game.main()
    out = capsys.readouterr().out
    assert "TODO" not in out, "Replace placeholder title and scene text"
    assert "Alex" in out


def test_shows_two_numbered_choices(capsys, monkeypatch):
    monkeypatch.setattr(sys, "stdin", __import__("io").StringIO("Alex\n"))
    game.main()
    out = capsys.readouterr().out
    choices = re.findall(r"^\s*([12])\)", out, re.MULTILINE)
    assert len(choices) >= 2, "Print at least two numbered choices (1) and 2))"


def test_no_branching_yet():
    source = (MODULE_DIR / "game.py").read_text()
    lowered = source.lower()
    assert "if " not in lowered and "elif " not in lowered, (
        "Module 2 is display-only — save if/elif for Module 3"
    )
