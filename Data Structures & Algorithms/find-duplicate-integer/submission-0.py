class Solution:
    # hashset time O(n), space O(n)
    def findDuplicate(self, nums: List[int]) -> int:
        seen = set()
        for num in nums:
            if num in seen:
                return num
            seen.add(num)

        return -1

    # floyd fast & slow pointer, time O(n) space O(1)
    # def findDuplicate(self, nums: List[int]) -> int:
    #     slow, fast = 0, 0
    #     while True:
    #         slow = nums[slow]
    #         fast = nums[nums[fast]]
    #         if slow == fast:
    #             break

    #     slow2 = 0
    #     while True:
    #         slow = nums[slow]
    #         slow2 = nums[slow2]
    #         if slow == slow2:
    #             return slow