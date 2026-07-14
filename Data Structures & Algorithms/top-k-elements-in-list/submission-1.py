class Solution:
    # Time: O(nlogk)
    # Space: O(n+k)
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        result = []
        for num in nums:
            count[num] = count.get(num, 0) + 1
        max_heap = [(-value, key) for key, value in count.items()]
        
        heapq.heapify(max_heap)
        for i in range(k):
            fre = heapq.heappop(max_heap)
            result.append(fre[1])
        return result