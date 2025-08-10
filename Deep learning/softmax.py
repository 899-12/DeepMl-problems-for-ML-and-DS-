"""
Write a Python function that computes the softmax activation for a given list of scores. 
The function should return the softmax values as a list, each rounded to four decimal places.
"""
import math

def softmax(scores: list[float]) -> list[float]:
	# Your code here
    max_score = max(scores)
    exp_scores = [math.exp(s - max_score) for s in scores]
    sum_exp = sum(exp_scores)
    softmax_values = [round(e / sum_exp, 4) for e in exp_scores]
    return softmax_values
	
