class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.stream = nums
        heapq.heapify_max(self.stream)
        self.k = k

    def add(self, val: int) -> int:
        heapq.heappush_max(self.stream, val)
        copy = self.stream.copy()
        for i in range(self.k):
            result = heapq.heappop_max(copy)

        return result
