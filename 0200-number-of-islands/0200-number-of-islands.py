class Solution(object):
    def numIslands(self, grid):
        queue = deque()
        island = 0

        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        rows = len(grid)
        cols = len(grid[0])
        for r, row in enumerate(grid):
            for c, col in enumerate(row):
                if col == "1":
                    queue.append((r, c))
                    island += 1

                while queue:
                    for _ in range(len(queue)):
                        cr, cc = queue.popleft()

                        for dr, dc in directions:
                            nr = dr + cr
                            nc = dc + cc

                            if not (0 <= nr < rows and 0 <= nc < cols): continue
                            if grid[nr][nc] == "0": continue

                            grid[nr][nc] = "0"
                            queue.append((nr, nc))

        return island