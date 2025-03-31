"""
Poisson Distribution Probability Calculator

Write a Python function to calculate the probability of observing exactly k events in a fixed interval using the Poisson distribution formula. 
The function should take k (number of events) and lam (mean rate of occurrences) as inputs and return the probability rounded to 5 decimal places.

"""
import math

def poisson_probability(k, lam):
    val = (math.exp(-lam) * (lam ** k)) / math.factorial(k)
    return round(val, 5)


