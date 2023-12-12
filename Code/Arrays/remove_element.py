def removeElement(nums, val):
    """
    :type nums: List[int]
    :type val: int
    :rtype: int
    """
    countVal = nums.count(val)
    print("count val", countVal)
    return len(nums) - countVal


print(removeElement([1, 23, 4], 23))
