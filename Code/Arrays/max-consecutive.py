def findMaxConsecutiveOnes(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    count = 0
    maxCount = []

    for i in range(len(nums)):
        if nums[i] == 1:
            count += 1
            maxCount.append(count)
        if nums[i] == 0:
            count = 0
    if maxCount == []:
        return 0
    return max(maxCount)


print(findMaxConsecutiveOnes([0]))
