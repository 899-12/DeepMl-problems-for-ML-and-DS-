"""
Binomial Distribution Probability

Write a Python function to calculate the probability of achieving exactly k successes in n independent Bernoulli trials,
each with probability p of success, using the Binomial distribution formula.
"""
import math

def binomial_probability(n, k, p):
    if k > n or k < 0 or p < 0 or p > 1:
        return "Invalid input"
    
    combination = math.comb(n, k)  
    probability = combination * (p ** k) * ((1 - p) ** (n - k))
    return round(probability, 5)
	
