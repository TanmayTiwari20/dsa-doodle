def setZeroes(self, matrix):
    """
    :type matrix: List[List[int]]
    :rtype: None Do not return anything, modify matrix in-place instead.
    """
    zero_row = [False] * len(matrix)
    zero_col = [False] * len(matrix[0])
    print("Origional zero_row: ", zero_row)
    print("Origional zero_col: ", zero_col)
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == 0:
                zero_row[i] = True
                zero_col[j] = True

    print("Changed zero_row: ", zero_row)
    print("Changed zero_col: ", zero_col)
    print("Og Matrix: ", matrix)

    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if zero_row[i] or zero_col[j]:
                matrix[i][j] = 0

    print("changed Matrix: ", matrix)


print(setZeroes(None, [[1, 1, 1], [1, 0, 1], [1, 1, 1]]))
