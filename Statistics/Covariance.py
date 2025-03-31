"""

Write a Python function to calculate the covariance matrix for a given set of vectors.
The function should take a list of lists, where each inner list represents a feature with its observations,
and return a covariance matrix as a list of lists. Additionally, provide test cases to verify the correctness of your implementation.

"""


import numpy as np
def calculate_covariance_matrix(vectors: list[list[float]]) -> list[list[float]]:
	
    """
    Computes the covariance matrix for a given set of vectors.

    :param vectors: List of lists, where each inner list represents a feature with its observations.
    :return: Covariance matrix as a list of lists.
    """
    data_array = np.array(vectors)  # Convert list of lists into a NumPy array
    cov_matrix = np.cov(data_array, bias=False)  # Compute covariance matrix (n-1 in denominator)
    return cov_matrix.tolist()  # Convert back to list of lists
