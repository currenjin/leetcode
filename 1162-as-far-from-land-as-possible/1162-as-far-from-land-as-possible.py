class Solution(object):
    def maxDistance(self, grid):
        """
        1. 육지를 찾아 queue에 저장한다.
        2. BFS로 물들을 전부 방문처리한다.
        3. 최대 값을 반환한다.
        4. 없으면 -1을 반환한다.

        시간복잡도
            - 초기 순회: O(RC)
            - BFS: O(RC)
        """

        queue = deque()
        notInZero = 0

        for r, row in enumerate(grid):
            if 0 not in row: notInZero += 1
            for c, col in enumerate(row):
                if col == 1: queue.append((r, c))

        rows = len(grid)
        cols = len(grid[0])
        distance = -1

        if notInZero == rows: return distance

        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        while queue:
            distance += 1
            for _ in range(len(queue)):
                cr, cc = queue.popleft()
                for dr, dc in directions:
                    nr = dr + cr
                    nc = dc + cc

                    if not (0 <= nr < rows and 0 <= nc < cols): continue
                    if grid[nr][nc] == 1: continue

                    grid[nr][nc] = 1
                    queue.append((nr, nc))

        return distance