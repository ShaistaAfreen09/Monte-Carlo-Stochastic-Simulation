import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm


def run_simulation(S0, K, r, sigma, T, steps=120, n_paths=5000, seed=42):
    """
    Runs a Monte Carlo simulation for European Call and Put pricing
    under Geometric Brownian Motion and compares results with
    analytical Black–Scholes pricing.
    """

    dt = T / steps

    # Reproducibility
    np.random.seed(seed)

    # Generate random shocks
    Z = np.random.standard_normal((n_paths, steps))

    # Initialize price paths
    paths = np.zeros((n_paths, steps + 1))
    paths[:, 0] = S0

    # Simulate GBM paths
    for t in range(1, steps + 1):
        paths[:, t] = paths[:, t-1] * np.exp(
            (r - 0.5 * sigma**2) * dt + sigma * np.sqrt(dt) * Z[:, t-1]
        )

    # Monte Carlo Payoffs
    call_payoff = np.maximum(paths[:, -1] - K, 0)
    put_payoff = np.maximum(K - paths[:, -1], 0)

    mc_call = np.exp(-r * T) * np.mean(call_payoff)
    mc_put = np.exp(-r * T) * np.mean(put_payoff)

    # Black–Scholes Analytical Pricing
    d1 = (np.log(S0 / K) + (r + 0.5 * sigma**2) * T) / (sigma * np.sqrt(T))
    d2 = d1 - sigma * np.sqrt(T)

    bs_call = S0 * norm.cdf(d1) - K * np.exp(-r * T) * norm.cdf(d2)
    bs_put = K * np.exp(-r * T) * norm.cdf(-d2) - S0 * norm.cdf(-d1)

    print("----- Simulation Results -----")
    print(f"Monte Carlo Call: {mc_call:.4f}")
    print(f"Black-Scholes Call: {bs_call:.4f}")
    print(f"Monte Carlo Put: {mc_put:.4f}")
    print(f"Black-Scholes Put: {bs_put:.4f}")

    return paths, mc_call, mc_put, bs_call, bs_put


# Run experiment only when executed directly
if __name__ == "__main__":
    run_simulation(
        S0=100,
        K=100,
        r=0.05,
        sigma=0.2,
        T=1.0,
        steps=120,
        n_paths=5000
    )
