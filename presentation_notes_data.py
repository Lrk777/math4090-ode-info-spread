# Full speaker notes for Modelling_Information_Spread_Presentation.pptx
# Used by create_outline_deck.py — regenerate deck after editing.

SLIDE_NOTES = [
    # Slide 1
    """Welcome everyone. My name is Lavanya Kumar, and this presentation is for MATH 4090.

The title is Modelling the Spread of Information Through Social Media. In one sentence, the project builds a system of ordinary differential equations — an ODE model — for how a single piece of content spreads when people repost it, and when seeing the post multiple times can matter before someone either reposts or loses interest.

I will walk through why that matters, how the model is set up with compartments and parameters, the main equations for the case with two exposure levels beyond “not exposed,” then show simulation results for three scenarios — viral, moderate, and fizzle — and end with future work and conclusions.

If you have questions, I am happy to take them at the end.""",

    # Slide 2
    """On social platforms, content does not only spread because someone sees it once. Reposts put the same item back into feeds, so many users see the same post two or more times before they decide to repost it themselves or to scroll past and disengage.

Classic “epidemic style” information models often split people into a small number of types — for example, those who have not heard the rumor, those who spread it, and those who stop spreading. That is useful, but it usually does not track how many times someone has been exposed. The goal of this project is to keep the mathematics manageable — a tractable ODE system — while still tracking exposure count through explicit classes I zero, I one, up to I m.

So the central question is: can we write down clear rules for how people move between “seen it zero times,” “seen it once,” “seen it twice,” active reposters, and people who will not repost anymore, and then study that system with both analysis and simulations?""",

    # Slide 3
    """This slide situates the project in existing ideas, without going into a long literature review.

First, epidemic-style and rumor models have a long history. They often use compartments like ignorants, spreaders, and stiflers — people who stop passing the information on. Those models capture that sharing is social and that interest can die out, but they typically do not reserve a separate state for “exposed twice” versus “exposed once.”

Second, there is work on complex contagion and thresholds, including experiments showing that sometimes people need repeated exposure before they adopt a behavior or share. That motivates counting exposures, not only a binary exposed or not.

This project extends SIR-style and rumor-style pictures by introducing an explicit chain: I zero, then I one, then dot dot dot up to I m. The maximum m is the highest exposure index we track before we force a decision on further exposure in the last class. For the slides that follow, m equals two, so we have I zero, I one, and I two.""",

    # Slide 4
    """Here is the state of the model at any time t. Think of N as the size of the audience we follow — fixed over the run.

I zero counts people who have not yet been counted as exposed to this post in our model — zero exposures in the chain.

I one and I two count people who have been exposed once or twice but are not currently in the active reposting class. They are still “in the pipeline”: they might get another exposure, repost, or drop out.

S counts active sharers or reposters. They matter because the model assumes the rate at which other people receive new exposures depends on how many people are actively sharing — more sharing pushes more impressions into the population.

R counts saturated users: they will not repost this content further. They might have dropped out after an exposure, or they might have been sharers who stopped.

The key accounting identity is that everyone is in exactly one box: I zero plus I one plus I two plus S plus R equals N. That conservation is what makes the model a closed population problem and checks that the equations are consistent.

The diagram below the bullets is the same idea visually: a chain through exposure levels, then sharing and saturation.""",

    # Slide 5
    """This slide is the core mechanism. We use a mean-field exposure rate lambda. You can think of lambda as the per-capita intensity of “another viewing opportunity” for people still in the exposure chain, driven in this project by active sharers through a formula I give on the next slide.

When someone in class I i receives an exposure event, three things can happen, with probabilities rho i, sigma i, and the remainder. With probability rho i they repost and move into S. With probability sigma i they lose interest or saturate and move into R. With the remaining probability one minus rho i minus sigma i they do not repost and do not saturate yet, but their exposure count goes up by one, so they move to I i plus one.

The constraints zero less than or equal to rho i and sigma i less than or equal to one, and rho i plus sigma i less than or equal to one, guarantee that these three probabilities are all valid and sum to one.

The diagram shows the fork from a generic I i. For the very first exposure from I zero, the same picture applies with i equals zero: that is how mass enters I one, S, and R from the pool of people who have not yet been exposed.

When you read the differential equation for d I one over d t, the term one minus rho zero minus sigma zero times lambda times I zero is exactly this “continue to the next exposure class” flow.""",

    # Slide 6
    """This table collects the symbols peers need to follow the equations.

Lambda t equals beta S t over N. So the exposure rate scales with the number of active sharers S. If almost nobody is sharing, lambda is small and the exposure chain barely moves. If many people share, lambda grows and exposures happen faster. Dividing by N is a standard mean-field scaling: we are not drawing a full social network here; we assume mixing is uniform in expectation.

Beta is the repost intensity parameter. Larger beta means each sharer contributes more strongly to pulling others into new exposures, in this reduced description.

Gamma is the rate at which active sharers leave S. They go to R when they stop reposting. So gamma is “attention decay” or loss of sharing activity among current sharers.

Rho i is the probability that, upon an exposure while in I i, the user reposts. Sigma i is the probability they saturate instead. Those are the local behavioral rules at each exposure level. In simulations you can make early rhos small and later rhos larger to mimic needing reinforcement, or adjust sigmas to make drop-out more likely after several views.

Together, beta, gamma, rho i, and sigma i are the levers that change whether the system behaves like a viral spike, a moderate wave, or a fizzle.""",

    # Slide 7
    """These are the governing ODEs for m equals two.

First, lambda t equals beta S t over N links the exposure rate to sharers.

The equation for I zero says the number of people with zero exposures decreases at rate lambda times I zero: they leave I zero when they receive an exposure.

The equation for I one has two pieces. The inflow is one minus rho zero minus sigma zero times lambda times I zero — those are the people who were in I zero, got an exposure, and neither reposted nor saturated, so they advance to one exposure. The outflow is lambda times I one: people in I one continue to receive exposures and leave I one toward I two, S, or R according to the fork.

For I two, the inflow is similar from I one, and the outflow includes both continued exposure at rate lambda and the possibility of sharing or saturating from the last class with probabilities rho two and sigma two appearing together on the I two term as rho two plus sigma two times lambda I two, because from the maximum exposure class another exposure forces a share or saturate outcome in this formulation.

S collects rho i lambda I i from each exposure class minus gamma S. R collects sigma i lambda I i plus the gamma S term from sharers who stop.

The note at the bottom repeats the key story: the I zero to I one inflow is only the “continue” outcome, not everyone who was exposed from I zero.

The panel on the right restates the three-way split from I zero in words so the audience can connect the picture to the algebra.""",

    # Slide 8
    """Numerically, I fix the population at N equals one thousand and the maximum exposure index m equals two, matching the equations on the previous slide.

The initial condition is a small seed of active sharers: S at time zero equals fifteen. Everyone else is still in I zero, so I zero at zero equals nine hundred eighty-five, and I one, I two, and R start at zero. That is a standard way to ask whether a small amount of sharing can ignite a larger cascade.

The table gives beta and gamma for three labeled scenarios. Viral uses a relatively high beta and low gamma: strong repost-driven exposure and slow decay of sharers. Moderate uses the same sharing and saturation probabilities rho and sigma as viral in my runs, but a weaker beta to gamma balance, so the outbreak is smaller and slower. Fizzle uses low beta and high gamma, and also different rho and sigma that make drop-out more likely, so the system barely leaves the neighborhood of the initial seed.

You should read the table as illustrating three qualitatively different outcomes from the same model structure, not as calibrated real-world Instagram parameters.""",

    # Slide 9
    """This figure plots active reposters S of t for the three scenarios on one set of axes.

The viral curve rises to a large peak: many users are actively sharing at once before the event burns down. The moderate curve peaks lower and typically later: spread still happens, but the reposting layer is thinner or slower to build. The fizzle curve stays essentially flat near the initial fifteen: there is no sustained amplification — the seed does not trigger a self-reinforcing wave in this parameter regime.

In terms of the model, the difference is not mysterious: it comes from how strongly lambda is fed by S through beta, how fast S drains through gamma, and how rho and sigma move people into S versus R versus further exposure classes.

For peers grading clarity, the message is: one model, three different qualitative shapes, controlled by interpretable parameters.""",

    # Slide 10
    """This figure shows all compartments over time for the viral parameter set only.

Watch I zero decline as people leave the never-exposed pool. I one and I two rise and then fall as exposure moves through the chain. S rises to a peak then falls as reposters decay and the pool of people still available to enter S shrinks. R grows monotonically in this setting because it collects saturated users and former sharers.

This plot is the evidence that the “exposure chain” is doing real work. If we only had susceptible and infected, we would not see separate curves for one versus two exposures. Here the structure you saw in the compartment diagram shows up directly in the simulation.

When you present this, trace one color at a time so the audience does not get lost.""",

    # Slide 11
    """This figure holds rho and sigma fixed at the viral-shaped values and sweeps gamma, plotting the peak value of S of t — the maximum number of simultaneous active sharers — against gamma.

When gamma is small, sharers stay active longer, so the outbreak can grow to a large peak. When gamma increases, reposters disengage faster, so the peak shrinks. In this simulation there is a fairly sharp transition: beyond a certain gamma, the peak collapses to roughly the initial seed level, meaning there is no real cascade.

Interpret that in plain language: if people lose interest quickly as sharers, even strong mixing may not produce a visible viral spike. That is a useful sensitivity result to mention in discussion: gamma is not just a technical constant; it changes the qualitative outcome.

If asked, you can say beta was held fixed in this sweep at the value stated in your code or report so the plot isolates the role of gamma.""",

    # Slide 12
    """This slide is honest future work for the written final report.

First, the disease-free equilibrium and local stability can be discussed more completely in the Jacobian framework, including what the eigenvalues imply for small perturbations of S and the exposure chain. I have partial results; the write-up will be polished and made self-contained.

Second, sensitivity can be expanded beyond one-dimensional sweeps — for example grids over beta and gamma or over early versus late rho values — to map regions of viral versus fizzle behavior.

Third, an optional extension is to replace strict mean-field mixing with a toy network or degree-weighted exposure so influence is not identical across users.

That list shows the core model and simulations are in place, while the report still gains depth from fuller analysis and optional extensions.""",

    # Slide 13
    """To conclude: repeated exposure is not optional detail for social repost dynamics — this project makes it explicit through I zero, I one, and I two.

The outcomes depend on the interaction of repost intensity beta, sharer decay gamma, and the local probabilities rho i and sigma i that decide whether another view leads to sharing, dropping out, or moving up the exposure ladder. The same equations can produce viral, moderate, or fizzle-like traces depending on those choices.

Thank you. I am happy to take questions.""",
]
