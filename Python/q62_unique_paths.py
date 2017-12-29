class Solution:
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        r, c = m, n
        ans = [[0 for j in range(n)] for i in range(m)]
        for i in range(r):
            ans[i][0]=1
        for j in range(c):
            ans[0][j]=1
        for i in range(1,r):
            for j in range(1,c):
                ans[i][j]=ans[i-1][j]+ans[i][j-1]

        return ans[m-1][n-1]
