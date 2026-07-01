"""
Module 5: User-Defined Functions (Part 1)
Build on Module 4 — extract show_scene() and get_choice().
"""

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


def show_scene(scene):
    """Display scene text and numbered choices."""
    # TODO: Print scene text
    # TODO: If scene has "choices", print each option (you may use placeholder labels)
    pass


def get_choice(valid_options):
    """Prompt until the player enters one of valid_options."""
    # TODO: Loop with input() until choice is in valid_options; return the choice
    pass


def main():
    print("TODO: Your Game Title")
    name = input("What's your name? ")
    print(f"Welcome, {name}!")

    scene_index = 0
    while True:
        scene = SCENES[scene_index]

        # TODO: Call show_scene(scene) instead of inline prints
        show_scene(scene)

        if "ending" in scene:
            print(f"\n=== THE END: {scene['ending']} ===")
            with open(LOG_FILE, "w") as f:
                f.write(f"{name} reached ending: {scene['ending']}\n")
            break

        # TODO: Call get_choice(...) with the scene's valid choice keys
        choice = get_choice(list(scene["choices"].keys()))
        scene_index = scene["choices"][choice]


if __name__ == "__main__":
    main()
