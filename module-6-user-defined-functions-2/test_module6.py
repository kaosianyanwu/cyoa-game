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


def test_has_show_previous_ending():
    assert callable(game.show_previous_ending)


def test_main_is_short(main_body):
    lines = [ln for ln in main_body(game).splitlines() if ln.strip()]
    assert len(lines) <= 8, "Keep main() short — delegate to helper functions"


def test_main_calls_run_game(main_body):
    assert "run_game(" in main_body(game)


def test_helper_functions_exist():
    funcs = [
        name
        for name, obj in inspect.getmembers(game, inspect.isfunction)
        if name != "main" and obj.__module__ == game.__name__
    ]
    assert len(funcs) >= 2, "Split work across focused helper functions"


def test_show_scene_and_get_choice_still_exist():
    assert callable(game.show_scene)
    assert callable(game.get_choice)


def test_behaves_like_module_5(tmp_path, monkeypatch, capsys):
    log_file = tmp_path / "ending.txt"
    marker = "PRIOR_RUN: Riley reached ending: Ending B"
    log_file.write_text(marker)
    monkeypatch.setattr(game, "LOG_FILE", str(log_file))
    monkeypatch.chdir(tmp_path)
    monkeypatch.setattr(sys, "stdin", __import__("io").StringIO("Riley\n1\n"))
    game.main()
    out = capsys.readouterr().out
    assert marker in out
    assert log_file.exists()
