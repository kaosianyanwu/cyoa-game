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


def test_player_class():
    assert hasattr(game, "Player")
    p = game.Player("Test")
    assert hasattr(p, "name")
    assert hasattr(p, "current_scene")
    assert hasattr(p, "stats")


def test_to_dict_round_trip():
    p = game.Player("Alex")
    data = p.to_dict()
    assert isinstance(data, dict)
    restored = game.Player.from_dict(data)
    assert restored.name == p.name
    assert restored.current_scene == p.current_scene
    assert restored.stats == p.stats


def test_save_and_load(tmp_path, monkeypatch):
    save_path = tmp_path / "save.json"
    monkeypatch.setattr(game, "SAVE_FILE", str(save_path))
    player = game.Player("Sam")
    game.save_game(player)
    assert save_path.exists()
    loaded = game.load_game()
    assert loaded is not None
    assert loaded.name == "Sam"


def test_load_missing_returns_none(tmp_path, monkeypatch):
    monkeypatch.setattr(game, "SAVE_FILE", str(tmp_path / "nope.json"))
    assert game.load_game() is None


def test_save_writes_valid_json(tmp_path, monkeypatch):
    save_path = tmp_path / "save.json"
    monkeypatch.setattr(game, "SAVE_FILE", str(save_path))
    player = game.Player("Jo")
    player.current_scene = "path_a"
    player.stats = {game.STAT_NAME: 40}
    game.save_game(player)
    data = json.loads(save_path.read_text())
    assert "name" in data and "current_scene" in data and "stats" in data
