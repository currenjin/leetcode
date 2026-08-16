class Solution(object):
    def orangesRotting(self, grid):
        queue = deque()
        fresh = 0
        for r, row in enumerate(grid):
            for c, col in enumerate(row):
                if col == 1: fresh += 1
                if col == 2:
                    queue.append((r, c))
                    grid[r][c] = 0

        minutes = 0
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        rows = len(grid)
        cols = len(grid[0])
        while queue and fresh != 0:
            for _ in range(len(queue)):
                cr, cc = queue.popleft()
                for dr, dc in directions:
                    nr = dr + cr
                    nc = dc + cc

                    if not (0 <= nr < rows and 0 <= nc < cols): continue
                    if grid[nr][nc] != 1: continue

                    grid[nr][nc] = 0
                    queue.append((nr, nc))
                    fresh -= 1
            minutes += 1
        if fresh == 0: return minutes
        return -1
