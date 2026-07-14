class Solution:
    # Time: O(n)
    # Space: O(n)
    # Each number in the array appears a certain number of times, and the maximum possible frequency is the length of the array.
    # We can use this idea by creating a list where the index represents a frequency, and at each index we store all numbers that appear exactly that many times
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        result = []
        freq = [[] for i in range(len(nums) + 1)]

        for num in nums:
            count[num] = count.get(num, 0) + 1
        for num, appear in count.items():
            freq[appear].append(num)
        
        for i in range(len(freq) - 1, 0, -1):
            for num in freq[i]:
                result.append(num)
                if len(result) == k:
                    return result