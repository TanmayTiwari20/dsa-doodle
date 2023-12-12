import math


def majorityElement(nums):
    floor_nums = math.floor(len(nums) / 3)
    occurance = {}
    for i in nums:
        occurance[i] = nums.count(i)

    return [key for key, value in occurance.items() if value > floor_nums]


print(majorityElement([1, 2, 3, 4, 5, 5, 6, 6, 6, 6]))
