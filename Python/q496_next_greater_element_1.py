class Solution:
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """

        ans = [-1]*len(nums1)
        for i in range(len(nums1)):
            found = False
            for j in range(len(nums2)):
                if nums2[j]==nums1[i]:
                    found = True
                if found and nums2[j]>nums1[i]:
                    ans[i] = nums2[j]
                    break
        return ans
