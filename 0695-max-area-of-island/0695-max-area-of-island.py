class Solution:
    def maxAreaOfIsland(self, grid: List[List[str]]) -> int:

        paths=[(-1,0),(0,-1),(1,0),(0,1)]

        def bfs(i,j):
            area=0
            que=collections.deque()

            que.append((i,j))

            while que:
                area+=1
                row,col = que.popleft()
                grid[row][col] = 0

                for x,y in paths:
                    newr,newc = row+x , col+y 
                    if 0<= newr < m and  0<= newc < n and grid[newr][newc] != 0 :
                        que.append((newr,newc))
                        grid[newr][newc] = 0
            return area

        m=len(grid)
        n=len(grid[0])
        result=0
        maxi =0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    maxi=max(maxi,bfs(i,j))
        return maxi
