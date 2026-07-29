class Solution:
    # sliding window, time O(n+m)
    def minWindow(self, s: str, t: str) -> str:
        if t == "":
            return ""

        countT = {}
        window = {}
        for c in t:
            countT[c] = 1 + countT.get(c, 0)

        left = 0
        have, need = 0, len(countT)
        res, resLen = [-1, -1], float('infinity')

        for right in range(len(s)):
            char = s[right]
            window[char] = 1 + window.get(char, 0)
            if char in countT and window[char] == countT[char]:
                have += 1

            while have == need:
                if (right - left + 1) < resLen:
                    res = [left, right]
                    resLen = right - left + 1

                window[s[left]] -= 1
                if s[left] in countT and window[s[left]] < countT[s[left]]:
                    have -= 1
                left += 1
                

        l, r = res
        return s[l:r+1] if resLen != float('infinity') else ""