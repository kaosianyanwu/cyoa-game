"""
Mall Run — REFERENCE EXAMPLE ONLY (see EXAMPLE_GAME_PLAN.md)
This shows what a *finished* CYOA game looks like once you've reached
Module 8 (dictionaries) and Module 9 (classes + save/load).
Read it, run it, play with it — but your own game should be written by
YOU, in your own module folders, one concept at a time. Don't copy this
in. The point is to see the shape of where you're headed.
"""

import json
import os

SAVE_FILE = "save.json"

# --- The whole story lives as data (Module 8 concept) -----------------
# Each scene has: text, and either "choices" (a dict of option -> next
# scene id) or "ending" (a string, meaning the story stops here).
STORY = {
    "start": {
        "text": "The mall closes in an hour. {name} has $60 to spend "
                "and two stores in mind.",
        "choices": {
            "1": ("Check out the shoe store", "shoe_store"),
            "2": ("Check out the clothing store", "clothing_store"),
        },
    },
    "shoe_store": {
        "text": "There's a pair of sneakers on sale for $50.",
        "choices": {
            "1": ("Buy the sneakers", "buy_sneakers"),
            "2": ("Skip it, check the clothing store instead", "clothing_store"),
        },
    },
    "buy_sneakers": {
        "text": "{name} walks out with a brand new pair of sneakers.",
        "stat_effect": ("budget", -50),
        "ending": "New Kicks",
    },
    "clothing_store": {
        "text": "There's a jacket here for $40.",
        "choices": {
            "1": ("Buy the jacket", "buy_jacket"),
            "2": ("Skip it, head home", "leave_empty_handed"),
        },
    },
    "buy_jacket": {
        "text": "{name} grabs the jacket on the way out.",
        "stat_effect": ("budget", -40),
        "ending": "Bundle Deal",
    },
    "leave_empty_handed": {
        "text": "{name} decides nothing's worth it today and heads home "
                "with the full $60 still in their pocket.",
        "ending": "Saved It",
    },
}


class Player:
    """Module 9 concept: bundle player state into a class instead of
    loose variables, so it's easy to save/load as one object."""

    def __init__(self, name):
        self.name = name
        self.current_scene = "start"
        self.stats = {"budget": 60}

    def to_dict(self):
        return {
            "name": self.name,
            "current_scene": self.current_scene,
            "stats": self.stats,
        }

    @classmethod
    def from_dict(cls, data):
        player = cls(data["name"])
        player.current_scene = data["current_scene"]
        player.stats = data["stats"]
        return player


def save_game(player):
    with open(SAVE_FILE, "w") as f:
        json.dump(player.to_dict(), f)
    print("\n[Game saved. Come back anytime with the same name to resume.]")


def load_game():
    if not os.path.exists(SAVE_FILE):
        return None
    with open(SAVE_FILE, "r") as f:
        return Player.from_dict(json.load(f))


def play(player):
    while True:
        scene_id = player.current_scene
        scene = STORY[scene_id]

        print("\n" + scene["text"].format(name=player.name))

        if "stat_effect" in scene:
            stat_name, amount = scene["stat_effect"]
            player.stats[stat_name] = player.stats.get(stat_name, 0) + amount

        if "ending" in scene:
            print(f"\n=== THE END: {scene['ending']} ===")
            print(f"Budget remaining: ${player.stats['budget']}")
            if os.path.exists(SAVE_FILE):
                os.remove(SAVE_FILE)
            return

        choices = scene["choices"]
        for key, (label, _) in choices.items():
            print(f"  {key}) {label}")

        choice = input("> ").strip()
        while choice not in choices:
            choice = input("Please choose a valid option: ").strip()

        _, next_scene = choices[choice]
        player.current_scene = next_scene

        # Save after every choice so quitting mid-story is safe.
        save_game(player)


def main():
    print("=== Mall Run (reference example) ===\n")
    existing = load_game()

    if existing:
        resume = input(
            f"Found a saved game for '{existing.name}'. Resume? (y/n) "
        ).strip().lower()
        if resume == "y":
            play(existing)
            return

    name = input("What's your name? ").strip()
    play(Player(name))


if __name__ == "__main__":
    main()
