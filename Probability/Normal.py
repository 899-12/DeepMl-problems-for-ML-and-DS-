"""

Write a Python function to calculate the probability density function (PDF) of the normal distribution for a given value, mean, and standard deviation. 
The function should use the mathematical formula of the normal distribution to return the PDF value rounded to 5 decimal places.

"""
import math

def normal_pdf(x, mean, std_dev):
    coefficient = 1 / (std_dev * math.sqrt(2 * math.pi))
    exponent = math.exp(-((x - mean) ** 2) / (2 * std_dev ** 2))
    val = coefficient * exponent
    
	return round(val,5)
