import heapq
class Solution:
    # Heap: time O(nlogn), space O(n)
    # def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
    #     heap = []
    #     output = []
    #     for i in range(len(nums)):
    #         heapq.heappush(heap, (-nums[i], i))
    #         if i >= k - 1:
    #             while heap[0][1] <= i - k:
    #                 heapq.heappop(heap)
    #             output.append(-heap[0][0])
    #     return output


    # deque, time O(n) space O(n)
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        output = []
        q = deque()  # index
        l = r = 0

        while r < len(nums):
            while q and nums[q[-1]] < nums[r]:
                q.pop()
            q.append(r)

            if l > q[0]:
                q.popleft()

            if (r + 1) >= k:
                output.append(nums[q[0]])
                l += 1
            r += 1

        return output