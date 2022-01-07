# Link
https://programmers.co.kr/learn/courses/30/lessons/12982

# 구현 방법

```python
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
```

# 맞는데 왜 틀리지?
내 답이 정답임

# 다른 방법


# 다른 방법에서 궁금한점