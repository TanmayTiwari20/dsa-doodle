def subarraySum(self, nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: int
    """
    cur_sum = 0
    count = 0
    sum_dict = {0: 1}
    print("nums: ", nums)
    for i in range(len(nums)):
        cur_sum = cur_sum + nums[i]
        print("cur_sum: ", cur_sum)
        print("curr_sum - k :", cur_sum - k)
        count += sum_dict.get(cur_sum - k, 0)
        print("count: ", count)
        print("sum_dict: ", sum_dict)
        print("Curr_sum - k: ", sum_dict.get(cur_sum - k, 0))
        sum_dict[cur_sum] = sum_dict.get(cur_sum, 0) + 1
        print("sum_dict after adding: ", sum_dict)
    return count


print(subarraySum(None, [1, 2, 3, 1, -2, -2], 10))
