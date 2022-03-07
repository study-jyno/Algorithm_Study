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


if __name__ == "__main__":
    n = 5
    results = [[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]]
    result = 2

    answer_ = solution(n, results)
    print(f'answer : {answer_} | result {result}')
