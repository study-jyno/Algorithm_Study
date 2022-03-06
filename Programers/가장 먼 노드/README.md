# Link
다익스트라 사용

# 구현 방법

```python
def solution(n, edge):
    answer = 0
    graph = {}
    for item in edge:
        if item[0] not in graph:
            graph[item[0]] = []
        graph[item[0]].append(item[1])
        if item[1] not in graph:
            graph[item[1]] = []
        graph[item[1]].append(item[0])

    # 중복 제거
    for item in graph:
        graph[item] = list(set(graph[item]))

    nodes = {x: float('inf') for x in range(1, n + 1)}
    nodes[1] = 0

    queue = []
    heapq.heappush(queue, [nodes[1], 1])

    while queue:  # queue에 남아 있는 노드가 없으면 끝
        current_distance, current_destination = heapq.heappop(queue)

        if nodes[current_destination] < current_distance:
            continue
        if current_destination in graph:
            for new_destination in graph[current_destination]:
                distance = current_distance + 1
                if distance < nodes[new_destination]:
                    nodes[new_destination] = distance
                    heapq.heappush(queue, [distance, new_destination])

    max_num = 0
    max_count = 0
    for index in nodes:
        if nodes[index] == float('inf'):
            continue
        if nodes[index] > max_num:
            max_count = 1
            max_num = nodes[index]
        elif nodes[index] == max_num:
            max_count += 1
    return max_count
```

# 맞는데 왜 틀리지?


# 다른 방법


# 다른 방법에서 궁금한점