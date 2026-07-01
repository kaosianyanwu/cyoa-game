"""Tests for Module 8 acceptance criteria."""

import importlib.util
import sys
from pathlib import Path

MODULE_DIR = Path(__file__).parent
sys.path.insert(0, str(MODULE_DIR))

spec = importlib.util.spec_from_file_location("game", MODULE_DIR / "game.py")
game = importlib.util.module_from_spec(spec)
spec.loader.exec_module(game)


def test_story_is_dict_with_string_keys():
    assert isinstance(game.STORY, dict)
    assert "start" in game.STORY
    assert all(isinstance(k, str) for k in game.STORY)


def test_scenes_have_text():
    for scene_id, scene in game.STORY.items():
        assert "text" in scene, f"Scene {scene_id!r} needs 'text'"


def test_branching_scene_has_choices():
    start = game.STORY["start"]
    assert "choices" in start
    key, (label, next_id) = next(iter(start["choices"].items()))
    assert isinstance(next_id, str), "choices should map to next scene id strings"


def test_ending_scene_has_no_choices():
    endings = [s for s in game.STORY.values() if "ending" in s]
    assert len(endings) >= 1
    for scene in endings:
        assert "choices" not in scene


def test_play_advances_by_scene_id(monkeypatch, capsys):
    monkeypatch.setattr(sys, "stdin", __import__("io").StringIO("Quinn\n1\n"))
    game.main()
    out = capsys.readouterr().out
    assert "THE END" in out or "End" in out or "ending" in out.lower()
