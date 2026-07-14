class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        map = {}
        result = []
        for num in nums:
            map.setdefault(num, 0)
            map[num] += 1
        max_heap = [(-value, key) for key, value in map.items()]
        heapq.heapify(max_heap)
        for i in range(k):
            fre = heapq.heappop(max_heap)
            result.append(fre[1])
        return result