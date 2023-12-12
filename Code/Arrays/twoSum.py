class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        seen = {}
        for i in range(0, len(nums)):
            diff = target - nums[i]
            print("target - nums[i]: ", target - nums[i])
            if diff in seen:
                print(seen)
                return [seen[diff], i]
            else:
                seen[nums[i]] = i
                print(seen)


newObj = Solution()
print(newObj.twoSum([1, 3, 3, 4], 7))
