def solution(lottos, win_nums):
    zero_count = lottos.count(0)
    match_num = len(set(lottos) & set(win_nums))
    rank = {
        6: 1,
        5: 2,
        4: 3,
        3: 4,
        2: 5,
        1: 6,
        0: 6
    }
    return [rank[match_num + zero_count], rank[match_num]]


if __name__ == '__main__':
    lottos = [44, 1, 0, 0, 31, 25]
    win_lottos = [31, 10, 45, 1, 6, 19]
    result = [3, 5]
    answer = solution(lottos, win_lottos)
    print(f'answer {answer} result {result} | {answer == result}')

    lottos = [0, 0, 0, 0, 0, 0]
    win_lottos = [38, 19, 20, 40, 15, 25]
    result = [1, 6]
    answer = solution(lottos, win_lottos)
    print(f'answer {answer} result {result} | {answer == result}')

    lottos = [45, 4, 35, 20, 3, 9]
    win_lottos = [20, 9, 3, 45, 4, 35]
    result = [1, 1]
    answer = solution(lottos, win_lottos)
    print(f'answer {answer} result {result} | {answer == result}')
