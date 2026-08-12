class Solution(object):
    def nearestExit(self, maze, entrance):
        """
        1. 새로운 배열을 구현한다. (벽은 방문 처리, 출구를 queue에 담는다.)
        2. BFS를 돌린다. (다음 위치가 출구가 있는 곳이라면 완료가 되어야 함)
        3. 출구를 못 찾으면 -1
        """

        rows = len(maze)
        cols = len(maze[0])

        queue = deque()
        copy_maze = [[0] * cols for _ in range(rows)]

        for r, row in enumerate(maze):
            for c, col in enumerate(row):
                if col == "+": copy_maze[r][c] = 1
                if [r, c] == entrance: continue
                if col == "." and (r == 0 or c == 0 or r == rows - 1 or c == cols - 1): queue.append((r, c))

        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        distance = 0

        while queue:
            distance += 1
            for _ in range(len(queue)):
                cr, cc = queue.popleft()
                for dr, dc in directions:
                    nr = dr + cr
                    nc = dc + cc

                    if not (0 <= nr < rows and 0 <= nc < cols): continue
                    if copy_maze[nr][nc] == 1: continue
                    if nr == entrance[0] and nc == entrance[1]: return distance
                    
                    queue.append((nr, nc))
                    copy_maze[nr][nc] = 1


        return -1