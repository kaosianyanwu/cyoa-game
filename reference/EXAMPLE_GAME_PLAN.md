# Game Plan: Mall Run
*(This is an EXAMPLE — for reference only. Your game will have its own
theme, characters, and scenes. Use this to see what a filled-out game
plan looks like before you write your own in `GAME_PLAN.md`.)*

## Premise
The mall closes in an hour and you've got $60 to spend. You start at
the entrance and decide which store to check first — the shoe store or
the clothing store. What you buy (or don't) decides how you walk out.

## Main Character
- No name assigned by the game — player is asked for their name in Module 1
  and it's used in scene text ("{name} walks into the mall...")

## Stat Tracked (introduced in Module 7)
- `budget` — starts at 60. Buying something subtracts its price. No
  branching math needed beyond that — simple and easy to follow.

## Scene List
1. **start** — At the entrance. Choice: shoe store, or clothing store.
2. **shoe_store** — Sneakers for $50. Choice: buy them, or skip and go
   check out the clothing store instead.
3. **buy_sneakers** — budget -50. → ending: "New Kicks"
4. **clothing_store** — (reached either from start, or after skipping the
   sneakers) A jacket for $40. Choice: buy it, or skip and leave.
5. **buy_jacket** — budget -40. → ending: "Bundle Deal"
6. **leave_empty_handed** → ending: "Saved It"

## Endings (3)
1. **"New Kicks"** — bought the sneakers
2. **"Bundle Deal"** — skipped the sneakers, bought the jacket instead
3. **"Saved It"** — walked out having bought nothing, kept the $60

## Notes to self
- [ ]
- [ ]
