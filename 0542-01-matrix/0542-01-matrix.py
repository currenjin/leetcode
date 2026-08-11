class Solution(object):
    def updateMatrix(self, mat):
        queue = deque()
            
        rows = len(mat)
        cols = len(mat[0])
        
        distance = [[-1] * cols for _ in range(rows)]

        for r, row in enumerate(mat):
            for c, col in enumerate(row):
                if col == 0:
                    queue.append((r, c))
                    distance[r][c] = 0

        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        while queue:
            cr, cc = queue.popleft()
            
            for dr, dc in directions:
                nr = dr + cr
                nc = dc + cc

                if not (0 <= nr < rows and 0 <= nc < cols): continue
                if distance[nr][nc] != -1: continue

                distance[nr][nc] = distance[cr][cc] + 1
                queue.append((nr, nc))

        return distance






                