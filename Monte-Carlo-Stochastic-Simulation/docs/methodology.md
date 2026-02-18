# Methodology

## Objective
To study stochastic price evolution under Geometric Brownian Motion (GBM)
and evaluate Monte Carlo convergence against analytical Black–Scholes pricing.

## Model Assumptions
- Log-normal asset dynamics
- Constant volatility and risk-free rate
- No transaction costs
- European-style payoff

## Simulation Approach
We discretize GBM using:

S(t+Δt) = S(t) * exp[(r − ½σ²)Δt + σ√Δt Z]

where Z ~ N(0,1).

Multiple independent paths are generated to approximate the expectation:

Price ≈ exp(-rT) * E[Payoff]

## Validation
Monte Carlo estimates are compared with the closed-form Black–Scholes solution
to analyze numerical convergence and estimator variance.

## Experimental Focus
This project emphasizes:
- stochastic simulation fidelity
- numerical stability
- statistical convergence behavior
- computational workload scaling with number of paths
