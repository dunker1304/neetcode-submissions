class MedianFinder:

    def __init__(self):
        self.maxHeap = []
        self.minHeap = []

    def addNum(self, num: int) -> None:
        if len(self.minHeap) == 0:
            heapq.heappush(self.minHeap, num)
            return

        if num > self.minHeap[0]:
            heapq.heappush(self.minHeap, num)
        else:
            heapq.heappush_max(self.maxHeap, num)

        if len(self.minHeap) - len(self.maxHeap) > 1:
            tmp = heapq.heappop(self.minHeap)
            heapq.heappush_max(self.maxHeap, tmp)
        elif len(self.maxHeap) - len(self.minHeap) > 1:
            tmp = heapq.heappop_max(self.maxHeap)
            heapq.heappush(self.minHeap, tmp)

    def findMedian(self) -> float:
        if len(self.minHeap) == len(self.maxHeap):
            return (self.minHeap[0] + self.maxHeap[0]) / 2
        if len(self.minHeap) > len(self.maxHeap):
            return self.minHeap[0]
        else:
            return self.maxHeap[0]
        