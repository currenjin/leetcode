class Solution(object):
    def numIslands(self, grid):
        land = 0
        queue = deque()
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        rows = len(grid)
        cols = len(grid[0])

        for r, row in enumerate(grid):
            for c, col in enumerate(row):
                if col == "1":
                    land += 1
                    queue.append((r, c))
                    grid[r][c] = "0"

                    while queue:
                        curr_r, curr_c = queue.popleft()

                        for dr, dc in directions:
                            nr = curr_r + dr
                            nc = curr_c + dc

                            if not (0 <= nr < rows and 0 <= nc < cols): continue
                            if grid[nr][nc] == "0": continue

                            grid[nr][nc] = "0"
                            queue.append((nr, nc))


        return land