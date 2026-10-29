class Solution:
    # brute force: time O(n*2^n)
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = set()
        nums.sort()
        # subset = []
        def dfs(i, subset):
            if i >= len(nums):
                res.add(tuple(subset))
                return
            
            subset.append(nums[i])
            dfs(i+1, subset)

            subset.pop()
            dfs(i+1, subset)
        
        dfs(0, [])

        return [list(s) for s in res]

    # backtracking, time O(n*2^n)
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        def backtrack(i, subset):
            if i == len(nums):
                res.append(subset[::])
                return

            subset.append(nums[i])
            backtrack(i+1, subset)
            subset.pop()

            while i + 1 < len(nums) and nums[i] == nums[i + 1]:
                i += 1

            backtrack(i+1, subset)

        backtrack(0, [])

        return res