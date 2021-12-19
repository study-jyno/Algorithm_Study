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


if __name__ == "__main__":
    places = [
        ["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"],
        ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"],
        ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"],
        ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"],
        ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]
    ]
    result = [1, 0, 1, 1, 1]
    places = [["PXOOO", "OOOOO", "PXOOO", "OOOOO", "OOOPO"]]
    result = [0]
    answer_ = solution(places)
    print(f'answer : {answer_} | result {result}')
