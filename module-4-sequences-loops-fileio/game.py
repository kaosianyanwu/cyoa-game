"""
Module 4: Sequences, Loops, and File I/O
Build on Module 3 — list of scenes, while loop, write ending to file.
"""

LOG_FILE = "ending.txt"

# TODO: Define a list of scenes. Each scene can be a dict with keys like:
#   "text", "choices" (dict mapping "1"/"2" to next scene index), and optionally "ending"
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
    # TODO: Print title and ask for name
    print("TODO: Your Game Title")
    name = input("What's your name? ")
    print(f"Welcome, {name}!")

    # TODO: Use a while loop — track current scene index, stop when scene has "ending"
    scene_index = 0
    while True:
        scene = SCENES[scene_index]
        print("\n" + scene["text"])

        if "ending" in scene:
            print(f"\n=== THE END: {scene['ending']} ===")
            # TODO: Write the ending to LOG_FILE (include player name and ending title)
            with open(LOG_FILE, "w") as f:
                f.write(f"{name} reached ending: {scene['ending']}\n")
            break

        # TODO: Show choices and ask for input; update scene_index from scene["choices"]
        for key in scene["choices"]:
            print(f"  {key}) ...")
        choice = input("> ").strip()
        while choice not in scene["choices"]:
            choice = input("Please choose a valid option: ").strip()
        scene_index = scene["choices"][choice]


if __name__ == "__main__":
    main()
