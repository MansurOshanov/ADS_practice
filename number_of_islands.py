class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited_nodes = set()
        num_islands = 0
        
        def dfs(i, j):
            if (i, j) in visited_nodes:
                return
            if grid[i][j] == '0':
                return
            visited_nodes.add((i,j))
            dfs(max(0, i-1), j)
            dfs(min(len(grid)-1, i+1), j)
            dfs(i, max(0, j-1))
            dfs(i, min(len(grid[0])-1, j+1))
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1' and (i,j) not in visited_nodes:
                    num_islands += 1
                    dfs(i,j)
        return num_islands