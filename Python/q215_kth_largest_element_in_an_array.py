class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """

        # return self.sorting_soln(nums, k)
        return self.max_heap(nums, k)

    def max_heap(self, nums, k):
        heap = nums[:k]
        heapq.heapify(heap)
        for i in nums[k:]:
            if i>heap[0]:
                heap[0]=i
                heapq.heapify(heap)
        return heap[0]

    def sorting_soln(self, nums, k):
        nums = sorted(nums)
        counter = 0
        ans = 0
        for i in range(len(nums)-1,-1,-1):
            counter+=1
            if counter==k:
                ans = nums[i]
                break
        return ans
