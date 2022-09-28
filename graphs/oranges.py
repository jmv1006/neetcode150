def orangesRotting(grid):
    minutes = 0

    rows, cols = len(grid), len(grid[0])
    rotten = []
    fresh = 0

    ## Count up fresh oranges and create a queue for all rotten ones
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == 1: fresh += 1
            elif grid[i][j] == 2: 
                rotten.append((i, j))
    
    ## while there are rotten oranges in queue and some fresh still
    while rotten and fresh > 0:
        minutes += 1

        for __ in range(len(rotten)):
            r, c = rotten.pop(0)

            neighbors = [[-1, 0], [1, 0], [0, 1], [0, -1]]

            ##check which neighbors can be rottened
            for dr, dc in neighbors:
                ## if space is in matrix and is not rotten or empty
                if dr + r in range(rows) and dc + c in range(cols) and grid[dr + r][dc + c] == 1:
                    grid[dr + r][dc + c] = 2
                    rotten.append((dr + r, dc + c))
                    fresh -= 1
    
    ##if there is no more fresh oranges, we can return minutes
    if not fresh:
        return minutes
    ##if fresh oranges exist, return -1
    else: 
        return -1
           




grid = [[2,1,1],[1,1,0],[0,1,1]]
grid2 = [[2,1,1],[0,1,1],[1,0,1]]
grid3 = [[1, 2]]
print(orangesRotting(grid))

