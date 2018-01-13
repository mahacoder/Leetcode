class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # return self.tabulation(nums)
        max_till_index = {}
        for i in range(len(nums)):
            self.memoized(nums, i, max_till_index)
        max = max_till_index[0]
        for v in max_till_index.values():
            if v>max: max=v
        return max

    def memoized(self, nums, index, max_till_index):
        if index in max_till_index: return max_till_index[index]

        if index==0:
            max_till_index[index]=nums[index]
            return max_till_index[index]

        max_till_index[index]=max(nums[index]+self.memoized(nums,index-1, max_till_index), nums[index])
        return max_till_index[index]


    def tabulation(self, nums):
        max_sum = [0]*len(nums)
        max_sum[0] = nums[0]
        for i in range(1, len(nums)):
            max_sum[i] = max(nums[i], nums[i]+max_sum[i-1])

        max_val = max(max_sum)
        return max_val
