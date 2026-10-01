"""
Numerical simulation of the social-media repost ODE model.
Exposure classes I_0,...,I_m, sharers S, saturated R.
lambda(t) = beta * S(t) / N
"""
import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

M = 2  # I0, I1, I2

def model(y, t, N, beta, gamma, rho, sigma):
    I = y[:M+1]
    S = y[M+1]
    lam = beta * S / N

    dI = np.zeros(M+1)
    dI[0] = -lam * I[0]
    for i in range(1, M):
        dI[i] = (1 - rho[i-1] - sigma[i-1]) * lam * I[i-1] - lam * I[i]
    dI[M] = (1 - rho[M-1] - sigma[M-1]) * lam * I[M-1] - (rho[M] + sigma[M]) * lam * I[M]

    dS = 0.0
    for i in range(M+1):
        dS += rho[i] * lam * I[i]
    dS -= gamma * S

    return np.concatenate([dI, [dS]])

def run_simulation(N, beta, gamma, rho, sigma, I0_init, T=120, npts=600):
    y0 = np.zeros(M + 2)
    y0[0] = I0_init
    y0[M+1] = N - I0_init
    t = np.linspace(0, T, npts)
    sol = odeint(model, y0, t, args=(N, beta, gamma, rho, sigma))
    I_all = sol[:, :M+1]
    S = sol[:, M+1]
    R = N - I_all.sum(axis=1) - S
    return t, I_all, S, R

def main():
    N = 1000.0
    T = 120
    npts = 600

    rho_viral = np.array([0.05, 0.15, 0.25])
    sigma_viral = np.array([0.01, 0.02, 0.04])
    beta_viral = 1.5
    gamma_viral = 0.08

    rho_fizzle = np.array([0.01, 0.02, 0.03])
    sigma_fizzle = np.array([0.10, 0.15, 0.20])
    beta_fizzle = 0.15
    gamma_fizzle = 0.6

    # Moderate: same reinforcement shape as viral, lower beta/gamma ratio
    rho_mod = np.array([0.05, 0.15, 0.25])
    sigma_mod = np.array([0.01, 0.02, 0.04])
    beta_mod = 1.13
    gamma_mod = 0.089

    t1, I1, S1, R1 = run_simulation(N, beta_viral, gamma_viral, rho_viral, sigma_viral, N - 15, T, npts)
    t2, I2, S2, R2 = run_simulation(N, beta_fizzle, gamma_fizzle, rho_fizzle, sigma_fizzle, N - 15, T, npts)
    t3, I3, S3, R3 = run_simulation(N, beta_mod, gamma_mod, rho_mod, sigma_mod, N - 15, T, npts)

    # Figure 1: Viral vs Fizzle
    fig, ax = plt.subplots(1, 2, figsize=(10, 4))
    ax[0].plot(t1, S1, 'b-', label='Sharers S(t)')
    ax[0].plot(t1, R1, 'g--', label='Saturated R(t)')
    ax[0].set_xlabel('Time (dimensionless)')
    ax[0].set_ylabel('Users')
    ax[0].set_title('Viral (high $\\beta$, low $\\gamma$)')
    ax[0].legend()
    ax[0].grid(True, alpha=0.3)

    ax[1].plot(t2, S2, 'b-', label='Sharers S(t)')
    ax[1].plot(t2, R2, 'g--', label='Saturated R(t)')
    ax[1].set_xlabel('Time (dimensionless)')
    ax[1].set_ylabel('Users')
    ax[1].set_title('Fizzle (low $\\beta$, high $\\gamma$)')
    ax[1].legend()
    ax[1].grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig('fig_viral_vs_fizzle.pdf', bbox_inches='tight')
    plt.close()

    # Figure 2: Three-way S(t) comparison
    plt.figure(figsize=(7, 4))
    plt.plot(t1, S1, 'b-', label='Viral')
    plt.plot(t2, S2, 'r-', label='Fizzle')
    plt.plot(t3, S3, color='0.35', linestyle='-', label='Moderate')
    plt.xlabel('Time (dimensionless)')
    plt.ylabel('Active sharers S(t)')
    plt.title('Comparison of sharer dynamics across scenarios')
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig('fig_comparison.pdf', bbox_inches='tight')
    plt.close()

    # Figure 3: Viral compartments
    fig, ax = plt.subplots(figsize=(7, 4))
    ax.plot(t1, I1[:, 0], label='$I_0$')
    ax.plot(t1, I1[:, 1], label='$I_1$')
    ax.plot(t1, I1[:, 2], label='$I_2$')
    ax.plot(t1, S1, label='$S$')
    ax.plot(t1, R1, label='$R$')
    ax.set_xlabel('Time (dimensionless)')
    ax.set_ylabel('Users')
    ax.set_title('Viral scenario: all compartments')
    ax.legend()
    ax.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig('fig_exposure_classes.pdf', bbox_inches='tight')
    plt.close()

    # Figure 4: Sensitivity — peak S vs beta (viral rho/sigma, gamma=0.09)
    betas = np.linspace(0.2, 1.55, 28)
    gamma_sens = 0.09
    peaks = []
    for b in betas:
        t, _, S, _ = run_simulation(N, b, gamma_sens, rho_viral, sigma_viral, N - 15, T, npts)
        peaks.append(float(S.max()))
    plt.figure(figsize=(7, 4))
    plt.plot(betas, peaks, 'b-', linewidth=1.5)
    plt.xlabel(r'Repost intensity $\beta$ (fixed $\gamma=0.09$)')
    plt.ylabel(r'Peak active sharers $\max_t S(t)$')
    plt.title('Sensitivity: peak sharing vs repost intensity')
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig('fig_sensitivity_beta.pdf', bbox_inches='tight')
    plt.close()

    # Figure 5: Sensitivity — peak S vs gamma (viral rho/sigma, beta=1.2)
    gammas = np.linspace(0.06, 0.35, 25)
    beta_sens = 1.2
    peaks_g = []
    for g in gammas:
        t, _, S, _ = run_simulation(N, beta_sens, g, rho_viral, sigma_viral, N - 15, T, npts)
        peaks_g.append(float(S.max()))
    plt.figure(figsize=(7, 4))
    plt.plot(gammas, peaks_g, 'r-', linewidth=1.5)
    plt.xlabel(r'Attention decay $\gamma$ (fixed $\beta=1.2$)')
    plt.ylabel(r'Peak active sharers $\max_t S(t)$')
    plt.title('Sensitivity: peak sharing vs sharer decay rate')
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig('fig_sensitivity_gamma.pdf', bbox_inches='tight')
    plt.close()

    def stats(name, t, S, R):
        print(f'{name}: peak S = {float(S.max()):.2f} at t = {float(t[S.argmax()]):.2f}, R({T}) = {float(R[-1]):.2f}')

    stats('Viral', t1, S1, R1)
    stats('Fizzle', t2, S2, R2)
    stats('Moderate', t3, S3, R3)

if __name__ == '__main__':
    main()
