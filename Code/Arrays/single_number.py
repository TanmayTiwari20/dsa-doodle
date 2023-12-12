class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        nums.sort()
        print(nums)

        for i in range(0, len(nums), 2):
            if i == len(nums) - 1 or nums[i] != nums[i + 1]:
                return nums[i]
        return None


obj = Solution()
print(obj.singleNumber([4, 1, 2, 1, 2]))

