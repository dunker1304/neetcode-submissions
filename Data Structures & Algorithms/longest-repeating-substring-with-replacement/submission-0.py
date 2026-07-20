class Solution:
    # sliding window, time O(n), space O(m) - total number of unique chars
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        res = 0

        l = 0
        maxfre = 0 
        for r in range(len(s)):
            count[s[r]] = 1 + count.get(s[r], 0)
            maxfre = max(maxfre, count[s[r]])

            while (r - l + 1) - maxfre > k:
                count[s[l]] -= 1
                l += 1

            res = max(res, r - l + 1)

        return res