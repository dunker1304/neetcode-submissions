class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        def backtrack(path, open, close):
            if close > open:
                return
            if len(path) == 2*n:
                res.append(path)
                return

            if close < n:
                backtrack(path + ")", open, close + 1)
            if open < n:
                backtrack(path + "(", open + 1, close)

        backtrack("(", 1, 0)
        return res


        