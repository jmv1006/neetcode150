

grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]

grid = []

def numIslands(grid):
    if not grid: return 0
    rows, columns = len(grid), len(grid[0])
    islands = 0
    visited = set()

    def bfs(initial):
        queue = []
        queue.append(initial)

        directions = [[-1, 0], [1, 0], [0, 1], [0, -1]]

        while queue:
            r, c = queue.pop(0)
            for dr, dc in directions:
                ## checking if coordinates are valid
                if min(dr + r, dc + c) < 0 or dr + r == rows or dc + c == columns or (dr + r, dc + c) in visited or grid[dr + r][dc + c] != "1":
                    ##position is not valid
                    continue
                queue.append((dr + r, dc + c))
                visited.add((dr + r, dc + c))

    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == "1" and (i, j) not in visited:
                bfs((i, j))
                islands += 1
    
    return islands

numIslands(grid)