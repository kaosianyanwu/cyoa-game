"""
Module 6: User-Defined Functions (Part 2)

COPY FIRST: paste your finished Module 5 game.py here, then refactor further.
main() should be short; each function one job. Same behavior as Module 5.
"""

import os

LOG_FILE = "ending.txt"

SCENES = [
    {
        "text": "TODO: Opening scene.",
        "choices": {
            "1": ("TODO: First choice label", 1),
            "2": ("TODO: Second choice label", 2),
        },
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
    # TODO: same read-back behavior as Module 4/5
    if os.path.exists(LOG_FILE):
        pass


def show_scene(scene):
    """Display scene text and numbered choice labels."""
    pass


def get_choice(valid_options):
    """Prompt until the player enters a valid option key."""
    pass


def write_ending(name, ending_title):
    """Write the player's ending to LOG_FILE."""
    pass


def play_turn(scene_index, name):
    """Show one scene. Return (next_index, done) where done=True if story ended."""
    pass


def run_game(name):
    """Main game loop for one player."""
    pass


def main():
    show_previous_ending()
    print("TODO: Your Game Title")
    name = input("What's your name? ")
    print(f"Welcome, {name}!")
    run_game(name)


if __name__ == "__main__":
    main()
