"""
Module 9: Classes + JSON Save/Load
Build on Module 8 — Player class and persistent saves.
"""

import json
import os

SAVE_FILE = "save.json"
STAT_NAME = "budget"
STARTING_STAT = 60

STORY = {
    "start": {
        "text": "TODO: Opening scene for {name}. Budget: ${budget}.",
        "choices": {
            "1": ("TODO: First choice", "path_a"),
            "2": ("TODO: Second choice", "path_b"),
        },
    },
    "path_a": {
        "text": "TODO: Path A.",
        "stat_effect": -20,
        "ending": "TODO: Ending A",
    },
    "path_b": {
        "text": "TODO: Path B.",
        "ending": "TODO: Ending B",
    },
}


class Player:
    """Bundle player state for easy save/load."""

    def __init__(self, name):
        # TODO: confirm these defaults match your GAME_PLAN
        self.name = name
        self.current_scene = "start"
        self.stats = {STAT_NAME: STARTING_STAT}

    def to_dict(self):
        # TODO: return dict with name, current_scene, stats
        pass

    @classmethod
    def from_dict(cls, data):
        # TODO: reconstruct a Player from saved data
        pass


def save_game(player):
    # TODO: json.dump player.to_dict() to SAVE_FILE
    pass


def load_game():
    # TODO: if SAVE_FILE exists, load and return Player.from_dict(...); else None
    pass


def play(player):
    # TODO: game loop using STORY[player.current_scene]
    # TODO: call save_game(player) after each choice
    # TODO: on ending, print final stats and remove/clear save file
    pass


def main():
    print("TODO: Your Game Title")
    # TODO: try load_game(); if save exists, ask to resume
    # TODO: otherwise create new Player and play
    pass


if __name__ == "__main__":
    main()
