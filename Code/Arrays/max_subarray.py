def maxSubArray(self, nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    sum_array = []
    sums = {}
    for i in range(len(nums) - 1):
        for j in range(i + 1, len(nums)):
            sum_array[:] = nums[i:j]

            sums[sum(sum_array)] = sum_array
    print(sums)

    return max(sums.keys(), default=0)


print(maxSubArray(None, [-2, 1, -3, 4, -1, 2, 1, -5, 4]))
