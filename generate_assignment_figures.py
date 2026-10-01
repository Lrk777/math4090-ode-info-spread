import numpy as np
import matplotlib.pyplot as plt


def predator_prey_rhs(x, y, a=5.0, b=2.0):
    dx = x * (a - x - y)
    dy = y * (x - b)
    return dx, dy


def plot_q3_phase_plane(output_path="Q3_phase_plane_a5_b2.png"):
    a, b = 5.0, 2.0
    x_min, x_max = 0.0, 6.0
    y_min, y_max = 0.0, 6.0

    xg, yg = np.meshgrid(np.linspace(x_min, x_max, 24), np.linspace(y_min, y_max, 24))
    dx, dy = predator_prey_rhs(xg, yg, a=a, b=b)
    speed = np.hypot(dx, dy)
    speed[speed == 0] = 1.0
    dxn, dyn = dx / speed, dy / speed

    fig, ax = plt.subplots(figsize=(8, 6), dpi=160)
    ax.quiver(xg, yg, dxn, dyn, color="gray", alpha=0.6, pivot="mid")

    # Nullclines
    xline = np.linspace(x_min, x_max, 400)
    ax.plot(xline, a - xline, "b--", lw=1.8, label=r"$\dot{x}=0:\ y=5-x$")
    ax.axvline(b, color="r", ls="--", lw=1.8, label=r"$\dot{y}=0:\ x=2$")
    ax.axhline(0, color="k", lw=1.0)
    ax.axvline(0, color="k", lw=1.0)

    # Forward Euler trajectories from multiple initial conditions
    dt = 0.02
    n_steps = 2400
    initials = [(0.5, 0.3), (1.5, 4.0), (3.0, 0.5), (4.5, 5.0), (2.2, 2.8)]
    for x0, y0 in initials:
        xs = [x0]
        ys = [y0]
        x, y = x0, y0
        for _ in range(n_steps):
            dx1, dy1 = predator_prey_rhs(x, y, a=a, b=b)
            x = max(0.0, x + dt * dx1)
            y = max(0.0, y + dt * dy1)
            xs.append(x)
            ys.append(y)
        ax.plot(xs, ys, lw=1.4)

    equilibria = np.array([[0, 0], [5, 0], [2, 3]])
    ax.scatter(equilibria[:, 0], equilibria[:, 1], color="black", s=28, zorder=5)
    ax.text(2.08, 3.12, "(2,3)", fontsize=10)
    ax.text(5.05, 0.12, "(5,0)", fontsize=10)
    ax.text(0.08, 0.12, "(0,0)", fontsize=10)

    ax.set_xlim(x_min, x_max)
    ax.set_ylim(y_min, y_max)
    ax.set_xlabel("Prey x")
    ax.set_ylabel("Predator y")
    ax.set_title("Q3(e) Phase Plane for x' = x(5-x-y), y' = y(x-2)")
    ax.legend(loc="upper right", fontsize=9)
    ax.grid(alpha=0.2)
    fig.tight_layout()
    fig.savefig(output_path)
    plt.close(fig)


def cobweb_plot(f, x0, n_iter, xlim, ylim, title, output_path):
    xs = np.linspace(xlim[0], xlim[1], 700)
    fig, ax = plt.subplots(figsize=(7, 5), dpi=160)
    ax.plot(xs, f(xs), "b", lw=2, label="y = f(x)")
    ax.plot(xs, xs, "k--", lw=1.5, label="y = x")

    x = x0
    for _ in range(n_iter):
        y = f(x)
        ax.plot([x, x], [x, y], color="crimson", lw=1.0)
        ax.plot([x, y], [y, y], color="crimson", lw=1.0)
        x = y

    ax.scatter([x0], [x0], color="green", s=26, zorder=5, label=f"start x0={x0}")
    ax.set_xlim(*xlim)
    ax.set_ylim(*ylim)
    ax.set_xlabel(r"$x_n$")
    ax.set_ylabel(r"$x_{n+1}$")
    ax.set_title(title)
    ax.grid(alpha=0.2)
    ax.legend(fontsize=8, loc="upper left")
    fig.tight_layout()
    fig.savefig(output_path)
    plt.close(fig)


def plot_q6_cobwebs():
    # Q6(a): x_{n+1} = (3/8)x_n + 5/2
    f1 = lambda x: (3.0 / 8.0) * x + 2.5
    cobweb_plot(
        f=f1,
        x0=10.0,
        n_iter=20,
        xlim=(-2, 11),
        ylim=(-2, 11),
        title=r"Q6(a) Cobweb: $x_{n+1}=\frac{3}{8}x_n+\frac{5}{2}$ (stable at x*=4)",
        output_path="Q6a_cobweb_linear.png",
    )

    # Q6(b): x_{n+1} = x_n^2, case |x0|<1 converges to 0
    f2 = lambda x: x**2
    cobweb_plot(
        f=f2,
        x0=0.6,
        n_iter=22,
        xlim=(-0.2, 1.2),
        ylim=(-0.2, 1.2),
        title=r"Q6(b) Cobweb: $x_{n+1}=x_n^2$ from x0=0.6 (to 0)",
        output_path="Q6b_cobweb_to0.png",
    )

    # Q6(b): x0>1 diverges
    cobweb_plot(
        f=f2,
        x0=1.1,
        n_iter=9,
        xlim=(0, 2.2),
        ylim=(0, 2.2),
        title=r"Q6(b) Cobweb: $x_{n+1}=x_n^2$ from x0=1.1 (diverges)",
        output_path="Q6b_cobweb_diverge.png",
    )


if __name__ == "__main__":
    plot_q3_phase_plane()
    plot_q6_cobwebs()
    print("Generated: Q3_phase_plane_a5_b2.png")
    print("Generated: Q6a_cobweb_linear.png")
    print("Generated: Q6b_cobweb_to0.png")
    print("Generated: Q6b_cobweb_diverge.png")
