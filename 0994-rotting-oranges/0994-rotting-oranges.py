class Solution(object):
    def orangesRotting(self, grid):
        minutes = 0
        fresh_count = 0
        queue = deque()
        
        for r, row in enumerate(grid):
            for c, col in enumerate(row):
                if col == 2:
                    queue.append((r, c))
                elif col == 1:
                    fresh_count += 1
        
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        rows = len(grid)
        cols = len(grid[0])

        while queue:
            current_count = len(queue)

            for _ in range(current_count):
                r, c = queue.popleft()
            
                for dr, dc in directions:
                    nr = r + dr
                    nc = c + dc

                    if not (0 <= nr < rows and 0 <= nc < cols):
                        continue
                    
                    if grid[nr][nc] != 1:
                        continue
                    
                    grid[nr][nc] = 2
                    fresh_count -= 1
                    queue.append((nr, nc))

            if queue:
                minutes += 1

        if fresh_count == 0:
            return minutes

        return -1