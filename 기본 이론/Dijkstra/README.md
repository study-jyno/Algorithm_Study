# Dijkstra

최단 경로 탐색 하는 방법

    # Namu wiki

    음의 가중치가 없는 그래프의 한 정점에서 모든 정점까지의 최단거리를 각각 구하는 알고리즘
    
    그래프 방향의 유무는 상관 없으나, 간선(幹線, Edge)들 중 단 하나라도 가중치가 음수이면
    이 알고리즘은 사용할 수 없다. 음의 가중치를 가지는 간선이 있으며, 
    가중치 합이 음인 사이클이 존재하지 않는 경우 벨만-포드 알고리즘을 사용 가능하다.

    또한 그래프 내에 가중치 합이 음인 사이클이 존재한다면 무한히 음의 사이클을 도는 경우
    경로 합이 음수 무한대로 발산하기 때문에 그래프 내의 최단 경로는 구성할 수 없다.

# 구현 방법

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