class Solution(object):
    def checkSubarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """

        l = len(nums)
        if l<=1: return False
        if k==0:
            for i in range(l):
                if nums[i] != 0:
                    return False
            return True

        for i in range(l-1):
            for j in range(i+2, l+1):
                summtn = sum(nums[i:j])
                if summtn%k==0 or summtn==0:
                    return True
        return False
