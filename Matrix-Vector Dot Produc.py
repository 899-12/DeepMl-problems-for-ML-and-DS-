def matrix_dot_vector(a: list[list[int|float]], b: list[int|float]) -> list[int|float]:
	if not a or not a[0]:
		return -1
	
	num_cols=len(a[0])
	if num_cols!=len(b):
		return -1
	
	result=[]
	for row in a:
		dot=sum(row[i]*b[i] for i in range (num_cols))
		result.append(dot)
	return result
