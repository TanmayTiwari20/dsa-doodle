def pascalsTraingle(self, numRow):
    triangle = [[1] * (i + 1) for i in range(numRow)]
    for i in range(numRow):
        for j in range(1, i):
            triangle[i][j] = triangle[i - 1][j - 1] + triangle[i - 1][j]

    return triangle


print(pascalsTraingle(None, 5))
