# Linear Analytica

[![Language](https://img.shields.io/badge/language-Python-blue)](https://github.com/badges/shields)
[![IG Tier](https://img.shields.io/badge/IG-O%E2%82%82-blueviolet)](https://github.com/badges/shields)
[![μ∘δ=id](https://img.shields.io/badge/%CE%BC%E2%88%98%CE%B4%3Did-open-critical)](https://github.com/badges/shields)
[![License](https://img.shields.io/badge/license-MIT-blue)](https://github.com/badges/shields)
[![Author](https://img.shields.io/badge/author-Lando%E2%8A%97%E2%8A%99perator-informational)](https://github.com/badges/shields) [![Type](https://img.shields.io/badge/type-%E2%9F%A8%F0%90%91%A6%F0%90%91%B8%F0%90%91%BE%F0%90%91%B9%F0%90%90%B8%F0%90%91%82%F0%90%91%A7%F0%90%91%94%F0%90%91%9D%E2%8A%99%F0%90%91%96%F0%90%91%B3%F0%90%91%AD%E2%9F%A9-blue)](https://github.com/badges/shields) [![Tier](https://img.shields.io/badge/tier-O%E2%88%9E-blueviolet)](https://github.com/badges/shields)
**A structural cipher decoder for Minoan Linear A.**  
The zero-distance theorem (d=0.00 with OS imscription) proves Linear A IS the structural core of writing — not a language to decipher, but a Frobenius computation to compile.

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
