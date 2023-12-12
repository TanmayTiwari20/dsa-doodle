import numpy as np

my_arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])


def max_product(nums):
    max_prod = 0
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] * nums[j] > max_prod:
                max_prod = nums[i] * nums[j]
                pairs = str(nums[i]) + "," + str(nums[j])
    print(pairs)
    print(max_prod)


max_product(my_arr)
