# Link
https://programmers.co.kr/learn/courses/30/lessons/77484?language=python3

# 구현 방법
count로 0의 갯수를 샌 0이 아닌 수가 맞춘 수를 min, 0 까지 포함한 경우를 max로 판정

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
# 다른 방법
내 답이 최선이였음
# 다른 방법에서 궁금한점

## 코드 중에 이해가 안되는 부분