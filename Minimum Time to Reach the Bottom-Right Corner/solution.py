import heapq

class Solution:
    def minTimeToReach(self, moveTime):
        n, m = len(moveTime), len(moveTime[0])
        dist = [[float('inf')] * m for _ in range(n)]

        # min-heap priority queue: (time, x, y)
        heap = [(0, 0, 0)]
        dist[0][0] = 0

        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        while heap:
            time, x, y = heapq.heappop(heap)

            if (x, y) == (n - 1, m - 1):
                return time

            if time > dist[x][y]:
                continue

            for dx, dy in directions:
                nx, ny = x + dx, y + dy

                if 0 <= nx < n and 0 <= ny < m:
                    wait_time = max(time, moveTime[nx][ny])
                    new_time = wait_time + 1

                    if new_time < dist[nx][ny]:
                        dist[nx][ny] = new_time
                        heapq.heappush(heap, (new_time, nx, ny))

        return -1  # unreachable (edge case)
