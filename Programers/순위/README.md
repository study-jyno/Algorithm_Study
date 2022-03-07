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

```python
# 플로이드 워셜 알고리즘 사용
def solution(n, results):
    answer = 0

    INF = 4501
    graph = {x: {y: INF for y in range(1, n + 1)} for x in range(1, n + 1)}
    for item in results:
        graph[item[0]][item[1]] = 1
        graph[item[1]][item[0]] = -1

    for item in range(1, n + 1):
        graph[item][item] = 0

    for k in range(1, n + 1):
        for a in range(1, n + 1):
            for b in range(1, n + 1):
                graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])
    import pprint
    pprint.pprint(graph)
    return answer

# {1: {1: -4, 2: -3, 3: -4, 4: -5, 5: -5},
# 2: {1: -5, 2: -4, 3: -5, 4: -6, 5: -6},
# 3: {1: -4, 2: -3, 3: -4, 4: -5, 5: -5},
# 4: {1: -4, 2: -3, 3: -4, 4: -5, 5: -5},
# 5: {1: -9, 2: -8, 3: -9, 4: -10, 5: -10}}
```

# 맞는데 왜 틀리지?

이기면 더하고 지면 빼는 방식이 잘못된듯

답을 열었다

이기면 더하고 지면 빼는것이 아니라 이기면 이겼다고 하고 지면 졌다고 표현해야 한다

# 다른 방법

```python
def solution(n, results):
    answer = 0

    graph = {x: {y: 0 for y in range(1, n + 1)} for x in range(1, n + 1)}
    for item in results:
        graph[item[0]][item[1]] = 1
        graph[item[1]][item[0]] = -1

    for i in range(1, n + 1):  # 각 행별로 처리
        for j in range(1, n + 1):
            if graph[i][j] == 1:
                for m in range(1, n + 1):
                    if graph[j][m] == 1 and graph[i][m] == 0:
                        graph[i][m] = 1
                        graph[m][i] = -1
            elif graph[i][j] == -1:
                for m in range(1, n + 1):
                    if graph[j][m] == -1 and graph[i][m] == 0:
                        graph[i][m] = -1
                        graph[m][i] = 1

    for i in range(1, n + 1):
        count = 0
        for j in range(1, n + 1):
            if graph[i][j] == 0:
                count += 1
        if count == 1:
            answer += 1

    return answer
```

# 다른 방법에서 궁금한점

또 다른 방법

```python
from collections import defaultdict


def solution(n, results):
    answer = 0
    win, lose = defaultdict(set), defaultdict(set)
    for result in results:
        lose[result[1]].add(result[0])
        win[result[0]].add(result[1])

    for i in range(1, n + 1):
        for winner in lose[i]: win[winner].update(win[i])
        for loser in win[i]: lose[loser].update(lose[i])

    for i in range(1, n + 1):
        if len(win[i]) + len(lose[i]) == n - 1: answer += 1
    return answer
```

```python
def solution(n, results):
    total = [['?' for i in range(n)] for j in range(n)]

    for i in range(n):
        total[i][i] = 'SELF'

    for result in results:
        total[result[0]-1][result[1]-1] = 'WIN'
        total[result[1]-1][result[0]-1] = 'LOSE'

    for k in range(n):
        for i in range(n):
            for j in range(n):
                if total[i][k] == 'WIN' and total[k][j] == 'WIN':
                    total[i][j] = 'WIN'
                elif total[i][k] == 'LOSE' and total[k][j] == 'LOSE':
                    total[i][j] = 'LOSE'

    answer = 0

    for i in total:
        if '?' not in i:
            answer += 1

    return answer
```


```python
def solution(n, results):
    answer = 0
    graph = [[0 for cols in range(n)] for rows in range(n)]
    for r in results:   #그래프 초기화
        graph[r[0]-1][r[1]-1] = 1
        graph[r[1]-1][r[0]-1] = -1
    for i in range(n):  #각 행별로 처리
        for j in range(n):
            if graph[i][j] == 1:
                for m in range(n):
                    if graph[j][m] == 1 and graph[i][m] == 0:
                        graph[i][m] = 1
                        graph[m][i] = -1
            elif graph[i][j] == -1:
                for m in range(n):
                    if graph[j][m] == -1 and graph[i][m] == 0:
                        graph[i][m] = -1
                        graph[m][i] = 1
    for i in range(n):
        if graph[i].count(0) == 1:
            answer += 1
    return answer
```

플로이드-워셜 알고리즘을 더 풀어보자