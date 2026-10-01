# Final Report: Modelling the Spread of Information Through Social Media Reposting

**Course:** MATH 4090  
**Author:** Lavanya Kumar — Student ID: 219148790  
**Date:** April 17, 2026  

*This report is written to match the course final-write-up expectations (clear sections, figures referenced in text, alignment with the oral presentation) and to record how presentation feedback was incorporated.*

---

## Abstract (≈200 words)

Social feeds repeatedly surface the same content before users repost or disengage. Classical rumor-style models often omit an explicit count of exposures. This project develops a closed-population ordinary differential equation (ODE) model with exposure classes \(I_0,\ldots,I_m\), active sharers \(S\), and saturated users \(R\), with mean-field exposure rate \(\lambda(t)=\beta S(t)/N\). At each exposure level, users share with probability \(\rho_i\), saturate with probability \(\sigma_i\), or advance along the exposure chain. For \(m=2\), we summarize a reproduction-style scalar \(R_{\mathrm{eff}}\), discuss the disease-free equilibrium and Jacobian structure, and present numerical simulations (viral, moderate, fizzle) together with sensitivity of peak sharing to \(\beta\) and \(\gamma\). Results show that the same equations can produce qualitatively different cascades depending on repost intensity, sharer decay, and \((\rho_i,\sigma_i)\). Limitations include mean-field mixing and illustrative parameters. Future work includes fuller stability analysis and optional network-style extensions.

---

## 1. Introduction (problem overview)

**Domain and motivation.** Platforms rank and resurface content; Meta’s public documentation describes engagement and recency as signals (Meta Platforms Inc., 2024). Reposting creates repeated impressions, so “how many times seen” is as important as “seen at all.”

**Target users / audience.** The model is aimed at analysts who want a compact dynamical description of a single campaign or post where reposts drive additional exposures.

**Objectives.** (1) Encode repeated exposure in a tractable ODE. (2) Relate parameters to qualitative regimes. (3) Connect local linear analysis to global behaviour via simulation.

---

## 2. Data and materials (what this project uses)

This project is **theory-forward**: there is no empirical dataset calibration step. **Numerical outputs** come from integrating the ODE system in Python (`simulate_instagram_ode.py`) using `scipy.integrate.odeint`, with fixed \(N=1000\), \(m=2\), seed \(S(0)=15\), and scenario tables as in the presentation.

**Figures used in this report (same as presentation):** viral vs fizzle, three-way comparison of \(S(t)\), viral compartment panel, sensitivity to \(\beta\), sensitivity to \(\gamma\) (PDFs produced by the script above).

---

## 3. Analysis questions (tasks)

1. When does a small seed of sharers amplify into a larger cascade?  
2. How do \(\beta\) (repost intensity in \(\lambda=\beta S/N\)) and \(\gamma\) (sharer decay) change peak sharing and final reach?  
3. How can one set of equations represent viral, moderate, and fizzle-like outcomes?

---

## 4. Solution and design rationale (model + visuals)

**Compartments and conservation.** \(I_i\): exposed \(i\) times, not yet sharing; \(S\): active sharers; \(R\): saturated. Conservation: \(\sum_i I_i + S + R = N\).

**Mechanism.** On exposure in \(I_i\): share with \(\rho_i\), saturate with \(\sigma_i\), else advance to \(I_{i+1}\) with probability \(1-\rho_i-\sigma_i\), with \(0\le\rho_i,\sigma_i\le 1\) and \(\rho_i+\sigma_i\le 1\). Sharers leave \(S\) at rate \(\gamma S\).

**Why these encodings.** \(\beta\) scales how strongly sharers generate new exposures; \(\gamma\) captures loss of interest among active sharers; \((\rho_i,\sigma_i)\) encode reinforcement (later \(\rho\) larger) or early dropout (larger \(\sigma_i\)).

**Figures.** Time-series plots make regime differences visible; sensitivity curves isolate one parameter at a time so the audience can connect a single knob to peak height (see **Figure 1–5** in the compiled `final_project.pdf` or slide deck).

---

## 5. Insights / findings (supported by visuals)

1. **Repeated exposure is structurally explicit** via \(I_0\to I_1\to I_2\), aligning with complex-contagion motivation (Centola, 2010).  
2. **Moderate vs viral at matched \((\rho_i,\sigma_i)\)** shows that lowering \(\beta/\gamma\) can cut the peak roughly in half while preserving the same “micro-rules” at each exposure—this is the clearest comparative static in the three-way \(S(t)\) figure.  
3. **Fizzle** corresponds to parameters where the trajectory stays near the seed: high decay and/or high dropout probabilities choke the feedback loop \(\lambda\propto S\).  
4. **Sensitivity** plots show threshold-like behaviour: beyond certain \(\beta\) or \(\gamma\) bands, peak \(S(t)\) collapses toward the initial seed level—so parameters change **qualitative** outcomes, not only scale.  
5. **Interpretation for \(\gamma\)** (as stressed in rehearsal notes): larger \(\gamma\) means sharers disengage faster, which directly suppresses the exposure engine \(\lambda=\beta S/N\).

---

## 6. Limitations and future work

**Limitations.** Mean-field mixing; no follower graph; parameters are illustrative, not fitted to platform data; Jacobian discussion at the disease-free equilibrium is local and does not replace global nonlinear analysis.

**Future work.** Fuller equilibrium classification; 2D sensitivity grids; optional small-network exposure toy; optional calibration if time-series become available.

---

## 7. Conclusion

The project contributes a transparent multi-exposure compartment model for repost-driven spread, links it to classical rumor and threshold ideas, and demonstrates viral/moderate/fizzle regimes with sensitivity analysis. The written report and slides tell the same story: local analysis motivates parameters; simulations show global cascades.

---

## 8. References

Centola, D. (2010). The spread of behavior in an online social network experiment. *Science*, 329(5996), 1194–1197.  

Daley, D. J., & Kendall, D. G. (1965). Stochastic rumours. *Journal of the Institute of Mathematics and its Applications*, 1(1), 42–55.  

Granovetter, M. (1978). Threshold models of collective behavior. *American Journal of Sociology*, 83(6), 1420–1443.  

Kempe, D., Kleinberg, J., & Tardos, É. (2003). Maximizing the spread of influence through a social network. In *Proceedings of KDD* (pp. 137–146).  

Maki, D. P., & Thompson, M. (1973). *Mathematical Models and Applications*. Prentice Hall.  

Meta Platforms Inc. (2024). How the Instagram algorithm works. Instagram Help Center. https://help.instagram.com/  

Rogers, E. M. (2003). *Diffusion of Innovations* (5th ed.). Free Press.  

**Code / reproducibility:** `simulate_instagram_ode.py` in this project folder (generate figures, then compile `final_project.tex`).

---

## 9. Presentation feedback incorporated (genuine items from rehearsal / course notes)

The following items come from your own presentation preparation files (`presentation_notes.md`, `project_presentation_speaker_notes.md`, and `Modelling_Presentation_Full_Content_and_Notes.md`), i.e. guidance you already identified as important for clarity and grading alignment:

| Feedback theme | How this report / deck addresses it |
|----------------|-------------------------------------|
| Define \(\rho_i,\sigma_i\) clearly and show where they enter the equations | Section 4 states the fork explicitly; the full write-up in `final_project.tex` includes the governing equations and parameter table. |
| Present equilibria **before** leaning on Jacobian language | `final_project.tex` orders disease-free equilibrium, absorbing equilibrium, then Jacobian at \(E_0\) (matching the requested narrative order). |
| Explain why Jacobian is **not enough** | Discussion ties local linearization to the need for simulations when \(\lambda\) couples the exposure chain nonlinearly. |
| Explain \(\gamma\) in plain language | Section 5 (insight 5): \(\gamma\) is “how fast active sharers stop,” which shrinks \(\lambda\). |
| Slow down on the scenario table | Speaker notes recommend summarizing structure rather than reading every number; figures carry the comparison. |
| Future work honesty | Section 6 mirrors slide 12 (fuller stability, richer sensitivity, optional network). |

---

## 10. Integrity, permitted resources, and attestation (project submission)

**Note:** The long exam-style pledge you pasted refers to an **exam** context (no outside resources). A **project report** may follow different rules set by your instructor. Use the paragraph below only if it matches what your syllabus actually requires.

**Suggested attestation (edit if your instructor’s wording differs):**

> I attest that this final report and associated presentation materials were prepared in accordance with the course rules stated on the assignment / syllabus. I have cited the references and tools I used (course notes where applicable, course-permitted code such as `simulate_instagram_ode.py`, and standard software such as Python/Maple/LaTeX only as permitted). I have not misrepresented sources or collaboration.  
>  
> Signature: _________________________ Date: __________

If your instructor required the **exact** exam wording for a different deliverable, attach that document only where it applies; do not confuse an exam pledge with “peer review feedback” for the presentation.

---

## 11. Alignment checklist (rubric-style quick audit)

- [ ] Title page fields match course requirements (title, course/section, name, ID).  
- [ ] Abstract 150–250 words.  
- [ ] Figures have captions and are called **Figure 1, …** in the PDF (`final_project.tex` already numbers tables/figures).  
- [ ] Written report matches what you said in the final presentation (same model, same scenarios, same figures).  
- [ ] No long code blocks in the main text (link to script / appendix).  
- [ ] References include Meta help page + primary literature + code location.

---

*End of report. To produce a PDF for upload, paste into Word/Google Docs or compile from `final_project.tex` and merge this integrity/reflection section as an appendix if your rubric asks for reflection separately.*
