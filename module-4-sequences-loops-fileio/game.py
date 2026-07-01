"""
Module 4: Sequences, Loops, and File I/O

COPY FIRST: paste your finished Module 3 game.py here, then refactor into this shape.
Turn your scenes into SCENES list + while loop. Add file write AND read-back
(show the previous run's ending when the game starts — practice for file I/O).
"""

import os

LOG_FILE = "ending.txt"


def show_previous_ending():
    """If LOG_FILE exists, read it and print it for the player."""
    # TODO: open LOG_FILE for reading and print its contents
    if os.path.exists(LOG_FILE):
        pass


# TODO: Move your story into this list (opening scene + paths to endings)
SCENES = [
    {
        "text": "TODO: Opening scene.",
        "choices": {"1": 1, "2": 2},
    },
    {
        "text": "TODO: Path A — leads to an ending.",
        "ending": "TODO: Ending A",
    },
    {
        "text": "TODO: Path B — leads to an ending.",
        "ending": "TODO: Ending B",
    },
]


def main():
    show_previous_ending()

    print("TODO: Your Game Title")
    name = input("What's your name? ")
    print(f"Welcome, {name}!")

    scene_index = 0
    while True:
        scene = SCENES[scene_index]
        print("\n" + scene["text"])

        if "ending" in scene:
            print(f"\n=== THE END: {scene['ending']} ===")
            with open(LOG_FILE, "w") as f:
                f.write(f"{name} reached ending: {scene['ending']}\n")
            break

        for key in scene["choices"]:
            print(f"  {key}) ...")  # TODO: use your choice labels
        choice = input("> ").strip()
        while choice not in scene["choices"]:
            choice = input("Please choose a valid option: ").strip()
        scene_index = scene["choices"][choice]


if __name__ == "__main__":
    main()
