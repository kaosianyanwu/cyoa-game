"""
Module 4: Sequences, Loops, and File I/O

COPY FIRST: paste your finished Module 3 game.py here, then refactor into this shape.
Add SCENES list, while loop, file write, and read-back on the next run.
"""

LOG_FILE = "ending.txt"

# TODO: your scenes as a list of dicts (text, choices, and/or ending)
SCENES = []


def show_previous_ending():
    """If LOG_FILE exists, read and print it."""
    # TODO: implement
    pass


def main():
    print("Solo Leveling")

    name = input("What is players name?")
    print( "welcome", name, "to Solo Leveling")

    scene= input("Write scene of your choice :")
    print(scene)
    print("And you notice youre in a new dimension and you have powers")

    power = input("Do you want Super strength or Invisibility?").strip().lower()
    if power == "super strength":
       print("You have now gained Super strength")
    elif power == "invisibility":
       print("You have now gained Invisibility")
    else:
       print("You have not chosen a valid power, you remain normal.")
    scene =[ "You decide to go explore the new universe",
          "And you notice this new world goes against everything you know", 
          "In this new world mythical creatures exist",
          "You watch two fairies zoom past you"]
    scene_number = 0
    while scene_number < len(scene) :      
        print(scene[scene_number] )
        scene_number= scene_number + 1
    ending = "You gasped, eyes wide!"
    with open("ending.txt", "w") as file: 
        file.write(ending) 

    with open("ending.txt", "r") as file:
        saved_ending = file.read() 
        print("ending:", saved_ending)

if __name__ == "__main__":
    main()
