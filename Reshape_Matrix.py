## Write a Python function that reshapes a given matrix into a specified shape. if it cant be reshaped return back an empty list [ ]
import numpy as np

def reshape_matrix(a: list[list[int | float]], new_shape: tuple[int, int]) -> list[list[int | float]]:
    flat = [item for row in a for item in row]
    
    # Check if reshaping is possible
    if len(flat) != new_shape[0] * new_shape[1]:
        return []

    # Use numpy to reshape and convert to list
    np_array = np.array(flat).reshape(new_shape)
    reshaped_matrix = np_array.tolist()

    return reshaped_matrix
