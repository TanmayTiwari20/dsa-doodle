def rotate(nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: None Do not return anything, modify nums in-place instead.
    """
    n = len(nums) - 1
    for i in range(len(nums) - 1):
        temp = nums[i]
        print("temp", temp)
        nums[i], nums[i + 1] = nums[i + k]
        print("nums[i]", nums[i])
        print("nums[i+1]", nums[i + k])
        nums[i + 1] = temp
    print("last elements", nums[n - k + 1])
    temp = nums[n - k + 1]
    nums[n - k + 1] = nums[0]
    nums[0] = temp
    print(nums)
    return nums


# print(rotate([1, 2, 3, 4], 1))
nums = [1, 2]
print(nums[:-1])
print(nums[-1:])
