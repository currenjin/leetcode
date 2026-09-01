class Solution(object):
    def permute(self, nums):
        results = []
        
        def dfs(index, path):
            if len(path) == len(nums):
                results.append(path[:])
                return

            for num in nums:
                if num not in path:
                    path.append(num)
                    dfs(index + 1, path)
                    path.pop()
            

        dfs(0, [])
        return results