def solution(d, budget):
    answer = 0
    d.sort()
    sum = 0
    for i in d:
        if budget < sum + i:
            return answer
        sum += i
        answer += 1
    return answer


if __name__ == "__main__":
    result_ = []
    d_list = [[1, 3, 2, 5, 4], [2, 2, 3, 3]]
    budget_list = [9, 10]
    result_list = [3, 4]
    for d, budget, result in zip(d_list, budget_list, result_list):
        answer_ = solution(d, budget)
        print(f'answer : {answer_} | result {result}')
