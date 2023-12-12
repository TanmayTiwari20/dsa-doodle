import numpy as np

my_arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])


class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        for layer in range(n // 2):
            first = layer
            last = n - layer - 1
            for i in range(first, last):
                top = matrix[layer][i]
                matrix[layer][i] = matrix[-i - 1][layer]
                matrix[-i - 1][layer] = matrix[-layer - 1][-i - 1]
                matrix[-layer - 1][-i - 1] = matrix[i][-layer - 1]
                matrix[i][-layer - 1] = top
        return matrix


obj = Solution()
print(obj.rotate(my_arr))

