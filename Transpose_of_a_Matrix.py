## 2.Write a Python function that computes the transpose of a given matrix.
def transpose_matrix(a: list[list[int|float]]) -> list[list[int|float]]:
    if not a or not a[0]:
        return -1

    b = [ [ a[row][col] for row in range(len(a)) ] for col in range(len(a[0])) ]

    return b
     
