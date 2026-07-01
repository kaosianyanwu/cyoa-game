"""
Module 5: User-Defined Functions (Part 1)

COPY FIRST: paste your finished Module 4 game.py here, then extract functions.
Behavior must stay identical to Module 4 (including file read/write).
"""

import os

LOG_FILE = "ending.txt"

SCENES = [
    {
        "text": "TODO: Opening scene.",
        "choices": {"1": 1, "2": 2},
    },
    {
        "text": "TODO: Path A.",
        "ending": "TODO: Ending A",
    },
    {
        "text": "TODO: Path B.",
        "ending": "TODO: Ending B",
    },
]


def show_previous_ending():
    # TODO: same read-back behavior as Module 4
    if os.path.exists(LOG_FILE):
        pass


def show_scene(scene):
    """Display scene text and numbered choices."""
    # TODO: Print scene text and choice labels
    pass


def get_choice(valid_options):
    """Prompt until the player enters one of valid_options."""
    # TODO: validation loop; return the choice
    pass


def main():
    show_previous_ending()

    print("TODO: Your Game Title")
    name = input("What's your name? ")
    print(f"Welcome, {name}!")

    scene_index = 0
    while True:
        scene = SCENES[scene_index]
        show_scene(scene)

        if "ending" in scene:
            print(f"\n=== THE END: {scene['ending']} ===")
            with open(LOG_FILE, "w") as f:
                f.write(f"{name} reached ending: {scene['ending']}\n")
            break

        choice = get_choice(list(scene["choices"].keys()))
        scene_index = scene["choices"][choice]


if __name__ == "__main__":
    main()
