class Solution(object):
    def shortestPathBinaryMatrix(self, grid):
        if grid[0][0] == 1 or grid[-1][-1] == 1: return -1

        count = 1
        queue = deque()

        queue.append((0, 0))
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]
        rows = len(grid)
        cols = len(grid[0])
        while queue:
            for _ in range(len(queue)):
                cr, cc = queue.popleft()
                if (cr == rows - 1 and cc == cols - 1): return count

                for dr, dc in directions:
                    nr = dr + cr
                    nc = dc + cc

                    if not (0 <= nr < rows and 0 <= nc < cols): continue
                    if grid[nr][nc] == 1: continue

                    queue.append((nr, nc))
                    grid[nr][nc] = 1
                
            count += 1


        return -1