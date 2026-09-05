class Solution(object):
    def subsets(self, nums):
        results = []
        
        def dfs(index, path):
            if index == len(nums):
                results.append(path[:])
                return

            dfs(index + 1, path)

            path.append(nums[index])
            dfs(index + 1, path)

            path.pop()
        
        dfs(0, [])
        return results