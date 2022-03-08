from typing import List
from heapq import heapify, heappop, heappush


class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        # Todo 진행 중 03.08 23:31
        answer = 0
        graph = {}
        for item in flights:
            if item[0] not in graph:
                graph[item[0]] = {}
            graph[item[0]][item[1]] = item[2]
        # distance, node_count
        nodes = {x: [10 ** 5, n + 1] for x in range(n)}
        nodes[src] = [0, 0]  # Start point

        queue = []
        heapify(queue)
        heappush(queue, [src, nodes[src]])  # [current_destination, [current_distance, node_count]

        while queue:
            current_destination, current_node = heappop(queue)

            if current_node[1] == k + 1:  # node count >= k
                continue

            # if nodes[current_destination][0] < current_node[0]:  # 이미 최소 거리인 경우 진행할 필요 없음
            #     continue

            if current_destination in graph:
                for new_destination, new_distance in graph[current_destination].items():

                    distance = current_node[0] + new_distance
                    node_count = current_node[1] + 1

                    if distance < nodes[new_destination][0]:
                        nodes[new_destination] = [distance, node_count]
                        heappush(queue, [new_destination, [distance, node_count]])  # 다음 인접 거리를 계산 하기 위해 큐에 삽입

        if nodes[dst][0] == 10 ** 5:
            return -1
        else:
            return nodes[dst][0]


if __name__ == "__main__":
    Solution = Solution()

    # n = 3
    # flights = [[0, 1, 100], [1, 2, 100], [0, 2, 500]]
    # src = 0
    # dst = 2
    # k = 1
    # result_ = 200
    # answer_ = Solution.findCheapestPrice(n=n, flights=flights, src=src, dst=dst, k=k)
    # print(f'answer : {answer_} | result {result_}')
    #
    # n = 3
    # flights = [[0, 1, 100], [1, 2, 100], [0, 2, 500]]
    # src = 0
    # dst = 2
    # k = 0
    # result_ = 500
    # answer_ = Solution.findCheapestPrice(n=n, flights=flights, src=src, dst=dst, k=k)
    # print(f'answer : {answer_} | result {result_}')

    # n = 5
    # flights = [[4, 1, 1], [1, 2, 3], [0, 3, 2], [0, 4, 10], [3, 1, 1], [1, 4, 3]]
    # src = 2
    # dst = 1
    # k = 1
    # result_ = -1
    # answer_ = Solution.findCheapestPrice(n=n, flights=flights, src=src, dst=dst, k=k)
    # print(f'answer : {answer_} | result {result_}')

    n = 4
    flights = [[0, 1, 1], [0, 2, 5], [1, 2, 1], [2, 3, 1]]
    src = 0
    dst = 3
    k = 1

    result_ = 6
    answer_ = Solution.findCheapestPrice(n=n, flights=flights, src=src, dst=dst, k=k)
    print(f'answer : {answer_} | result {result_}')
