import numpy as np

import math

def bhattacharyya_distance(p: list[float], q: list[float]) -> float:
    """
    Calculate the Bhattacharyya distance between two discrete probability distributions.

    Args:
    p (list[float]): First probability distribution.
    q (list[float]): Second probability distribution.

    Returns:
    float: Bhattacharyya distance rounded to 4 decimal places.
    """
    if len(p) != len(q) or len(p) == 0:
        return 0.0

    # Compute coefficient
    coeff = 0.0
    for pi, qi in zip(p, q):
        if pi < 0 or qi < 0:
            return 0.0  # invalid probability
        coeff += math.sqrt(pi * qi)

    if coeff == 0:
        return float('inf')  # completely disjoint

    distance = -math.log(coeff)
    return round(distance, 4)
