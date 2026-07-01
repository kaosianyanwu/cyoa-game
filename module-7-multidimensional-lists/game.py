"""
Module 7: Tracked Stat (Multi-Dimensional Lists)

COPY FIRST: paste your finished Module 6 game.py here, then add a tracked stat.
Folder name matches the syllabus; this module adds one stat (e.g. budget)
that changes based on choices. Keep all Module 6 behavior working.
"""

import os

LOG_FILE = "ending.txt"
STARTING_STAT = 60  # TODO: match your GAME_PLAN
STAT_NAME = "budget"  # TODO: rename if you track something else

SCENES = [
    {
        "text": "TODO: Opening scene. You have ${stat}.",
        "choices": {
            "1": ("TODO: Choice that costs something", 1),
            "2": ("TODO: Choice that is free", 2),
        },
    },
    {
        "text": "TODO: Paid path.",
        "stat_effect": -20,
        "ending": "TODO: Ending A",
    },
    {
        "text": "TODO: Free path.",
        "ending": "TODO: Ending B",
    },
]


def show_previous_ending():
    if os.path.exists(LOG_FILE):
        pass


def show_scene(scene, name, stats):
    pass


def get_choice(valid_options):
    pass


def apply_stat_effect(scene, stats):
    """If scene has stat_effect, update stats[STAT_NAME]."""
    pass


def write_ending(name, ending_title, stats):
    pass


def run_game(name):
    stats = {STAT_NAME: STARTING_STAT}
    pass


def main():
    show_previous_ending()
    print("TODO: Your Game Title")
    name = input("What's your name? ")
    print(f"Welcome, {name}!")
    run_game(name)


if __name__ == "__main__":
    main()
