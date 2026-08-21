class Solution(object):
    def subsets(self, nums):
        result = []

        def dfs(index, path):
            if index == len(nums):
                result.append(path[:])
                return

            dfs(index + 1, path)
            
            path.append(nums[index])
            dfs(index + 1, path)

            path.pop()

        dfs(0, [])
        return result