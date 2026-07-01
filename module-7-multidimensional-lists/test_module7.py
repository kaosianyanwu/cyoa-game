"""Tests for Module 7 acceptance criteria."""

import importlib.util
import sys
from pathlib import Path

MODULE_DIR = Path(__file__).parent
sys.path.insert(0, str(MODULE_DIR))

spec = importlib.util.spec_from_file_location("game", MODULE_DIR / "game.py")
game = importlib.util.module_from_spec(spec)
spec.loader.exec_module(game)


def test_tracked_stat_defined():
    assert hasattr(game, "STAT_NAME") or hasattr(game, "STARTING_STAT")
    source = (MODULE_DIR / "game.py").read_text()
    assert "stat" in source.lower()


def test_at_least_one_choice_modifies_stat():
    scenes = getattr(game, "SCENES", []) or getattr(game, "STORY", {}).values()
    has_effect = any(
        "stat_effect" in scene for scene in scenes if isinstance(scene, dict)
    )
    assert has_effect, "At least one scene should modify the tracked stat"


def test_apply_stat_effect_changes_stat():
    stats = {game.STAT_NAME: game.STARTING_STAT}
    scene = {"stat_effect": -10}
    game.apply_stat_effect(scene, stats)
    assert stats[game.STAT_NAME] == game.STARTING_STAT - 10
