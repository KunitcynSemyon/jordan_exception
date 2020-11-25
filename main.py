def jordan(matrix, row, column):
	row -= 1
	column -= 1
	temp_matrix = []
	for i in range(len(matrix)):
		temp_matrix.append([])
		for j in range(len(matrix[i])):
			temp_val = (matrix[i][j] * matrix[row][column] - matrix[i][column] * matrix[row][j]) / matrix[row][column]
			temp_matrix[i].append(temp_val)

	for i in range(len(matrix)):
		temp_matrix[i][column] = matrix[i][column] / matrix[row][column] * -1

	for i in range(len(matrix[row])):
		temp_matrix[row][i] = matrix[row][i] / matrix[row][column]

	temp_matrix[row][column] = 1 / matrix[row][column]

	return temp_matrix

print(jordan([[-1, -2, 0], [-2, 0, 3], [0, -2, -2]], 2, 3))