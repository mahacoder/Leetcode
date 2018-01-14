class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ans = []
        if len(nums)<=2: return []

        nums = sorted(nums)
        for start in range(len(nums)-2):
            if start>0 and nums[start]==nums[start-1]: continue
            mid, end = start+1, len(nums)-1
            while mid<end:
                sum = nums[start]+nums[mid]+nums[end]
                if sum<0: mid+=1
                elif sum>0: end-=1
                else:
                    ans.append([nums[start], nums[mid], nums[end]])
                    while mid<end and nums[mid]==nums[mid+1]: mid+=1
                    while mid<end and nums[end]==nums[end-1]: end-=1
                    mid+=1
                    end-=1
        return ans


        class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ans = []
        if len(nums)<=2: return []

        nums = sorted(nums)
        for start in range(len(nums)-2):
            if start>0 and nums[start]==nums[start-1]: continue
            mid, end = start+1, len(nums)-1
            while mid<end:
                sum = nums[start]+nums[mid]+nums[end]
                if sum<0: mid+=1
                elif sum>0: end-=1
                else:
                    ans.append([nums[start], nums[mid], nums[end]])
                    while mid<end and nums[mid]==nums[mid+1]: mid+=1
                    while mid<end and nums[end]==nums[end-1]: end-=1
                    mid+=1
                    end-=1
        return ans
