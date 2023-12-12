def majorityElement(self, nums):
    """
    :type nums: List[int]
    :rtype: int
    """

    distinct_nums = list(set(nums))
    print(distinct_nums)
    count_list = {}
    for i in distinct_nums:
        count_list[i] = nums.count(i)
    print(count_list)
    return max(count_list, key=count_list.get)


print(majorityElement(None, [3, 3, 4]))
