"""
Module 9: Classes + JSON Save/Load

COPY FIRST: paste your finished Module 8 game.py here, then add Player + save/load.
JSON save after each choice; player can quit and resume where they left off.
"""

import json
import os

SAVE_FILE = "save.json"
STAT_NAME = "budget"
STARTING_STAT = 60
STORY = {}  # TODO: carry your STORY forward from Module 8


class Player:
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
    pass


def main():
    pass


if __name__ == "__main__":
    main()
