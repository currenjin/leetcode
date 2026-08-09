class Solution(object):
    def orangesRotting(self, grid):
        fresh_count = 0
        minutes = 0
        queue = deque()
        
        for r, row in enumerate(grid):
            for c, col in enumerate(row):
                if col == 2: queue.append((r, c))
                if col == 1: fresh_count += 1

        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        rows = len(grid)
        cols = len(grid[0])
        while queue and fresh_count:
            for _ in range(len(queue)):
                r, c = queue.popleft()

                for dr, dc in directions:
                    nr = dr + r
                    nc = dc + c

                    if not (0 <= nr < rows and 0 <= nc < cols): continue
                    if grid[nr][nc] != 1: continue

                    grid[nr][nc] = 2
                    queue.append((nr, nc))
                    fresh_count -= 1
            minutes += 1

        if fresh_count == 0: return minutes
        return -1
        

