def longestConsecutive(self, nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    nums[:] = sorted(nums)
    maxCount = 1
    print(nums)
    for i in range(len(nums) - 1):
        print("nums[i]: ", nums[i])
        print("nums[i + 1] -1 : ", nums[i + 1] - 1)
        if nums[i] == nums[i + 1] - 1:
            maxCount += 1
            print("MaxCount: ", maxCount)
    return maxCount


print(longestConsecutive(None, [9, 1, 4, 7, 3, -1, 0, 5, 8, -1, 6]))
