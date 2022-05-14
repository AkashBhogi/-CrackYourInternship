class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def lol(grid,i,j):
            if i<0 or i>=len(grid) or j<0 or j>=len(grid[i]) or grid[i][j]=="0":
                return
            grid[i][j]="0"
            lol(grid,i,j+1)
            lol(grid,i+1,j)
            lol(grid,i,j-1)
            lol(grid,i-1,j)
        c=0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j]=="1":
                    lol(grid,i,j)
                    c+=1
        return c
