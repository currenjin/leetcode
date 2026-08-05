class Solution(object):
    def shortestPathBinaryMatrix(self, grid):
        if grid[0][0] == 1 or grid[-1][-1] == 1: return -1

        distance = 1
        queue = deque()
        queue.append((0, 0))
        grid[0][0] = 1

        rows = len(grid)
        cols = len(grid[0])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1), (-1, -1), (-1, 1), (1, -1), (1, 1)]

        while queue:
            for _ in range(len(queue)):
                curr_r, curr_c = queue.popleft()
                if curr_r == rows - 1 and curr_c == cols -1: return distance

                for dr, dc in directions:
                    nr = curr_r + dr
                    nc = curr_c + dc

                    if not (0 <= nr < rows and 0 <= nc < cols): continue
                    if grid[nr][nc] == 1: continue

                    grid[nr][nc] = 1
                    queue.append((nr, nc))
                
            distance += 1

        return -1
                
        