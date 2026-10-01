# Multi-Exposure Modelling of Information Spread

**Course:** MATH 4090 (York University) · **Author:** Lavanya Kumar  
**Stack:** Python (NumPy, SciPy, Matplotlib) · LaTeX

ODE compartment model of how a social-media post spreads when users may need **repeated exposures** before reposting (or may disengage without sharing). Tracks exposure classes \(I_0,\ldots,I_m\), active sharers \(S\), and saturated users \(R\), with mean-field exposure rate \(\lambda = \beta S / N\).

## What’s here

| File | Role |
|------|------|
| `simulate_instagram_ode.py` | Simulations + figure generation (viral / moderate / fizzle regimes, sensitivity) |
| `final_project.tex` | Final write-up (theory, stability, computation, discussion) |
| `report.tex` / `proposal_revised.tex` | Progress report & revised proposal |
| `presentation.tex` + `*.pptx` / speaker notes | Presentation materials |
| `fig_*.pdf` | Simulation figures used in the paper |

Peer-review videos and transcripts were **excluded** from this public package.

## Reproduce simulations

```bash
python3 -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install numpy scipy matplotlib
python simulate_instagram_ode.py
```

Figures are written as PDFs in the project folder.

## Compile the paper (optional)

```bash
pdflatex final_project.tex
```

## Key questions

1. When does reposting amplify from a small seed of sharers?
2. How do \(\beta\) (repost intensity) and \(\gamma\) (attention decay) affect peak sharers and reach?
3. Can the same equations represent viral vs. slower content?

## License / academic use

Coursework packaged for portfolio demonstration. Cite as student work for MATH 4090 unless otherwise noted.
