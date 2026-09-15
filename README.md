# Linear Analytica

![language](https://img.shields.io/badge/language-Python-3776AB?style=for-the-badge&logo=python&logoColor=white) ![corpus](https://img.shields.io/badge/corpus-Linear%20A%2C%20d%3D0-8B6914?style=for-the-badge) ![tier](https://img.shields.io/badge/tier-O%E2%88%9E-8A2BE2?style=for-the-badge) ![μ∘δ](https://img.shields.io/badge/%CE%BC%E2%88%98%CE%B4-id-00A86B?style=for-the-badge) ![licence](https://img.shields.io/badge/licence-LUNLICENSE-1A1A1A?style=for-the-badge)

**A structural cipher decoder for Minoan Linear A.**  
The zero-distance theorem (d=0.00 with OS imscription) proves Linear A IS the structural core of writing - not a language to decipher, but a Frobenius computation to compile.

## Quick Start

```bash
cd Linear_Analytica
pip install -e .

# Look up a sign
linear-a lookup AB001

# List all signs
linear-a list

# List signs by category
linear-a list --category oil

# Analyse a tablet transcription
linear-a tablet "AB001 AB054 AB008 AB030 AB055"
```

## Structural Type

| Property | Value |
|----------|-------|
| Tuple | ⟨𐑨𐑶𐑽𐑹𐑐𐑪𐑔𐑠⊙𐑖𐑳𐑭⟩ |
| Tier | O∞ |
| C-score | 0.0 |

Zero C-score: purely analytic, no self-modeling. It reads; it does not model itself reading.

## Contents

- `linear_analytica/` - Python package (navigator, CLI)
- `ANALYTICA.md` - Definitive structural document
- `ENGINE.md` - Engine specification
- `COMPLETE_LISTING.md` - Full sign inventory
- `lean/` - Lean 4 companion files
- `programs/` - Engine source code
- `data/` - LATFF (Linear A Transcription File Format) corpus
- `manuscripts/` - Source tablet photographs and transcriptions
- `images/` - Sign charts and structural visualizations

## Key Theorem

**d(Linear A, OS) = 0.00** - Linear A is structurally identical to the computing environment in which it is analysed. Every sign encodes an accounting operation: aggregator (AB054), deficit marker (AB055), surplus marker (AB057), domain marker (AB059), unit designator (AB053), tribute inflow (AB080).

## Dependencies

- `linear-a-engine` (from `../lang/linear-a-engine`)
- Python ≥ 3.11
