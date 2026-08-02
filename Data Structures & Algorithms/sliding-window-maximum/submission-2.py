import heapq
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        l, r = 0, 0
        maxHeap = []
        result = []
        for i in range(k):
            heapq.heappush(maxHeap, (-nums[i], i))
        
        result.append(-maxHeap[0][0])
        for i in range(k, len(nums)):
            heapq.heappush(maxHeap, (-nums[i], i))
            while True:
                maxValue, maxIdx = -maxHeap[0][0], maxHeap[0][1]
                if i - k < maxIdx <= i:
                    result.append(maxValue)
                    break
                else:
                    heapq.heappop(maxHeap)


        return result