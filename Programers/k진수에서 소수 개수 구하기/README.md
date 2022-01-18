# Link

https://programmers.co.kr/learn/courses/30/lessons/92335?language=python3

# 구현 방법

진수 변환 후 0으로 스플릿

- 스플릿 해도 값이 변하지 않는다면 전체 문자열 소수인지 확인
- 아니라면 각 문자열 소수인지 확인

```python
def solution(n, k):
    answer = 0
    k_num_system_string = ''
    while n != 0:
        k_num_system_string += str(n % k)
        n = n // k
    k_num_system_string = k_num_system_string[::-1]
    check_prime_list = [int(x) for x in k_num_system_string.split('0') if len(x) != 0]

    def is_prime(num):
        if num == 1:
            return False
        for i in range(2, num // 2 + 1):
            if num % i == 0:
                return False
        return True

    for number in check_prime_list:
        if is_prime(number):
            answer += 1
    return answer


if __name__ == "__main__":
    n_list = [437674, 110011]
    l_list = [3, 10]
    result_list = [3, 2]
    for n, k, result in zip(n_list, l_list, result_list):
        answer = solution(n, k)
        print(f'answer : {answer} | result {result}')
```

# 맞는데 왜 틀리지?

시간 에러 뜸 - 소수 판별에서 시간 초과가 발생하는 듯

소수 검사할 최대값을 더 줄일 수 있을까? - 더 줄일 수 있음

    제곱근(sqrt) 범위 나누기법이란? 
    
    소수 여부를 검사할 수에 대해서 그 값의 제곱근을 기준으로 그 곱은 대칭적으로 곱이 일어나므로 제곱근 이하의 작은 값까지만 검사를 하면 나머지는 검사를 할 필요가 없다는 방법으로 검사할 데이터를 제곱근 개 이하로 줄 일 수 있는 방법입니다.
    
    출처: https://www.it-note.kr/308 [IT 개발자 Note]

# 다른 방법

```python
def solution(n, k):
    answer = 0
    k_num_system_string = ''
    while n != 0:
        k_num_system_string += str(n % k)
        n = n // k
    k_num_system_string = k_num_system_string[::-1]
    check_prime_list = [int(x) for x in k_num_system_string.split('0') if len(x) != 0]

    def is_prime(num):
        if num == 1:
            return False
        max_num = int((num + 1) ** 0.5) + 1
        for i in range(2, max_num):
            if num % i == 0:
                return False
        return True

    for number in check_prime_list:
        if is_prime(number):
            answer += 1
    return answer
```

# 다른 방법에서 궁금한점

없음