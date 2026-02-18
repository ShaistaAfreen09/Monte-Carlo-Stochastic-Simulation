import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

S0 = 100
K = 100
r = 0.05
sigma = 0.2
T = 1.0
steps = 120
n_paths = 5000

dt = T / steps

np.random.seed(42)
Z = np.random.standard_normal((n_paths, steps))

paths = np.zeros((n_paths, steps + 1))
paths[:, 0] = S0

for t in range(1, steps + 1):
    paths[:, t] = paths[:, t-1] * np.exp(
        (r - 0.5*sigma**2)*dt + sigma*np.sqrt(dt)*Z[:, t-1]
    )

call_payoff = np.maximum(paths[:, -1] - K, 0)
put_payoff = np.maximum(K - paths[:, -1], 0)

mc_call = np.exp(-r*T) * np.mean(call_payoff)
mc_put = np.exp(-r*T) * np.mean(put_payoff)

d1 = (np.log(S0/K) + (r + 0.5*sigma**2)*T) / (sigma*np.sqrt(T))
d2 = d1 - sigma*np.sqrt(T)

bs_call = S0*norm.cdf(d1) - K*np.exp(-r*T)*norm.cdf(d2)
bs_put = K*np.exp(-r*T)*norm.cdf(-d2) - S0*norm.cdf(-d1)

print("Monte Carlo Call:", mc_call)
print("Black-Scholes Call:", bs_call)
print("Monte Carlo Put:", mc_put)
print("Black-Scholes Put:", bs_put)
