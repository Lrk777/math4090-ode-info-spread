# Project Presentation Speaker Notes

## Overall timing

- Aim for about 11 to 12 minutes of speaking.
- Leave the final 2 to 3 minutes for questions.
- Do not rush the equations slide; that is the slide most likely to generate questions.

## Core clarification you must say clearly

There are two different ideas that should not be mixed up:

- The disease-free equilibrium is the exact no-spread state, so `I0 = N` and all other compartments are `0`.
- The simulations do not start at that equilibrium. They start with a small seed of sharers, so `S(0) > 0` and therefore `I0(0) = N - S(0)`.

So if someone asks whether `I0` should be `N` or `0`, the correct answer is:

- `I0 = N` at the disease-free equilibrium
- `I0(0) = N - S(0)` in the simulation setup

## Slide-by-slide notes

### Slide 1: Title

Open simply: this project studies how one piece of content spreads on social media when repeated exposure matters. Mention that the presentation will cover the model, the main results, and what remains to finish for the final report.

### Slide 2: Motivation and background

Explain that on social media, seeing a post once is often not enough for someone to repost it. Some users share quickly, some need reinforcement, and some lose interest. That is the motivation for tracking exposure classes rather than using a single susceptible or ignorant compartment.

You can say that the project is related to rumor models, threshold models, and complex contagion, but your contribution is to keep the model in a simple ODE form while still allowing repeated exposure to matter.

### Slide 3: Compartments, parameters, and assumptions

Walk through the table slowly enough for the audience to see the structure of the model. Explain that `rho_i` and `sigma_i` were important comments from the professor, so you now state them clearly:

- `rho_i` is the probability of sharing after exposure level `i`
- `sigma_i` is the probability of saturating, or losing interest, after exposure level `i`

Then mention the condition `rho_i + sigma_i <= 1`, which ensures the remaining probability corresponds to moving forward in the exposure chain.

### Slide 4: Governing equations

This is the main mechanics slide. First define `lambda(t) = beta S(t)/N`. Then explain that:

- `beta` controls how strongly sharers expose others
- `gamma` controls how quickly current sharers stop being active

For the `I0` to `I1` step, use this explanation almost exactly:

`Users in I0 are exposed at rate lambda I0. If they do not share and do not saturate after that exposure, they move into I1. That is why the inflow into I1 is (1-rho0-sigma0) lambda I0.`

That phrasing is simple and mathematically correct.

### Slide 5: Equilibria and local stability

Present the disease-free equilibrium first, then the burned-out equilibrium, and only after that mention the Jacobian. This matches the order your professor wanted.

When you get to the sign discussion, say:

`There are two useful sign checks in this model. First, dI0/dt = -lambda I0 is always nonpositive, so I0 never increases. Second, dR/dt is always nonnegative, so R never decreases. For local stability near the disease-free equilibrium, the key sign is rho0 beta minus gamma.`

Then explain:

- if `rho0 beta - gamma < 0`, tiny sharing dies out initially
- if `rho0 beta - gamma > 0`, tiny sharing can grow initially

Finish by saying that this Jacobian result is local, so the simulations are needed to understand the broader nonlinear behaviour.

### Slide 6: Simulation setup and main outcomes

State the simulation setup clearly: `m = 2`, `N = 1000`, and an initial seed `S(0) = 15`. Then summarize the table rather than reading every number.

The main message is:

- the viral scenario produces the largest outbreak
- the moderate scenario spreads, but more slowly and less strongly
- the fizzle scenario stays close to the seed and does not develop into a cascade

### Slide 7: Comparison of sharer dynamics

Use the figure to tell a story. Point first to the viral curve, then the moderate curve, then the fizzle curve. Emphasize that this is the clearest summary of the project's numerical result because the three regimes are visually distinct.

### Slide 8: Exposure-class dynamics

Explain that this figure justifies the multi-exposure model itself. It shows users leaving `I0`, passing through the exposure classes, and then eventually entering either `S` or `R`. This is what a one-step model would hide.

### Slide 9: Sensitivity to gamma

Explain `gamma` in plain language: it measures how quickly current sharers lose interest and stop participating in the spread. Then use the graph to show that when `gamma` increases, the peak drops substantially. This gives a clear interpretation of one of the main parameters.

### Slide 10: What still needs to be completed

Be direct and professional here. Say that the model and the main numerical results are already complete, and the remaining work is mostly strengthening the analysis and polishing the report. That sounds honest and academically mature.

### Slide 11: Conclusion and Q&A

End with three points:

- repeated exposure matters
- the model can reproduce very different spreading regimes
- the balance among `beta`, `gamma`, `rho_i`, and `sigma_i` determines whether the post grows or dies out

Then pause and invite questions.

## Likely questions and polished answers

### Why not use a network model?

A network model would be a natural extension, but for this project I wanted a model that remains analytically tractable while still capturing repeated exposure. The ODE framework gives that balance.

### Why is `I0 = N` at equilibrium but not in the simulation?

The equilibrium describes the exact no-spread resting state. The simulation is intentionally started away from that state by introducing a small seed of sharers, so `I0(0)` must be less than `N`.

### What do `rho_i` and `sigma_i` represent in practice?

`rho_i` represents the chance that a user reposts after exposure level `i`, while `sigma_i` represents the chance that the user loses interest and stops participating after that exposure level.

### What does the Jacobian tell us?

It tells us the local behaviour near the disease-free equilibrium. In particular, it identifies the sign condition that determines whether a very small amount of sharing initially grows or dies out.

### Why are simulations still necessary if you have the Jacobian?

Because the Jacobian is only a local linear approximation. The full model includes nonlinear flow through multiple exposure classes, so simulations are needed to understand the larger cascade behaviour.
