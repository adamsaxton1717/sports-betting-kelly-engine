# Sports Betting Promo Optimization & Bankroll Engine

A Python-based quantitative framework for evaluating promotional sports betting opportunities using implied probabilities, expected value, and bankroll optimization.

## Project Overview

This project is being developed to evaluate promotional betting opportunities on platforms such as PrizePicks and Pick6. The goal is to convert sportsbook market odds into probability estimates, compare alternative promotional slip structures, and determine how capital should be allocated based on expected return and risk.

The framework is designed around manually collected sportsbook odds rather than automated scraping, allowing the quantitative engine to remain the primary focus of the project.

## Current Development

The project is currently in active development. The initial framework focuses on building the core pricing and decision pipeline:

**Sportsbook Odds → Fair Probabilities → Slip Payoffs → Expected Value → Bet Selection → Fractional Kelly Sizing**

Current work includes:

* Structuring historical betting and market data for quantitative analysis
* Converting American odds into implied probabilities
* Developing methods to remove sportsbook margin from two-sided markets
* Modeling promotional and multi-leg payout structures
* Building an expected-value framework for comparing alternative slips
* Designing bankroll tracking for future Kelly sizing and performance analysis

## Planned Quantitative Analysis

### Market Pricing

Sportsbook prices will be converted into implied probabilities and adjusted for bookmaker margin when both sides of a market are available.

### Slip Optimization

Candidate promotional entries will be evaluated using their estimated joint probabilities and displayed payout multipliers. This will allow comparisons such as:

* Discounted pick + regular selection
* Discounted pick + higher-probability reduced-payout selection
* Alternative multi-leg Power and Flex structures

### Capital Allocation

The project will implement Fractional Kelly optimization to determine bet sizing based on the full distribution of possible returns. Quarter Kelly will be used as the primary risk-management strategy.

### Bankroll Simulation & Risk Analysis

Monte Carlo simulation will be used to compare staking strategies and analyze:

* Bankroll growth and expected return
* Return volatility
* Sharpe ratio
* Maximum drawdown
* Risk of ruin

## Future Extensions

Potential extensions include:

* Alternate-line probability interpolation
* Paired-slip and middle optimization
* Correlation modeling between selections
* Portfolio-level Kelly optimization
* Automated sportsbook odds ingestion

## Tech Stack

* **Language:** Python
* **Data Analysis:** pandas, NumPy
* **Scientific Computing & Optimization:** SciPy
* **Visualization:** Matplotlib
* **Development:** Git, GitHub, Jupyter

## Status

**In Progress — Core pricing and expected-value engine under development.**
