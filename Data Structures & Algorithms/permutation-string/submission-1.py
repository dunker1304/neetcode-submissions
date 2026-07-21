class Solution:
    # sliding window: time O(26n), space O(1)
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
            if window == s1Count: # can optimize by using param matches == 26 instead of comparing array
                return True
        return False
        

    # optimal sliding window O(n)
    # def checkInclusion(self, s1: str, s2: str) -> bool:
    #     if len(s1) > len(s2):
    #         return False

    #     s1Count, s2Count = [0] * 26, [0] * 26
    #     for i in range(len(s1)):
    #         s1Count[ord(s1[i]) - ord('a')] += 1
    #         s2Count[ord(s2[i]) - ord('a')] += 1

    #     matches = 0
    #     for i in range(26):
    #         matches += (1 if s1Count[i] == s2Count[i] else 0)

    #     l = 0
    #     for r in range(len(s1), len(s2)):
    #         if matches == 26:
    #             return True

    #         index = ord(s2[r]) - ord('a')
    #         s2Count[index] += 1
    #         if s1Count[index] == s2Count[index]:
    #             matches += 1
    #         elif s1Count[index] + 1 == s2Count[index]:
    #             matches -= 1

    #         index = ord(s2[l]) - ord('a')
    #         s2Count[index] -= 1
    #         if s1Count[index] == s2Count[index]:
    #             matches += 1
    #         elif s1Count[index] - 1 == s2Count[index]:
    #             matches -= 1
    #         l += 1
    #     return matches == 26