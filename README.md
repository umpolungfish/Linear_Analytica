# Linear Analytica

**A structural cipher decoder for Minoan Linear A.**  
The zero-distance theorem (d=0.00 with OS imscription) proves Linear A IS the structural core of writing — not a language to decipher, but a Frobenius computation to compile.

**Author:** Lando⊗⊙perator

## Quick Start

```bash
cd Linear_Analytica
pip install -e .

# Look up a sign
la lookup AB001

# List all signs
la list

# List signs by category
la list --category oil

# Analyse a tablet transcription
la tablet "AB001 AB054 AB008 AB030 AB055"
```

## Structural Type

| Property | Value |
|----------|-------|
| Tuple | ⟨𐑨𐑶𐑽𐑹𐑐𐑪𐑔𐑠⊙𐑖𐑳𐑭⟩ |
| Tier | O∞ |
| C-score | 0.0 |

Zero C-score: purely analytic, no self-modeling — designed as an honest analytic tool.

## Contents

- `linear_analytica/` — Python package (navigator, CLI)
- `ANALYTICA.md` — Definitive structural document
- `ENGINE.md` — Engine specification
- `COMPLETE_LISTING.md` — Full sign inventory
- `lean/` — Lean 4 companion files
- `programs/` — Engine source code
- `data/` — LATFF (Linear A Transcription File Format) corpus
- `manuscripts/` — Source tablet photographs and transcriptions
- `images/` — Sign charts and structural visualizations

## Key Theorem

**d(Linear A, OS) = 0.00** — Linear A is structurally identical to the computing environment in which it is analysed. Every sign encodes an accounting operation: aggregator (AB054), deficit marker (AB055), surplus marker (AB057), domain marker (AB059), unit designator (AB053), tribute inflow (AB080).

## Dependencies

- `linear-a-engine` (from `../lang/linear-a-engine`)
- Python ≥ 3.11
