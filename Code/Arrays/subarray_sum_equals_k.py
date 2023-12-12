class Solution(object):
    def subArraySum(self, nums, k):
        prefixSum = {0: 1}
        res = 0
        curSum = 0
        for i in nums:
            curSum += i
            res += prefixSum.get(curSum - k, 0)
            prefixSum[curSum] = prefixSum.get(curSum, 0) + 1
        return res
