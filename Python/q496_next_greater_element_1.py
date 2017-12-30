from collections import defaultdict

class Solution:
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """

        # return brute_force(nums1, nums2)
        return self.stack_solution(nums1, nums2)

    def stack_solution(self, nums1, nums2):
        ans = [-1]*len(nums1)
        map = defaultdict()
        for i, v in enumerate(nums1):
            map[v]=i

        stack = []
        for i, v in enumerate(nums2):
            if len(stack)==0:
                stack.append(v)
            else:
                if v>stack[-1]:
                    while len(stack)!=0 and stack[-1]<v:
                        elem = stack.pop(-1)
                        if elem in map:
                            ans[map[elem]] = v
                    stack.append(v)
                else: stack.append(v)
        return ans

    def brute_force(self, nums1, nums2):
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
