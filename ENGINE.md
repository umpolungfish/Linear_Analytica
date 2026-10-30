# Linear Analytica — Engine Specification

## 12 IG Primitives as Script Operations

| Primitive | Value | Script Interpretation |
|-----------|-------|---------------------|
| Ð (Dimensionality) | 𐑨 (2d surface) | Linear A is inscribed on clay tablets — a writing surface |
| Þ (Topology) | 𐑶 (box product) | Signs are composed from discrete sign × syllabogram combinations |
| Ř (Coupling) | 𐑽 (adjoint pair) | Sign ↔ sound — a one-way mapping from written to spoken |
| Φ (Parity) | 𐑹 (Frobenius-special) | The script is μ∘δ=id exact: each sign has a unique referent |
| ƒ (Fidelity) | 𐑐 (quantum) | Sign values are precise — accounting requires exactness |
| Ç (Kinetics) | 𐑪 (moderate) | Script change is moderate — 1000 years of stable use |
| Γ (Cardinality) | 𑔁 (mesoscale) | ~80 signs in regular use — intermediate inventory |
| ɢ (Composition) | 𐑠 (sequential) | Signs read left-to-right in fixed sequence |
| ⊙ (Criticality) | ⊙ (self-modeling gate open) | The zero-distance theorem means Linear A models its own computation |
| Ħ (Chirality) | 𐑖 (two-step memory) | Sign sequences have bigram structure |
| Σ (Stoichiometry) | 𐑳 (many heterogeneous) | Multiple sign types combine in tablet formulae |
| Ω (Winding) | 𐑭 (integer winding) | A full tablet cycle is one complete computation |

## 12 Sign Families → IMASM Opcodes

| Sign Type | Opcode | Operation |
|-----------|--------|----------|
| Head/logogram | VINIT | Initialize account |
| Commodity | AFWD | Forward commodity record |
| Quantity | AREV | Reverse/verify quantity |
| Fraction | FSPLIT | Split into subunits |
| Total | FFUSE | Fuse line items into sum |
| Deficit | — | Mark negative balance |
| Surplus | — | Mark positive balance |
| Sacred | CLINK | Dedicate to deity |
| Tribute | IMSCRIB | Record inflow |
| Estate | EVALT | Domain assessment |
| Unit | EVALF | Measurement unit |
| King | ENGAGR | Royal authorization |

## Bootstrap Core

```
IMSCRIB → AREV → FSPLIT → AFWD → FFUSE → CLINK → IFIX → IMSCRIB
```

## Section Topology

Linear A tablets follow a ⟨𐑑⟩ categorical structure — a fixed accounting formula:

```
HEAD → COMMODITY → QUANTITY → UNIT → [FRACTION] → TOTAL → [DEFICIT/SURPLUS]
```

The brackets indicate optional elements. Every tablet is a complete Frobenius computation: each line item's δ (recording) has a μ (verification) such that μ∘δ=id.

## Transcription Format (LATFF)

```
<HEAD> <COMMODITY> <QUANTITY> <UNIT> [<FRACTION>] <TOTAL> [<SURPLUS/DEFICIT>]
```

Example: `AB001 AB054 AB008 AB030 AB055` = "Man total oil wool deficit"
