def missingNumber(nums):
    n = len(nums)
    return (n * (n + 1)) / 2 - sum(nums)


print(missingNumber([0, 1, 2, 3, 5]))
