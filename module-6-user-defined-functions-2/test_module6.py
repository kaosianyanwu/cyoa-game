"""Tests for Module 6 acceptance criteria."""

import importlib.util
import inspect
import sys
from pathlib import Path

MODULE_DIR = Path(__file__).parent
sys.path.insert(0, str(MODULE_DIR))

spec = importlib.util.spec_from_file_location("game", MODULE_DIR / "game.py")
game = importlib.util.module_from_spec(spec)
spec.loader.exec_module(game)


def test_at_least_four_helper_functions():
    funcs = [
        name
        for name, obj in inspect.getmembers(game, inspect.isfunction)
        if name != "main" and obj.__module__ == game.__name__
    ]
    assert len(funcs) >= 4, f"Define at least 4 helper functions; found: {funcs}"


def test_main_is_short():
    source = inspect.getsource(game.main)
    non_empty = [ln for ln in source.splitlines() if ln.strip() and not ln.strip().startswith("#")]
    assert len(non_empty) <= 12, "Keep main() short — delegate to helper functions"


def test_choice_labels_not_placeholder(capsys):
    scene = game.SCENES[0]
    game.show_scene(scene)
    out = capsys.readouterr().out
    assert "..." not in out
    assert "TODO" not in out


def test_full_game(tmp_path, monkeypatch):
    log_file = tmp_path / "ending.txt"
    monkeypatch.setattr(game, "LOG_FILE", str(log_file))
    monkeypatch.chdir(tmp_path)
    monkeypatch.setattr(sys, "stdin", __import__("io").StringIO("Riley\n1\n"))
    game.main()
    assert log_file.exists()
