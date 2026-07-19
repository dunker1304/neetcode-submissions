class Solution:
    # sliding window, time O(n) space O(m)
    def lengthOfLongestSubstring(self, s: str) -> int:
        mp = {}
        l = 0
        longest = 0

        for r in range(len(s)):
            if s[r] in mp:
                l = max(mp[s[r]] + 1, l)
            mp[s[r]] = r
            longest = max(longest, r - l + 1)

        return longest