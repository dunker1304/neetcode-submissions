class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        def backtracking(i, path, total):
            if total == target:
                res.append(path.copy())
                return
            if i >= len(nums) or total > target:
                return
            
            path.append(nums[i])
            backtracking(i, path, total + nums[i])

            path.pop()
            backtracking(i + 1, path, total)

        backtracking(0, [], 0)

        return res