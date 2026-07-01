"""
Module 6: User-Defined Functions (Part 2)
Build on Module 5 — complete refactor; main() reads like an outline.
"""

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


def show_scene(scene):
    """Display scene text and numbered choice labels."""
    # TODO: Print scene["text"]
    # TODO: For each choice key, print f"  {key}) {label}" from scene["choices"]
    pass


def get_choice(valid_options):
    """Prompt until the player enters a valid option key."""
    # TODO: implement validation loop
    pass


def write_ending(name, ending_title):
    """Write the player's ending to LOG_FILE."""
    # TODO: open LOG_FILE and write name + ending
    pass


def play_turn(scene_index, name):
    """
    Show one scene. Return (next_index, done) where done=True if story ended.
    """
    # TODO: show scene, handle ending (call write_ending), or get choice and return next index
    pass


def run_game(name):
    """Main game loop for one player."""
    # TODO: while loop using play_turn until done
    pass


def main():
    print("TODO: Your Game Title")
    name = input("What's your name? ")
    print(f"Welcome, {name}!")
    # TODO: Call run_game(name)
    pass


if __name__ == "__main__":
    main()
