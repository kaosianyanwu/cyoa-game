"""Tests for Module 5 acceptance criteria."""

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


def test_show_scene_function_exists():
    assert callable(game.show_scene)
    assert len(inspect.signature(game.show_scene).parameters) >= 1


def test_get_choice_function_exists():
    assert callable(game.get_choice)
    assert len(inspect.signature(game.get_choice).parameters) >= 1


def test_get_choice_validates(monkeypatch):
    inputs = iter(["9", "bad", "1"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))
    result = game.get_choice(["1", "2"])
    assert result == "1"


def test_show_scene_prints_text(capsys):
    scene = {"text": "A dark hallway.", "choices": {"1": 0, "2": 1}}
    game.show_scene(scene)
    out = capsys.readouterr().out
    assert "hallway" in out.lower()


def test_main_calls_show_scene_and_get_choice(main_body):
    body = main_body(game)
    assert "show_scene(" in body
    assert "get_choice(" in body


def test_behaves_like_module_4_writes_and_reads_file(tmp_path, monkeypatch, capsys):
    log_file = tmp_path / "ending.txt"
    marker = "PRIOR_RUN: Casey reached ending: Ending A"
    log_file.write_text(marker)
    monkeypatch.setattr(game, "LOG_FILE", str(log_file))
    monkeypatch.chdir(tmp_path)
    monkeypatch.setattr(sys, "stdin", __import__("io").StringIO("Casey\n1\n"))
    game.main()
    out = capsys.readouterr().out
    assert marker in out, "Still read the previous ending file like Module 4"
    assert "Casey" in log_file.read_text()
