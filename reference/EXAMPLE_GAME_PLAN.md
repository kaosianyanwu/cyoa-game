# 📖 Example Game Plan: Mall Run

> **Reference only** — see what a filled-out plan looks like. Yours goes in [`GAME_PLAN.md`](../GAME_PLAN.md) at the repo root.

## Premise
The mall closes in an hour and you've got $60 to spend. Shoe store or clothing store first — what you buy (or don't) decides how you walk out.

## Main Character
- Player name via `input()` in Module 1 — used in scene text as `{name}`

## Stat Tracked (Module 7)
- `budget` — starts at 60. Purchases subtract cost. Simple on purpose.

## Scene List
1. **start** — Entrance. Shoe store or clothing store.
2. **shoe_store** — Sneakers $50. Buy or skip to clothing store.
3. **buy_sneakers** — budget −50 → ending **"New Kicks"**
4. **clothing_store** — Jacket $40. Buy or leave.
5. **buy_jacket** — budget −40 → ending **"Bundle Deal"**
6. **leave_empty_handed** → ending **"Saved It"**

## Endings
1. **New Kicks** — bought sneakers
2. **Bundle Deal** — skipped sneakers, bought jacket
3. **Saved It** — bought nothing, kept $60

## Notes to self
- [ ]
- [ ]
