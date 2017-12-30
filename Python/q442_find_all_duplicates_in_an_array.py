class Solution:
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        # return self.countarray_solution(nums)
        return self.bitmask_solution(nums)

    def bitmask_solution(self, nums):
        def create_special(nums):
            '''create a special bit for elements
            not present in the original array.

            The bit should have a leading one (check)
            '''

            val = 10*(len(nums)+1)

        bit = 0
        specialbit = create_special(nums)

        for i in nums:
            print(i, bit, end=' ')
            bit = self.togglebit(bit, i)
            print(bit)

        print(bit)
        return []

    def togglebit(self, bit, n):
        def is_zero(bit, n):
            rem = bit%10**n
            if rem==0 or rem<10**(n-1): return True
            else: return False

        if is_zero(bit, n):
            bit+=10**(n-1)
        else:
            bit-=10**(n-1)

        return bit


    def countarray_solution(self, nums):
        count = [0]*(len(nums)+1)
        ans = []
        for i in nums:
            count[i]+=1
        for i, v in enumerate(count):
            if v>1:
                ans.append(i)
        return ans
