def rearrangeArray(self, nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    """
    negativeList = [i for i in nums if i < 0]
    positiveList = [i for i in nums if i >= 0]
    rearragedList = []
    for i in range(len(nums) // 2):
        rearragedList.append(positiveList[i])
        rearragedList.append(negativeList[i])
    return rearragedList


print(rearrangeArray(None, [3, 1, -2, -5, 2, -4]))
