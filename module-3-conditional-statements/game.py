"""
Module 3: Conditional Statements

COPY FIRST: paste your finished Module 2 game.py here, then add this module's work.
Replace the hardcoded ending with two choices and if/elif branches.
"""


def main():
   power = input("Do you want Superstrength or Invisibility? ").strip().lower()

if power == "superstrength":
    print("You have now gained Superstrength")
elif power == "invisibility":
    print("You have now gained Invisibility")
else:
    print("You have not chosen a valid power, you remain normal.")

if __name__ == "__main__":
    main()
