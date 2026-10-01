# Presentation Notes

## Timing

- Aim for about 1 minute per slide.
- Total target: 12 to 14 minutes, leaving time for questions.

## Slide-by-slide notes

### 1. Title

Say that the project studies how reposted content spreads on social media when repeated exposure matters.

### 2. Roadmap

Tell the audience you will cover background, the model, key math, results, and what remains for the final report.

### 3. Topic and motivation

Explain in simple words:

- people do not always repost after seeing content once,
- some need repeated exposure,
- some lose interest,
- so a multi-exposure model is more realistic than a one-step model.

### 4. Background and existing modelling

Say that rumor models and epidemic-style models already exist, and threshold models also exist, but your project combines these ideas in a simpler ODE framework with repeated exposure classes.

### 5. Compartments

Stress the difference between:

- equilibrium setup: $I_0=N$ and everything else is zero,
- simulation setup: start with a small seed of sharers, so $S(0)>0$.

This is one of the professor's key comments, so make it very clear.

### 6. Movement between classes

Say:

- $\beta$ controls how strongly sharers expose others,
- $\rho_i$ means probability of sharing after exposure level $i$,
- $\sigma_i$ means probability of dropping out after exposure level $i$,
- $\gamma$ means sharers stop sharing over time.

Also mention the condition $\rho_i+\sigma_i \le 1$, because the leftover part is the probability of moving forward to the next exposure class.

### 7. Key equations

Spend extra time here.

Explain the step from $I_0$ to $I_1$:

- users leave $I_0$ when they are exposed,
- if they do not share and do not saturate, they move to $I_1$,
- this is why the inflow into $I_1$ is $(1-\rho_0-\sigma_0)\lambda I_0$.

### 8. Variables and parameters

Show that the table now clearly includes $\rho_i$ and $\sigma_i$, what they mean, and where they appear in the equations.

### 9. Equilibria

Define the two main equilibria clearly:

- no spread,
- burned out.

Then say that the next step is to study local stability using the Jacobian.

### 10. Jacobian

Keep this simple:

- first identify the equilibrium,
- then compute the Jacobian,
- then look at the eigenvalues.

Main point: the sign of $\rho_0\beta-\gamma$ affects whether small sharing initially grows or shrinks.

### 11. Why Jacobian is not enough

Say that the Jacobian only tells us local behaviour near the disease-free equilibrium.

Because the model has repeated exposure classes, nonlinear behaviour matters, so simulations are also needed.

### 12. Simulation setup

Briefly explain the three scenarios:

- viral,
- moderate,
- fizzle.

### 13. Numerical results

Say:

- viral has the largest and fastest outbreak,
- moderate spreads but less strongly,
- fizzle stays near the initial seed.

### 14. Figure comparison

Walk the audience through the graph from highest curve to lowest curve.

### 15. Exposure class figure

Explain that the figure helps visualize the path users take through the model.

### 16. Parameter effects

Say in plain language:

- bigger $\rho_i$ helps spread,
- bigger $\sigma_i$ stops spread,
- bigger $\gamma$ makes sharers disappear faster.

### 17. Remaining work

Be honest and concise:

- stability discussion still needs polishing,
- sensitivity analysis can be expanded,
- figure discussion and report presentation can be improved.

### 18. Q&A

Pause and invite questions.

## Likely questions and short answers

### Why not just use an SIR model?

Because SIR does not track how many times someone has seen the content. My model keeps that repeated-exposure effect.

### Why is $I_0=N$ at equilibrium but not in simulations?

At equilibrium, I am describing the exact no-spread resting state. In simulations, I intentionally add a small seed of sharers to test whether spread begins.

### What do $\rho_i$ and $\sigma_i$ mean in real life?

$\rho_i$ is the chance someone reposts after that exposure level, and $\sigma_i$ is the chance they lose interest and stop engaging.

### What is the main limitation of the model?

It assumes homogeneous mixing, so it does not include a real follower network.

### What is the main conclusion?

Repeated exposure matters, and the balance between visibility, sharing probability, saturation, and sharer decay determines whether content goes viral or dies out.
