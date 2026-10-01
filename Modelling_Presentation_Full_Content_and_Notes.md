# Modelling the Spread of Information Through Social Media  
**Full slide copy + speaker notes** (13 slides)  
*Lavanya Kumar — MATH 4090*

Use **“On slide”** for what appears in PowerPoint. Use **“Speaker notes”** in Presenter View or as your script. Figures for slides 9–11 match `presentation_assets/` after running `python3 simulate_instagram_ode.py` or `python3 create_outline_deck.py`.

---

## Slide 1 — Title

### On slide
- **Title:** Modelling the Spread of Information Through Social Media  
- **Name:** Lavanya Kumar  
- **Course:** MATH 4090  
- **Subtitle / tagline:** ODE model for repost spread with repeated exposure  

### Speaker notes
Welcome everyone. My name is Lavanya Kumar, and this presentation is for MATH 4090.

The title is *Modelling the Spread of Information Through Social Media*. In one sentence, the project builds a system of ordinary differential equations — an ODE model — for how a single piece of content spreads when people repost it, and when seeing the post multiple times can matter before someone either reposts or loses interest.

I will walk through why that matters, how the model is set up with compartments and parameters, the main equations for the case with two exposure levels beyond “not exposed,” then show simulation results for three scenarios — viral, moderate, and fizzle — and end with future work and conclusions.

If you have questions, I am happy to take them at the end.

---

## Slide 2 — The question (why this model?)

### On slide
- Content gains visibility through **reposting**; users often see the **same post more than once** before reposting or losing interest.  
- **Goal:** a tractable ODE framework with explicit **exposure classes** \(I_0, I_1, \ldots, I_m\) that record **how many times** someone has been exposed.  
- **Why not a single “exposed / not exposed” split?** That would hide **reinforcement** from repeated views.  

### Speaker notes
On social platforms, content does not only spread because someone sees it once. Reposts put the same item back into feeds, so many users see the same post two or more times before they decide to repost it themselves or to scroll past and disengage.

Classic “epidemic style” information models often split people into a small number of types — for example, those who have not heard the rumor, those who spread it, and those who stop spreading. That is useful, but it usually does not track **how many times** someone has been exposed. The goal of this project is to keep the mathematics manageable — a tractable ODE system — while still tracking exposure count through explicit classes \(I_0, I_1\), up to \(I_m\).

So the central question is: can we write down clear rules for how people move between “seen it zero times,” “seen it once,” “seen it twice,” active reposters, and people who will not repost anymore, and then study that system with both analysis and simulations?

---

## Slide 3 — Background

### On slide
- **Epidemic / rumor models:** compartments such as spreaders, ignorants, stiflers — capture social spread and stopping, but usually **not** “1st vs 2nd exposure.”  
- **Complex contagion / thresholds:** evidence that **repeated exposure** can be needed before sharing or adopting.  
- **This project:** extend SIR-style ideas with an explicit chain \(I_0 \to I_1 \to \cdots \to I_m\) (here **\(m = 2\)**).  

### Speaker notes
This slide situates the project in existing ideas, without going into a long literature review.

First, epidemic-style and rumor models have a long history. They often use compartments like ignorants, spreaders, and stiflers — people who stop passing the information on. Those models capture that sharing is social and that interest can die out, but they typically do not reserve a separate state for “exposed twice” versus “exposed once.”

Second, there is work on complex contagion and thresholds, including experiments showing that sometimes people need repeated exposure before they adopt a behavior or share. That motivates counting exposures, not only a binary exposed or not.

This project extends SIR-style and rumor-style pictures by introducing an explicit chain: \(I_0\), then \(I_1\), then \(\ldots\) up to \(I_m\). The maximum \(m\) is the highest exposure index we track. For the rest of the talk, \(m = 2\), so we have \(I_0\), \(I_1\), and \(I_2\).

---

## Slide 4 — Compartments

### On slide
- **\(I_0\):** not yet exposed (0 exposures).  
- **\(I_1, I_2\):** exposed 1 or 2 times, **not** actively reposting.  
- **\(S\):** active sharers / reposters.  
- **\(R\):** saturated — will not repost this content further.  
- **Conservation:** \(N\) fixed, \(I_0 + I_1 + I_2 + S + R = N\).  
- **Visual:** diagram of boxes \(I_0 \to I_1 \to I_2 \to S\) and \(R\) (or chain + outcomes).  

### Speaker notes
Here is the state of the model at any time \(t\). Think of \(N\) as the size of the audience we follow — fixed over the run.

\(I_0\) counts people who have not yet been counted as exposed to this post in our model — zero exposures in the chain.

\(I_1\) and \(I_2\) count people who have been exposed once or twice but are not currently in the active reposting class. They are still “in the pipeline”: they might get another exposure, repost, or drop out.

\(S\) counts active sharers or reposters. They matter because the model assumes the rate at which other people receive new exposures depends on how many people are actively sharing — more sharing pushes more impressions into the population.

\(R\) counts saturated users: they will not repost this content further. They might have dropped out after an exposure, or they might have been sharers who stopped.

The key accounting identity is that everyone is in exactly one box: \(I_0 + I_1 + I_2 + S + R = N\). That conservation is what makes the model a closed population problem and checks that the equations are consistent.

The diagram below the bullets is the same idea visually: a chain through exposure levels, then sharing and saturation.

---

## Slide 5 — The exposure mechanism

### On slide
- New exposures arrive at mean-field rate **\(\lambda\)**.  
- From **\(I_i\)** on one exposure:  
  - repost with prob. **\(\rho_i\)** \(\to S\)  
  - saturate with prob. **\(\sigma_i\)** \(\to R\)  
  - else advance to **\(I_{i+1}\)** with prob. **\(1 - \rho_i - \sigma_i\)**  
- **Constraints:** \(0 \le \rho_i, \sigma_i \le 1\), \(\rho_i + \sigma_i \le 1\).  
- **Visual:** fork from \(I_i\) to \(S\), \(R\), \(I_{i+1}\) with probabilities.  

### Speaker notes
This slide is the core mechanism. We use a mean-field exposure rate \(\lambda\). You can think of \(\lambda\) as the per-capita intensity of “another viewing opportunity” for people still in the exposure chain, driven in this project by active sharers through a formula I give on the next slide.

When someone in class \(I_i\) receives an exposure event, three things can happen, with probabilities \(\rho_i\), \(\sigma_i\), and the remainder. With probability \(\rho_i\) they repost and move into \(S\). With probability \(\sigma_i\) they lose interest or saturate and move into \(R\). With the remaining probability \(1 - \rho_i - \sigma_i\) they do not repost and do not saturate yet, but their exposure count goes up by one, so they move to \(I_{i+1}\).

The constraints \(0 \le \rho_i, \sigma_i \le 1\) and \(\rho_i + \sigma_i \le 1\) guarantee that these three probabilities are all valid and sum to one.

The diagram shows the fork from a generic \(I_i\). For the very first exposure from \(I_0\), the same picture applies with \(i = 0\): that is how mass enters \(I_1\), \(S\), and \(R\) from the pool of people who have not yet been exposed.

When you read the differential equation for \(dI_1/dt\), the term \((1 - \rho_0 - \sigma_0)\lambda I_0\) is exactly this “continue to the next exposure class” flow.

---

## Slide 6 — Model parameters

### On slide
| Symbol | Meaning |
|--------|--------|
| \(\lambda(t) = \beta S(t)/N\) | Exposure rate driven by active sharers |
| \(\beta\) | Repost intensity — more sharing \(\Rightarrow\) more exposures |
| \(\gamma\) | Sharer decay — reposters stop being active over time |
| \(\rho_i\) | Probability of **sharing** at exposure level \(i\) |
| \(\sigma_i\) | Probability of **saturating** at exposure level \(i\) |

### Speaker notes
This table collects the symbols peers need to follow the equations.

\(\lambda(t) = \beta S(t)/N\). So the exposure rate scales with the number of active sharers \(S\). If almost nobody is sharing, \(\lambda\) is small and the exposure chain barely moves. If many people share, \(\lambda\) grows and exposures happen faster. Dividing by \(N\) is a standard mean-field scaling: we are not drawing a full social network here; we assume mixing is uniform in expectation.

\(\beta\) is the repost intensity parameter. Larger \(\beta\) means each sharer contributes more strongly to pulling others into new exposures, in this reduced description.

\(\gamma\) is the rate at which active sharers leave \(S\). They go to \(R\) when they stop reposting. So \(\gamma\) is “attention decay” or loss of sharing activity among current sharers.

\(\rho_i\) is the probability that, upon an exposure while in \(I_i\), the user reposts. \(\sigma_i\) is the probability they saturate instead. Those are the local behavioral rules at each exposure level. In simulations you can make early \(\rho\) small and later \(\rho\) larger to mimic needing reinforcement, or adjust \(\sigma\) to make drop-out more likely after several views.

Together, \(\beta\), \(\gamma\), \(\rho_i\), and \(\sigma_i\) are the levers that change whether the system behaves like a viral spike, a moderate wave, or a fizzle.

---

## Slide 7 — Governing equations (\(m = 2\))

### On slide
\[
\lambda(t) = \frac{\beta S(t)}{N}
\]
\[
\frac{dI_0}{dt} = -\lambda(t) I_0
\]
\[
\frac{dI_1}{dt} = (1-\rho_0-\sigma_0)\lambda(t) I_0 - \lambda(t) I_1
\]
\[
\frac{dI_2}{dt} = (1-\rho_1-\sigma_1)\lambda(t) I_1 - (\rho_2+\sigma_2)\lambda(t) I_2
\]
\[
\frac{dS}{dt} = \sum_{i=0}^{2} \rho_i \lambda(t) I_i - \gamma S
\]
\[
\frac{dR}{dt} = \sum_{i=0}^{2} \sigma_i \lambda(t) I_i + \gamma S
\]

**Note:** Inflow \(I_0 \to I_1\) is \((1-\rho_0-\sigma_0)\lambda I_0\) — only the **“continue”** outcome increases exposure count.

**Side panel:** One exposure from \(I_0\): \(\to S\) (\(\rho_0\)), \(\to R\) (\(\sigma_0\)), \(\to I_1\) (\(1-\rho_0-\sigma_0\)).

### Speaker notes
These are the governing ODEs for \(m = 2\).

First, \(\lambda(t) = \beta S(t)/N\) links the exposure rate to sharers.

The equation for \(I_0\) says the number of people with zero exposures decreases at rate \(\lambda I_0\): they leave \(I_0\) when they receive an exposure.

The equation for \(I_1\) has two pieces. The inflow is \((1-\rho_0-\sigma_0)\lambda I_0\) — those are the people who were in \(I_0\), got an exposure, and neither reposted nor saturated, so they advance to one exposure. The outflow is \(\lambda I_1\): people in \(I_1\) continue to receive exposures and leave \(I_1\) toward \(I_2\), \(S\), or \(R\) according to the fork.

For \(I_2\), the inflow is similar from \(I_1\), and the outflow includes both continued exposure at rate \(\lambda\) and the possibility of sharing or saturating from the last class with probabilities \(\rho_2\) and \(\sigma_2\) appearing together on the \(I_2\) term as \((\rho_2+\sigma_2)\lambda I_2\), because from the maximum exposure class another exposure forces a share or saturate outcome in this formulation.

\(S\) collects \(\rho_i \lambda I_i\) from each exposure class minus \(\gamma S\). \(R\) collects \(\sigma_i \lambda I_i\) plus the \(\gamma S\) term from sharers who stop.

The note at the bottom repeats the key story: the \(I_0\) to \(I_1\) inflow is only the “continue” outcome, not everyone who was exposed from \(I_0\).

The panel on the right restates the three-way split from \(I_0\) in words so the audience can connect the picture to the algebra.

---

## Slide 8 — Simulation setup

### On slide
- **\(N = 1000\)**, **\(m = 2\)**.  
- **Seed:** \(S(0) = 15\), \(I_0(0) = 985\), \(I_1(0) = I_2(0) = R(0) = 0\).  
- **Three scenarios** (example \((\beta, \gamma)\)):  

| Scenario | \(\beta\) | \(\gamma\) |
|----------|-----------|------------|
| Viral | 1.50 | 0.080 |
| Moderate | 1.13 | 0.089 |
| Fizzle | 0.15 | 0.600 |

- **Caption:** Viral = strong exposure, slow sharer decay; moderate = weaker \(\beta/\gamma\); fizzle = weak spread + fast decay — growth stalls near the seed.  

### Speaker notes
Numerically, I fix the population at \(N = 1000\) and the maximum exposure index \(m = 2\), matching the equations on the previous slide.

The initial condition is a small seed of active sharers: \(S(0) = 15\). Everyone else is still in \(I_0\), so \(I_0(0) = 985\), and \(I_1\), \(I_2\), and \(R\) start at zero. That is a standard way to ask whether a small amount of sharing can ignite a larger cascade.

The table gives \(\beta\) and \(\gamma\) for three labeled scenarios. Viral uses a relatively high \(\beta\) and low \(\gamma\): strong repost-driven exposure and slow decay of sharers. Moderate uses the same sharing and saturation probabilities \(\rho\) and \(\sigma\) as viral in my runs, but a weaker \(\beta\) to \(\gamma\) balance, so the outbreak is smaller and slower. Fizzle uses low \(\beta\) and high \(\gamma\), and also different \(\rho\) and \(\sigma\) that make drop-out more likely, so the system barely leaves the neighborhood of the initial seed.

You should read the table as illustrating three qualitatively different outcomes from the same model structure, not as calibrated real-world Instagram parameters.

---

## Slide 9 — Active sharers over time

### On slide
- **Figure:** Line chart — **\(S(t)\)** for viral, moderate, fizzle (legend).  
- **Caption:** Active reposters over time. Viral: fast, tall peak. Moderate: smaller, slower cascade. Fizzle: \(S(t)\) stays near the initial seed — no sustained outbreak.  

### Speaker notes
This figure plots active reposters \(S(t)\) for the three scenarios on one set of axes.

The viral curve rises to a large peak: many users are actively sharing at once before the event burns down. The moderate curve peaks lower and typically later: spread still happens, but the reposting layer is thinner or slower to build. The fizzle curve stays essentially flat near the initial fifteen: there is no sustained amplification — the seed does not trigger a self-reinforcing wave in this parameter regime.

In terms of the model, the difference is not mysterious: it comes from how strongly \(\lambda\) is fed by \(S\) through \(\beta\), how fast \(S\) drains through \(\gamma\), and how \(\rho\) and \(\sigma\) move people into \(S\) versus \(R\) versus further exposure classes.

For peers grading clarity, the message is: **one model, three different qualitative shapes**, controlled by interpretable parameters.

---

## Slide 10 — Viral compartment dynamics

### On slide
- **Figure:** Multi-line chart — \(I_0, I_1, I_2, S, R\) vs time (**viral** parameters only).  
- **Caption:** Mass moves \(I_0 \to I_1 \to I_2\) and into \(S\) and \(R\); supports the **exposure chain** vs a single exposed/unexposed split.  

### Speaker notes
This figure shows all compartments over time for the viral parameter set only.

Watch \(I_0\) decline as people leave the never-exposed pool. \(I_1\) and \(I_2\) rise and then fall as exposure moves through the chain. \(S\) rises to a peak then falls as reposters decay and the pool of people still available to enter \(S\) shrinks. \(R\) grows monotonically in this setting because it collects saturated users and former sharers.

This plot is the evidence that the “exposure chain” is doing real work. If we only had susceptible and infected, we would not see separate curves for one versus two exposures. Here the structure you saw in the compartment diagram shows up directly in the simulation.

When you present this, trace **one color at a time** so the audience does not get lost.

---

## Slide 11 — Sensitivity to \(\gamma\)

### On slide
- **Figure:** Peak \(\max_t S(t)\) vs \(\gamma\) (other parameters fixed, e.g. viral \(\rho,\sigma\) and fixed \(\beta\)).  
- **Caption:** Larger \(\gamma\) \(\Rightarrow\) reposters disengage faster \(\Rightarrow\) peak \(S\) drops; sharp transition past a threshold — sustained viral growth becomes impossible.  

### Speaker notes
This figure holds \(\rho\) and \(\sigma\) fixed at the viral-shaped values and sweeps \(\gamma\), plotting the peak value of \(S(t)\) — the maximum number of simultaneous active sharers — against \(\gamma\).

When \(\gamma\) is small, sharers stay active longer, so the outbreak can grow to a large peak. When \(\gamma\) increases, reposters disengage faster, so the peak shrinks. In this simulation there is a fairly sharp transition: beyond a certain \(\gamma\), the peak collapses to roughly the initial seed level, meaning there is no real cascade.

Interpret that in plain language: if people lose interest quickly as sharers, even strong mixing may not produce a visible viral spike. That is a useful sensitivity result to mention in discussion: \(\gamma\) is not just a technical constant; it changes the **qualitative** outcome.

If asked, you can say \(\beta\) was held fixed in this sweep so the plot isolates the role of \(\gamma\).

---

## Slide 12 — Future work

### On slide
- Complete **nonlinear / equilibrium and stability** analysis for the disease-free equilibrium \(E_0\) (Jacobian, eigenvalues, interpretation).  
- Extend **sensitivity**: grids over \(\beta\), \(\gamma\), and \(\rho_i\) (heatmaps or multiple 1D sweeps).  
- **Optional:** degree-weighted exposure or a **small network** toy model for heterogeneous influence.  

### Speaker notes
This slide is honest future work for the written final report.

First, the disease-free equilibrium and local stability can be discussed more completely in the Jacobian framework, including what the eigenvalues imply for small perturbations of \(S\) and the exposure chain. I have partial results; the write-up will be polished and made self-contained.

Second, sensitivity can be expanded beyond one-dimensional sweeps — for example grids over \(\beta\) and \(\gamma\) or over early versus late \(\rho\) values — to map regions of viral versus fizzle behavior.

Third, an optional extension is to replace strict mean-field mixing with a toy network or degree-weighted exposure so influence is not identical across users.

That list shows the core model and simulations are in place, while the report still gains depth from fuller analysis and optional extensions.

---

## Slide 13 — Conclusion

### On slide
- **Repeated exposure** is central to modelling repost-driven social contagion.  
- Outcomes depend on **\(\beta\)**, **\(\gamma\)**, and **\((\rho_i, \sigma_i)\)** — viral vs moderate vs fizzle.  
- **Questions?**  

### Speaker notes
To conclude: repeated exposure is not optional detail for social repost dynamics — this project makes it explicit through \(I_0\), \(I_1\), and \(I_2\).

The outcomes depend on the interaction of repost intensity \(\beta\), sharer decay \(\gamma\), and the local probabilities \(\rho_i\) and \(\sigma_i\) that decide whether another view leads to sharing, dropping out, or moving up the exposure ladder. The same equations can produce viral, moderate, or fizzle-like traces depending on those choices.

Thank you. I am happy to take questions.

---

## Regenerating the `.pptx` with these notes embedded

From the project folder:

```bash
python3 create_outline_deck.py
```

Ensure `create_outline_deck.py` imports `SLIDE_NOTES` from `presentation_notes_data.py` (already wired if you pulled the latest script).
