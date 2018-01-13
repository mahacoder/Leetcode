class Solution:
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # return self.iterative(nums)
        if len(nums)==0: return 0
        return self.recursion(nums, len(nums)-1, {})

    def recursion(self, nums, index, map):
        if index in map:
            return map[index]
        if index==0:
            map[0]=nums[0]
            return nums[0]
        if index==1:
            map[1]=nums[1]
            return nums[1]
            # map[1] = max(nums[0], nums[1])
            # return max(nums[0], nums[1])

        map[index]=max(nums[index] + self.recursion(nums, index-2, map), self.recursion(nums, index-1, map))
        return map[index]


    def iterative(self, nums):
        if len(nums)==0: return 0
        ans = [0]*len(nums)

        for i in range(len(nums)):
            if i==0: ans[i]=nums[i]
            elif i==1: ans[i]=max(nums[i-1], nums[i])
            else:
                ans[i]=max(ans[i-1], ans[i-2]+nums[i])
        return ans[-1]
