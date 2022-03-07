# Link
https://programmers.co.kr/learn/courses/30/lessons/49191?language=python3

# 구현 방법
그래프를 사용하라는데 어떻게 사용해야하는거지?

다익스트라를 사용하려 했지만 다익스트라는 한 정점에서 다른 정점에 대한 정보만 있음

-> 모든 노드의 관계를 구하는 알고리즘 - 플로이드-워셜 알고리즘


```python
# 다익스트라 방법 - 틀렸음
import heapq


def solution(n, results):
    answer = 0
    graph = {}
    for item in results:
        if item[0] not in graph:
            graph[item[0]] = []
        graph[item[0]].append(item[1])

    nodes_dist = {x: 4501 for x in range(1, n + 1)}
    nodes_dist[1] = 0  # 1번 선수 기준 거리
    queue = []
    heapq.heapify(queue)

    heapq.heappush(queue, [nodes_dist[1], 1])
    while queue:
        current_dist, current_node = heapq.heappop(queue)

        if nodes_dist[current_node] < current_dist:
            continue

        if current_node in graph:
            for new_node in graph[current_node]:
                distance = current_dist + 1
                if distance < nodes_dist[new_node]:
                    nodes_dist[new_node] = distance
                    heapq.heappush(queue, [distance, new_node])



    for item in nodes_dist:
        if nodes_dist[item] != 0 and nodes_dist[item] != 4501:
            answer += 1
    return answer
```

# 맞는데 왜 틀리지?


# 다른 방법


# 다른 방법에서 궁금한점