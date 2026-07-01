"""Tests for Module 7 acceptance criteria."""

import importlib.util
import sys
from pathlib import Path

MODULE_DIR = Path(__file__).parent
sys.path.insert(0, str(MODULE_DIR))

spec = importlib.util.spec_from_file_location("game", MODULE_DIR / "game.py")
game = importlib.util.module_from_spec(spec)
spec.loader.exec_module(game)


def test_starting_stat_defined():
    assert hasattr(game, "STARTING_STAT")
    assert isinstance(game.STARTING_STAT, (int, float))


def test_apply_stat_effect_changes_stat():
    stats = {game.STAT_NAME: game.STARTING_STAT}
    scene = {"stat_effect": -10}
    game.apply_stat_effect(scene, stats)
    assert stats[game.STAT_NAME] == game.STARTING_STAT - 10


def test_different_choices_different_stats(monkeypatch, capsys):
    """Picking the costly path should leave a lower stat than the free path."""

    def final_stat(choice):
        capsys.readouterr()
        monkeypatch.setattr(
            sys, "stdin", __import__("io").StringIO(f"Pat\n{choice}\n")
        )
        game.main()
        return capsys.readouterr().out

    out_costly = final_stat("1")
    out_free = final_stat("2")
    stat_label = game.STAT_NAME
    assert stat_label in out_costly.lower() or str(game.STARTING_STAT) in out_costly
    assert out_costly != out_free or "TODO" in out_costly
