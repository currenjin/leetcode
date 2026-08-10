class Solution(object):
    def orangesRotting(self, grid):
        minutes = 0
        fresh_count = 0
        queue = deque()

        for r, row in enumerate(grid):
            for c, col in enumerate(row):
                if col == 2: queue.append((r, c))
                if col == 1: fresh_count += 1
        
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        rows = len(grid)
        cols = len(grid[0])
        while queue and fresh_count != 0:
            for _ in range(len(queue)):
                cr, cc = queue.popleft()
                for dr, dc in directions:
                    nr = dr + cr
                    nc = dc + cc

                    if not (0 <= nr < rows and 0 <= nc < cols): continue
                    if grid[nr][nc] != 1: continue

                    queue.append((nr, nc))
                    grid[nr][nc] = 2
                    fresh_count -= 1

            minutes += 1

        if fresh_count == 0: return minutes
        return -1
