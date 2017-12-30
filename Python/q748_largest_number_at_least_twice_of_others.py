class Solution:
    def dominantIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return self.one_pass(nums)

    def one_pass(self, n):
        maxm, smaxm = -1, -1
        idxm = -1
        for i in range(len(n)):
            if n[i]>smaxm and n[i]<maxm:
                smaxm = n[i]
            elif n[i]>maxm:
                smaxm = maxm
                maxm=n[i]
                idxm = i
        if maxm==smaxm: return idxm
        else:
            if 2*smaxm<=maxm: return idxm
            else: return -1

    def two_pass(self, nums):
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
