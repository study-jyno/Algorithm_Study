def solution(n, k):
    answer = -1
    return answer


if __name__ == "__main__":
    n_list = [437674, 110011]
    l_list = [3, 10]
    result_list = [3, 2]
    for n, k, result in zip(n_list, l_list, result_list):
        answer = solution(n, k)
        print(f'answer : {answer} | result {result}')
