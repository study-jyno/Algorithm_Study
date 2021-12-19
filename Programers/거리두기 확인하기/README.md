# Link

https://programmers.co.kr/learn/courses/30/lessons/81302?language=python3

# 구현 방법

앉은 사람 다 뽑고 그 사람 주위를 전부 확인 하는 방법으로 구현 할 예정

앉은 사람 좌표를 추출 한 후 각 좌표의 조합을 통해 서로의 거리를 구해서 2인 경우 거리두기 수칙을 준수했는지 체크

# 맞는데 왜 틀리지?

    from itertools import combinations
    
    
    def get_distance(start_node, end_node):
        return abs(start_node[0] - end_node[0]) + abs(start_node[1] - end_node[1])
    
    
    def solution(places):
        answer = []
        for place in places:
            candidate_list = []
            for i, col in enumerate(place):
                for j, data in enumerate(col):
                    if data == 'P':
                        candidate_list.append([i, j])
    
            for node in combinations(candidate_list, 2):
                temp_answer = 1
                distance = get_distance(node[0], node[1])
                if distance == 1:
                    temp_answer = 0
                    break
                elif get_distance(node[0], node[1]) <= 2:
                    if node[0][0] == node[1][0]:
                        if place[node[0][0]][node[0][1] + 1] != 'X':
                            temp_answer = 0
                            break
                    elif node[0][1] == node[1][1]:
                        if place[node[0][0] + 1][node[0][1]] != 'X':
                            temp_answer = 0
                            break
                    else:
                        min_col = node[0][0] if node[0][0] < node[1][0] else node[1][0]
                        min_row = node[0][1] if node[0][1] < node[1][1] else node[1][1]
                        if place[min_col][min_row] == 'O' or \
                                place[min_col][min_row + 1] == 'O' or \
                                place[min_col + 1][min_row] == 'O' or \
                                place[min_col + 1][min_row + 1] == 'O':
                            temp_answer = 0
                        break
            answer.append(temp_answer)
        return answer

다른 사람은 어떻게 풀었을까 돼다가 안돼다가 함 왜그럴까 아에 런타임 에러가 뜨는 경우도 있는데

답지 열어서 확인 함

# 다른 방법

    def solution(places):
    result = []
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    def f(i, j, cnt):
        nonlocal good
        if cnt >2 : return
        if -1<i<5 and -1<j<5:
            if graph[i][j] == 'X':
                return

            if cnt != 0 and graph[i][j] == 'P':
                good = 0
                return

            graph[i][j] = 'X'

            for w in range(4):
                ni = i+dx[w]
                nj = j+dy[w]
                f(ni, nj, cnt+1)

    for case in places:
        graph = [list(r) for r in case]
        good = 1
        for i in range(5):
            for j in range(5):
                if graph[i][j]=='P':
                    f(i,j,0)

        result.append(good)
    return result

가능한 노드를 뽑아서 진행하는 것이 아니라 그냥 p 발견 시 주위에 p가 있는지 확인하는 방법 이 방법이 훨신 빠를듯

# 다른 방법에서 궁금한점

내가 멍청했다