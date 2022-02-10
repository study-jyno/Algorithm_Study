from typing import List
from itertools import combinations

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        answer = []
        for item in combinations(nums, 3):
            if item[0] + item[1] + item[2] == 0:
                answer.append(list(item))
        return answer


if __name__ == "__main__":
    solution_class = Solution()
    nums = [-1, 0, 1, 2, -1, -4]
    answer_ = solution_class.threeSum(nums=nums)
    result_ = [[-1, -1, 2], [-1, 0, 1]]
    print(f'answer : {answer_} | result {result_}')
