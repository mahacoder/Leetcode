from collections import defaultdict

class Solution(object):
    def canPartition(self, nums):

        l = len(nums)
        if l==0: return False

        total = sum(nums)
        if total%2!=0: return False

        #Tabulated DP (01 Knapsack approach)
        mat = [[False for j in range(total//2 + 1)] for i in range(len(nums)+1)]
        mat[0][0] = True
        for i in range(1,len(mat)):
            for j in range(1,len(mat[0])):
                curr = j - nums[i-1]
                if curr<0:
                    mat[i][j] = mat[i-1][j]
                else:
                    mat[i][j] = mat[i-1][j-nums[i-1]] or mat[i-1][j]


        ans = False
        for i in range(l):
            ans = ans or mat[i+1][total//2]

        return ans
