"""
Module 3: Conditional Statements

COPY FIRST: paste your finished Module 2 game.py here, then add this module's work.
Keep title, name, greeting, and scene variable. Replace the hardcoded ending
with two choices and if/elif branches.
"""


def main():
    # TODO: Print your game title
    print("TODO: Your Game Title")

    name = input("What's your name? ")
    print(f"Welcome, {name}!")

    # TODO: Keep your scene in a variable (from Module 2)
    scene_text = "TODO: Describe your opening scene here."
    print(scene_text)

    # TODO: Show two choice options (replace Module 2's hardcoded ending)
    print("  1) TODO: First choice")
    print("  2) TODO: Second choice")

    choice = input("> ").strip()

    # TODO: Use if/elif to show different outcome text for each choice
    if choice == "1":
        print("TODO: Outcome when player picks choice 1")
    elif choice == "2":
        print("TODO: Outcome when player picks choice 2")
    else:
        print("That's not a valid choice.")


if __name__ == "__main__":
    main()
