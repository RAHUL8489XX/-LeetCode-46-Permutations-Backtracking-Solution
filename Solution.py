class Solution:
    def permute(self, nums):
        res = []
        path = []

        def backtrack(used):
            if len(path) == len(nums):
                res.append(path[:])
                return
            for i in range(len(nums)):
                if not used[i]:
                    used[i] = True
                    path.append(nums[i])
                    backtrack(used)
                    path.pop()
                    used[i] = False

        backtrack([False] * len(nums))
        return res
