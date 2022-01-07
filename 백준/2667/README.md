# Link
https://www.acmicpc.net/problem/2667
# 구현 방법
BFS 로 면적을 구하자
```python
answer = []
len_list = int(input())
visited_map = [[0 for x in range(len_list)] for x in range(len_list)]

home_map = []
for i in range(len_list):
    temp = str(input())
    home_map.append(temp)

def get_possible_node_list(row, col):
    result = []
    if row == 0:
        if home_map[row + 1][col] == '1' and visited_map[row + 1][col] == 0:
            result.append([row + 1, col])
    elif row == len(home_map) - 1:
        if home_map[row - 1][col] == '1' and visited_map[row - 1][col] == 0:
            result.append([row - 1, col])
    else:
        if home_map[row - 1][col] == '1' and visited_map[row - 1][col] == 0:
            result.append([row - 1, col])
        if home_map[row + 1][col] == '1' and visited_map[row + 1][col] == 0:
            result.append([row + 1, col])
    if col == 0:
        if home_map[row][col + 1] == '1' and visited_map[row][col + 1] == 0:
            result.append([row, col + 1])
    elif col == len(home_map) - 1:
        if home_map[row][col - 1] == '1' and visited_map[row][col - 1] == 0:
            result.append([row, col - 1])
    else:
        if home_map[row][col + 1] == '1' and visited_map[row][col + 1] == 0:
            result.append([row, col + 1])

        if home_map[row][col - 1] == '1' and visited_map[row][col - 1] == 0:
            result.append([row, col - 1])
    return result

for i in range(len(home_map)):
    for j in range(len(home_map)):
        if home_map[i][j] == '0' or visited_map[i][j] == 1:
            continue
        possible_node_list = get_possible_node_list(i, j)
        room_count = 0
        while possible_node_list:
            visit_node = possible_node_list.pop(0)
            if visited_map[visit_node[0]][visit_node[1]] == 1:
                continue
            room_count += 1
            visited_map[visit_node[0]][visit_node[1]] = 1

            possible_node_list += get_possible_node_list(visit_node[0], visit_node[1])
        if room_count != 0:
            answer.append(room_count)
            
answer.sort()     
print(len(answer))
for i in answer:
    print(i)
```

# 맞는데 왜 틀리지?
모르겠다 - 왜 틀리는지 안나와서 개빡침

# 다른 방법
https://hongcoding.tistory.com/71
```python
n = int(input())
graph = []
num = []

for i in range(n):
    graph.append(list(map(int, input())))

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


def DFS(x, y):
    if x < 0 or x >= n or y < 0 or y >= n:
        return False

    if graph[x][y] == 1:
        global count
        count += 1
        graph[x][y] = 0
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            DFS(nx, ny)
        return True
    return False


count = 0
result = 0

for i in range(n):
    for j in range(n):
        if DFS(i, j) == True:
            num.append(count)
            result += 1
            count = 0

num.sort()
print(result)
for i in range(len(num)):
    print(num[i])
```

```python
from collections import deque

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


def bfs(graph, a, b):
    n = len(graph)
    queue = deque()
    queue.append((a, b))
    graph[a][b] = 0
    count = 1

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue
            if graph[nx][ny] == 1:
                graph[nx][ny] = 0
                queue.append((nx, ny))
                count += 1
    return count


n = int(input())
graph = []
for i in range(n):
    graph.append(list(map(int, input())))

cnt = []
for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            cnt.append(bfs(graph, i, j))

cnt.sort()
print(len(cnt))
for i in range(len(cnt)):
    print(cnt[i])
```

위 2가지 방법이 있다 BFS, DFS 둘 다 가능


# 다른 방법에서 궁금한점