class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heapq.heapify_max(stones)
        while len(stones) > 1:
            xStone = heapq.heappop_max(stones)
            yStone = heapq.heappop_max(stones)
            if xStone < yStone:
                heapq.heappush_max(stones, yStone - xStone)
            elif xStone > yStone:
                heapq.heappush_max(stones, xStone - yStone)

        return stones[0] if stones else 0