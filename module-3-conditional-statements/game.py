"""
Module 3: Conditional Statements
Build on Module 2 — branch on the player's first choice with if/elif.
"""


def main():
    # TODO: Print your game title
    print("TODO: Your Game Title")

    # TODO: Ask for name and greet the player
    name = input("What's your name? ")
    print(f"Welcome, {name}!")

    # TODO: Show opening scene text
    print("TODO: Opening scene description.")

    # TODO: Show two choice options
    print("  1) TODO: First choice")
    print("  2) TODO: Second choice")

    # TODO: Ask the player to pick 1 or 2
    choice = input("> ").strip()

    # TODO: Use if/elif to show different follow-up text for each choice
    if choice == "1":
        print("TODO: Outcome when player picks choice 1")
    elif choice == "2":
        print("TODO: Outcome when player picks choice 2")
    else:
        print("That's not a valid choice.")


if __name__ == "__main__":
    main()
