"""Tests for Module 9 acceptance criteria."""

import importlib.util
import json
import sys
from pathlib import Path

MODULE_DIR = Path(__file__).parent
sys.path.insert(0, str(MODULE_DIR))

spec = importlib.util.spec_from_file_location("game", MODULE_DIR / "game.py")
game = importlib.util.module_from_spec(spec)
spec.loader.exec_module(game)


def test_player_class_holds_state():
    assert hasattr(game, "Player")
    player = game.Player("Test")
    assert player.name == "Test"
    assert hasattr(player, "current_scene")
    assert hasattr(player, "stats")


def test_save_game_writes_json_after_state_change(tmp_path, monkeypatch):
    save_path = tmp_path / "save.json"
    monkeypatch.setattr(game, "SAVE_FILE", str(save_path))
    player = game.Player("Sam")
    player.current_scene = "path_a"
    player.stats = {game.STAT_NAME: 40}
    game.save_game(player)
    assert save_path.exists()
    data = json.loads(save_path.read_text())
    assert data["name"] == "Sam"
    assert data["current_scene"] == "path_a"
    assert data["stats"][game.STAT_NAME] == 40


def test_load_game_restores_exact_progress(tmp_path, monkeypatch):
    save_path = tmp_path / "save.json"
    monkeypatch.setattr(game, "SAVE_FILE", str(save_path))
    original = game.Player("Max")
    original.current_scene = "path_b"
    original.stats = {game.STAT_NAME: 25}
    game.save_game(original)
    restored = game.load_game()
    assert restored is not None
    assert restored.name == "Max"
    assert restored.current_scene == "path_b"
    assert restored.stats[game.STAT_NAME] == 25


def test_load_missing_returns_none(tmp_path, monkeypatch):
    monkeypatch.setattr(game, "SAVE_FILE", str(tmp_path / "nope.json"))
    assert game.load_game() is None
