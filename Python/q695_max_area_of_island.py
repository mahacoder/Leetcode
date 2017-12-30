class Solution:
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        ans = 0
        r, c = len(grid), len(grid[0])
        for i in range(r):
            for j in range(c):
                if grid[i][j]==1:
                    area = self.dfs(grid, i, j)
                    if area > ans: ans = area
        return ans

    def dfs(self, grid, i, j):
        area = 0
        if grid[i][j]==0:
            return area
        grid[i][j]=0
        area = 1
        if j<len(grid[0])-1: area+=self.dfs(grid, i, j+1)
        if j>0: area+= self.dfs(grid, i, j-1)
        if i<len(grid)-1: area+= self.dfs(grid, i+1, j)
        if i>0: area+= self.dfs(grid, i-1, j)

        return area
