class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        seen = set()
        for i in nums:
            if i in seen:
                return True
            else:
                seen.add(i)


newObj = Solution()
print(newObj.containsDuplicate([1, 2, 3, 4]))

