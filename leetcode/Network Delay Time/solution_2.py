import heapq
from typing import List


# 다시 풀어보기

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = {}
        for time in times:
            if time[0] not in graph:
                graph[time[0]] = {}
            graph[time[0]][time[1]] = time[2]

        nodes = {x: float('inf') for x in range(1, n + 1)}
        nodes[k] = 0  # Start Node is k

        queue = []
        heapq.heapify(queue)
        heapq.heappush(queue, [k, nodes[k]])  # [destination, distance]

        while queue:
            current_destination, current_distance = heapq.heappop(queue)

            if nodes[current_destination] < current_distance:  # 이미 최적 경로를 발견한 경우 진행할 필요 없음
                continue

            if current_destination in graph:
                for new_destination, new_distance in graph[current_destination].items():
                    distance = current_distance + new_distance
                    if distance < nodes[new_destination]:  # 기존에 알고있던 거리보다 짧은 경우에 수정 작업 진행
                        nodes[new_destination] = distance
                        heapq.heappush(queue, [new_destination, distance])

        max_distance = 0
        for item in nodes:
            if nodes[item] == float('inf'):
                return -1
            max_distance = max(max_distance, nodes[item])

        return max_distance


if __name__ == "__main__":
    result_ = []
    times = [[2, 1, 1], [2, 3, 1], [3, 4, 1]]
    n = 4
    k = 2
    result = 2
    answer = Solution().networkDelayTime(times, n, k)
    print(f'answer : {answer} | result {result}')

    times = [[1, 2, 1]]
    n = 2
    k = 1
    result = 1
    answer = Solution().networkDelayTime(times, n, k)
    print(f'answer : {answer} | result {result}')

    times = [[1, 2, 1]]
    n = 2
    k = 2
    result = -1
    answer = Solution().networkDelayTime(times, n, k)
    print(f'answer : {answer} | result {result}')
