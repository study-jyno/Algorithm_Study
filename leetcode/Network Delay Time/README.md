# Link

https://leetcode.com/problems/network-delay-time/

# 구현 방법

다익스트라를 사용해 최단 경로 탐색

일단 해시로 그래프 만들고 다익스트라 진행

다익스트라에 익숙치 않아서 탐색 하는 방법에 대해 잘 모르겠음

자세히 보고 몇문제 더 풀어보자

```python
import heapq
from typing import List


def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
    # K : Start N : Start
    graph = {}
    for time in times:
        if time[0] not in graph:
            graph[time[0]] = {}

        graph[time[0]][time[1]] = time[2]

    nodes = {node: float('inf') for node in range(1, n + 1)}
    nodes[k] = 0
    queue = []
    heapq.heappush(queue, [nodes[k], k])  # 시작 노드부터 탐색 시작 하기 위함.

    while queue:  # queue에 남아 있는 노드가 없으면 끝
        current_distance, current_destination = heapq.heappop(queue)  # 탐색 할 노드, 거리를 가져옴.

        if nodes[current_destination] < current_distance:  # 기존에 있는 거리보다 길다면, 볼 필요도 없음
            continue
        if current_destination in graph:
            for new_destination, new_distance in graph[current_destination].items():
                distance = current_distance + new_distance  # 해당 노드를 거쳐 갈 때 거리
                if distance < nodes[new_destination]:  # 알고 있는 거리 보다 작으면 갱신
                    nodes[new_destination] = distance
                    heapq.heappush(queue, [distance, new_destination])  # 다음 인접 거리를 계산 하기 위해 큐에 삽입
    
    max_distance = 0
    for key in nodes:
        if nodes[key] == float('inf'):
            return -1
        max_distance = max(max_distance, nodes[key])

    return max_distance

```

# 맞는데 왜 틀리지?

# 다른 방법

# 다른 방법에서 궁금한점