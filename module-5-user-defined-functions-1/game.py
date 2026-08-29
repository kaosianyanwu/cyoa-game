"""
Module 5: User Defined Functions (Part 1)

COPY FIRST: paste your finished Module 4 game.py here, then extract show_scene() and get_choice().
Same behavior as Module 4.
"""

LOG_FILE = "ending.txt"
SCENES = []  # TODO: carry your scenes forward from Module 4


def show_previous_ending():
    # TODO: same as Module 4
    pass


def show_scene(scene):
    """Display scene text and numbered choices."""
    # TODO: implement
    pass


def get_choice(valid_options):
    """Prompt until the player enters a valid option. Return the choice."""
    # TODO: implement
    pass


def main():
    # TODO: title, name, while loop using show_scene() and get_choice()
    pass


if __name__ == "__main__":
    main()
def show_scene(scene):
    print(scene)


def get_choice(question):
    choice = input(question)
    return choice


def main():
    print("Solo Leveling")

    name = get_choice("What is players name?")
    print("welcome", name, "to Solo Leveling")

    first_scene = get_choice("Write scene of your choice :")
    show_scene(first_scene)

    print("And you notice youre in a new dimension")

    power = get_choice("Do you want Superstrength or Invisibility?")

    if power == "Superstrength":
        print("You have now gained Superstrength")
    elif power == "Invisibility":
        print("You have now gained Invisibility")
    else:
        print("You have not chosen a valid power, you remain normal.")

    scenes = [
        "You decide to go explore the new universe",
        "And you notice this new world goes against everything you know",
        "In this new world mythical creatures exist",
        "You watch two fairies zoom past you"
    ]

    scene_number = 0

    while scene_number < len(scenes):
        show_scene(scenes[scene_number])
        scene_number = scene_number + 1

    ending = "You gasped, eyes wide!"

    with open("ending.txt", "w") as file:
        file.write(ending)

    with open("ending.txt", "r") as file:
        saved_ending = file.read()

    print("ending:", saved_ending)


main()