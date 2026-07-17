class Solution:
    # time O(n), space O(1)
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers) - 1
        while l < r:
            sum = numbers[l] + numbers[r]
            if sum > target:
                r -= 1
            if sum < target:
                l += 1
            if sum == target:
                return [l + 1, r + 1]