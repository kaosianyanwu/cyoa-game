"""
Module 9: Classes + JSON Save/Load

COPY FIRST: paste your finished Module 8 game.py here, then wrap state in
Player and add save/load. Hardest module — take your time.
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
        self.name = name
        self.current_scene = "start"
        self.stats = {STAT_NAME: STARTING_STAT}

    def to_dict(self):
        pass

    @classmethod
    def from_dict(cls, data):
        pass


def save_game(player):
    pass


def load_game():
    pass


def play(player):
    # TODO: STORY loop + save_game(player) after each choice
    # TODO: on ending, clear save file
    pass


def main():
    print("TODO: Your Game Title")
    # TODO: load_game() → offer resume, or new Player(name) → play()
    pass


if __name__ == "__main__":
    main()
