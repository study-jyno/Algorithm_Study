# Link
https://www.acmicpc.net/problem/10610

# 구현 방법
0이 있는지 확인
0이 있으면 0 하나 빼고 나머지의 조합이 3으로 나누어 지는지 확인
```python
from itertools import permutations
data = list(input())

if '0' not in data:
    print(-1)
    
print_bool = False
del_index = data.index('0')
removed_list = data[:del_index] + data[del_index + 1:]
for combi_str in permutations(removed_list, len(removed_list)):
    total_sum = 0
    total_str = ''
    for item in combi_str:
        total_sum += int(item)
        total_str += item
    if len(total_str) != len(str(int(total_str))):
        continue
    if total_sum % 3 == 0:
        print(total_str + '0')
        print_bool = True
        break
if print_bool:
    print(total_str + '0')
else:
    print(-1)
```

# 맞는데 왜 틀리지?
인풋값 입력 방법좀 다시 익혀야 할듯 딱 봐도 답 없음

# 다른 방법

```python
n = list(input())
n.sort(reverse=True)
sum = 0
for i in n:
    sum += int(i)
if sum % 3 != 0 or "0" not in n:
    print(-1)
else:
    print(''.join(n))
```
내 방법이 문제가 많았다.

그냥 합해서 되었을때 가장 작은 경우를 반환하면 되니깐 정렬 한 결과물을 반환하면 되는거였다.

패배 인정

# 다른 방법에서 궁금한점