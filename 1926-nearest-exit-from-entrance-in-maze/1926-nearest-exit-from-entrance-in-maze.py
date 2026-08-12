class Solution(object):
    def nearestExit(self, maze, entrance):
        """
        Before
        1. 새로운 배열을 구현한다. (벽은 방문 처리, 출구를 queue에 담는다.)
        2. BFS를 돌린다. (다음 위치가 출구가 있는 곳이라면 완료가 되어야 함)
        3. 출구를 못 찾으면 -1

        시간복잡도: O(rows * cols)
        공간복잡도: O(rows * cols)

        After
        1. 입구를 큐에 저장한다.
        2. BFS를 돌린다.
            방문은 + 처리를 한다.
            r이 0 or rows - 1, c가 0 or cols - 1이면 완료다.
        3. 출구를 못 찾으면 -1
        """

        queue = deque()
        queue.append((entrance[0], entrance[1]))
        maze[entrance[0]][entrance[1]] = "+"

        rows = len(maze)
        cols = len(maze[0])

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
                    if maze[nr][nc] == "+": continue
                    if nr == 0 or nr == rows - 1 or nc == 0 or nc == cols - 1: return distance

                    queue.append((nr, nc))
                    maze[nr][nc] = "+"
        
        return -1