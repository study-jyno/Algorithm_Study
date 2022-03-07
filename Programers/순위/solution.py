import heapq

# Dijkstra
import pprint


def solution_1(n, results):
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


def solution_2(n, results):
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


if __name__ == "__main__":
    n = 5
    results = [[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]]
    result = 2

    answer_ = solution(n, results)
    print(f'answer : {answer_} | result {result}')
