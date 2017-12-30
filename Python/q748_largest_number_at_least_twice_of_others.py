class Solution:
    def dominantIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        maxm = max(nums)
        flag, idx = True, -1
        for i in range(len(nums)):
            if nums[i]==maxm: idx=i
            else:
                if 2*nums[i]>maxm:
                    flag = False
                    idx = -1
                    break
        return idx
