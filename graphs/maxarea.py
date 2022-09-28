def maxAreaOfIsland(grid):
    rows, cols = len(grid), len(grid[0])
    area = 0
    visited = set()

    def dfs(grid, r, c, visited):
        if r == rows or c == cols or min(r, c) < 0 or (r, c) in visited or grid[r][c] != 1:
            return 0
        
        visited.add((r, c))
        curr_area = 1

        curr_area += dfs(grid, r + 1, c, visited)
        curr_area += dfs(grid, r - 1, c, visited)
        curr_area += dfs(grid, r, c + 1, visited)
        curr_area += dfs(grid, r, c - 1, visited)

        return curr_area



    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == 1:
                area = max(area, dfs(grid, i, j, visited))
    
    return area



grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]]
grid2 = [[0,0,0,0,0,0,0,0]]

print(maxAreaOfIsland(grid))