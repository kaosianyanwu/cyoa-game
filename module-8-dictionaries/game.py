"""
Module 8: Dictionaries
Build on Module 7 — story as STORY dict keyed by scene id.
"""

LOG_FILE = "ending.txt"
STAT_NAME = "budget"
STARTING_STAT = 60

# TODO: Fill in your scenes from GAME_PLAN.md
# Each scene: "text", optional "choices" {key: (label, next_id)}, optional "ending", optional "stat_effect"
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
    # TODO: print text formatted with player.name and player stats
    pass


def get_choice(valid_options):
    pass


def apply_stat_effect(scene, stats):
    pass


def play(player):
    """Main loop — advance player.current_scene through STORY."""
    # TODO: while True — lookup STORY[player.current_scene], handle ending, choices
    pass


def main():
    print("TODO: Your Game Title")
    name = input("What's your name? ")
    # TODO: bundle name + current_scene + stats (dict or simple namespace) and call play()
    pass


if __name__ == "__main__":
    main()
