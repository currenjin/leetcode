class Solution(object):
    def combine(self, n, k):
        results = []

        def dfs(num, path):
            if len(path) == k:
                results.append(path[:])
                return
            
            for candidate in range(num, n + 1):
                path.append(candidate)
                dfs(candidate + 1, path)
                path.pop()

        dfs(1, [])
        return results