class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        max_sum = [0]*len(nums)
        max_sum[0] = nums[0]
        for i in range(1, len(nums)):
            max_sum[i] = max(nums[i], nums[i]+max_sum[i-1])

        max_val = max(max_sum)
        return max_val
