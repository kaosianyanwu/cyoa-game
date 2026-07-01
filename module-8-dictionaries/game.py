"""
Module 8: Dictionaries

COPY FIRST: paste your finished Module 7 game.py here, then convert SCENES
to a STORY dictionary keyed by scene id. Game logic stays the same — story
becomes data you can extend without new elif branches.
"""

STAT_NAME = "budget"
STARTING_STAT = 60

# TODO: Port your scenes from GAME_PLAN.md — add scenes by editing this dict only
STORY = {
    "start": {
        "text": "TODO: Opening scene for {name}. Budget: ${budget}.",
        "choices": {
            "1": ("TODO: First choice", "path_a"),
            "2": ("TODO: Second choice", "path_b"),
        },
    },
    "path_a": {
        "text": "TODO: Path A.",
        "stat_effect": -20,
        "ending": "TODO: Ending A",
    },
    "path_b": {
        "text": "TODO: Path B.",
        "ending": "TODO: Ending B",
    },
}


def show_scene(scene, player):
    pass


def get_choice(valid_options):
    pass


def apply_stat_effect(scene, stats):
    pass


def play(player):
    """Main loop — advance player.current_scene through STORY."""
    # TODO: while True — scene = STORY[player.current_scene], ...
    pass


def main():
    print("TODO: Your Game Title")
    name = input("What's your name? ")
    # TODO: build a player object (name, current_scene="start", stats) and call play()
    pass


if __name__ == "__main__":
    main()
