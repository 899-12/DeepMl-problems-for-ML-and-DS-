import math

def phi_corr(x: list[int], y: list[int]) -> float:
    """
    Calculate the Phi coefficient between two binary variables.

    Args:
    x (list[int]): A list of binary values (0 or 1).
    y (list[int]): A list of binary values (0 or 1).

    Returns:
    float: The Phi coefficient rounded to 4 decimal places.
    """
    if len(x) != len(y):
        raise ValueError("Input lists must have the same length.")

    # Initialize the confusion matrix counts
    TP = TN = FP = FN = 0

    for xi, yi in zip(x, y):
        if xi == 1 and yi == 1:
            TP += 1
        elif xi == 0 and yi == 0:
            TN += 1
        elif xi == 0 and yi == 1:
            FP += 1
        elif xi == 1 and yi == 0:
            FN += 1

    numerator = TP * TN - FP * FN
    denominator = math.sqrt((TP + FP) * (TP + FN) * (TN + FP) * (TN + FN))

    if denominator == 0:
        val = 0.0
    else:
        val = numerator / denominator

    return round(val, 4)
