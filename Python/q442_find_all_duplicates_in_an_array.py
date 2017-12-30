class Solution:
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        count = [0]*(len(nums)+1)
        ans = []
        for i in nums:
            count[i]+=1
        for i, v in enumerate(count):
            if v>1:
                ans.append(i)
        return ans
