"""Tests for Module 4 acceptance criteria."""

import importlib.util
import sys
from pathlib import Path

MODULE_DIR = Path(__file__).parent
sys.path.insert(0, str(MODULE_DIR))

spec = importlib.util.spec_from_file_location("game", MODULE_DIR / "game.py")
game = importlib.util.module_from_spec(spec)
spec.loader.exec_module(game)


def test_scenes_is_list_with_at_least_three():
    assert isinstance(game.SCENES, list)
    assert len(game.SCENES) >= 3


def test_uses_while_loop():
    source = (MODULE_DIR / "game.py").read_text()
    assert "while " in source


def test_writes_ending_file(tmp_path, monkeypatch, capsys):
    log_file = tmp_path / "ending.txt"
    monkeypatch.setattr(game, "LOG_FILE", str(log_file))
    monkeypatch.chdir(tmp_path)
    monkeypatch.setattr(sys, "stdin", __import__("io").StringIO("Jordan\n1\n"))
    game.main()
    assert log_file.exists(), "Write ending info to a file on completion"
    content = log_file.read_text()
    assert "Jordan" in content
    assert "TODO" not in content
