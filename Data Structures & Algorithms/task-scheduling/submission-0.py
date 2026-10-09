class Solution:
    # max heap O(m)
    def leastInterval(self, tasks: List[str], n: int) -> int:
        queue = deque()
        freq = list(Counter(tasks).values())
        heapq.heapify_max(freq)
        time = 0
        while freq or queue:
            time += 1
            if freq:
                count = heapq.heappop_max(freq) - 1
                if count:
                    queue.append([count, time + n])
            else:
                time = queue[0][1]

            if queue and queue[0][1] == time:
                heapq.heappush_max(freq, queue.popleft()[0])


        return time