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


def test_scenes_have_text_and_choices_shape():
    for scene_id, scene in game.STORY.items():
        assert "text" in scene, f"Scene {scene_id!r} needs 'text'"
    start = game.STORY["start"]
    assert "choices" in start
    _, (label, next_id) = next(iter(start["choices"].items()))
    assert isinstance(label, str)
    assert isinstance(next_id, str)


def test_game_loop_reads_from_story():
    source = (MODULE_DIR / "game.py").read_text()
    assert "STORY[" in source, "Look up scenes from the STORY dictionary"


def test_new_scene_is_data_only():
    """Adding a dict entry should be enough — no per-scene if/elif branches."""
    source = (MODULE_DIR / "game.py").read_text()
    branch_count = source.count('elif scene') + source.count('elif scene_id')
    assert branch_count == 0, "Avoid hardcoded elif branches per scene id"


def test_play_reaches_ending(monkeypatch, capsys):
    monkeypatch.setattr(sys, "stdin", __import__("io").StringIO("Quinn\n1\n"))
    game.main()
    out = capsys.readouterr().out
    assert "THE END" in out or "End" in out
