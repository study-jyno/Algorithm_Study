from typing import List


class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        pass


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
    Output: -1
    answer = Solution().networkDelayTime(times, n, k)
    print(f'answer : {answer} | result {result}')
