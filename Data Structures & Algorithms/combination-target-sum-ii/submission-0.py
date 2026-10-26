class Solution:
    # backtracking time O(n*2^n), space O(n)
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()

        def backtracking(idx, path, total):
            if total == target:
                res.append(path.copy())
                return

            for i in range(idx, len(candidates)):
                if i > idx and candidates[i] == candidates[i-1]:
                    continue
                if total + candidates[i] > target:
                    break

                path.append(candidates[i])
                backtracking(i+1, path, total + candidates[i])
                path.pop()

                    
        backtracking(0, [], 0)
        return res
