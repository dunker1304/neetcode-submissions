class Solution:
    # sliding window: time O(n), space O(1)
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        s1Count, window = [0] * 26, [0] * 26
        for c in s1:
            s1Count[ord(c) - ord('a')] += 1

        for r in range(len(s2)):
            window[ord(s2[r]) - ord('a')] += 1
            if r >= len(s1):
                window[ord(s2[r - len(s1)]) - ord('a')] -= 1
            if window == s1Count:
                return True
        return False
        