"""
Module 3: Conditional Statements

COPY FIRST: paste your finished Module 2 game.py here, then add this module's work.
Replace the hardcoded ending with two choices and if/elif branches.
"""


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

if __name__ == "__main__":
    main()
