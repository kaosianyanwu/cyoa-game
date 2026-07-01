"""
Module 7: Tracked Stat
Build on Module 6 — add a stat (e.g. budget) modified by choices.
"""

LOG_FILE = "ending.txt"
STARTING_STAT = 60  # TODO: rename/adjust to match your GAME_PLAN (budget, health, etc.)
STAT_NAME = "budget"  # TODO: change if you track something else

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
        "stat_effect": -20,  # TODO: adjust amount
        "ending": "TODO: Ending A",
    },
    {
        "text": "TODO: Free path.",
        "ending": "TODO: Ending B",
    },
]


def show_scene(scene, name, stats):
    # TODO: Print scene text (use .format or f-strings for {name} and stat values)
    pass


def get_choice(valid_options):
    pass


def apply_stat_effect(scene, stats):
    """If scene has stat_effect, update stats[STAT_NAME]."""
    # TODO: implement
    pass


def write_ending(name, ending_title, stats):
    # TODO: write ending + final stat to LOG_FILE
    pass


def run_game(name):
    stats = {STAT_NAME: STARTING_STAT}
    scene_index = 0
    # TODO: game loop — apply stat effects, show final stat at ending
    pass


def main():
    print("TODO: Your Game Title")
    name = input("What's your name? ")
    print(f"Welcome, {name}!")
    run_game(name)


if __name__ == "__main__":
    main()
