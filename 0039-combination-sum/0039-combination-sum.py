class Solution(object):
    def combinationSum(self, candidates, target):
        results = []

        def dfs(start, remain, path):
            if remain < 0:
                return
                
            if remain == 0:
                results.append(path[:])
                return
            
            for index in range(start, len(candidates)):
                candidate = candidates[index]

                path.append(candidate)
                dfs(index, remain - candidate, path)
                path.pop()

        dfs(0, target, [])
        return results