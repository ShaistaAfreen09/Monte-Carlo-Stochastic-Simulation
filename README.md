# Monte Carlo Stochastic Simulation Model

Numerical simulation of stochastic processes for option pricing using Geometric Brownian Motion (GBM) and Monte Carlo methods, with validation against the analytical Black–Scholes formulation.

## Overview

This project implements a large-scale Monte Carlo simulation to analyze how stochastic dynamics evolve under repeated sampling.

The system numerically generates thousands of probabilistic trajectories and estimates option prices empirically, demonstrating convergence behavior and computational tradeoffs inherent to simulation-based modeling.

## Model

The asset follows a GBM process:

S(t+Δt) = S(t) · exp((r − ½σ²)Δt + σ√Δt Z)

where Z is sampled from a standard normal distribution.

## Methodology

1. Generate stochastic paths
2. Compute payoff distribution
3. Discount expected payoff
4. Compare with Black–Scholes analytical result

## Run

```bash
pip install -r requirements.txt
python monte_carlo.py
