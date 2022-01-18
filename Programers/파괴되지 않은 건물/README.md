# Link

https://programmers.co.kr/learn/courses/30/lessons/92344?language=python3

# 구현 방법

들어온 값 index list 만들어서 해당하는 index 에 값을 더해주자

```python
def get_target_index_list(start, end):
    result_index = []
    for i in range(start[0], end[0] + 1):
        for j in range(start[1], end[1] + 1):
            result_index.append([i, j])
    return result_index


def solution(board, skill):
    answer = 0
    for item in skill:
        target_index_list = get_target_index_list([item[1], item[2]], [item[3], item[4]])
        skill_type = 1
        if item[0] == 1:
            skill_type = -1
        for t_index in target_index_list:
            board[t_index[0]][t_index[1]] += (skill_type) * item[5]

    for row in board:
        for data in row:
            if data > 0:
                answer += 1
    return answer
```

# 맞는데 왜 틀리지?

효율에서 발린다 왜지?

문제가 뭘까

다르게 풀어보자

접근 방법이 잘못됐구만 - 누적합 이라는 방법이 필요
https://tech.kakao.com/2022/01/14/2022-kakao-recruitment-round-1/

# 다른 방법

# 다른 방법에서 궁금한점