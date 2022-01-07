from typing import List


def solution(home_map):
    answer = []
    len_list = len(home_map)
    visited_map = [[0 for x in range(len(home_map))] for x in range(len(home_map))]

    def get_possible_node_list(row, col):
        # 좌 우
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
        # 위 아래
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
    print()
    answer.sort()
    result = [len(answer)]
    return answer.sort()


if __name__ == "__main__":
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
# if __name__ == "__main__":
#     result_ = [
#         3,
#         7,
#         8,
#         9,
#     ]
#     input_data = [
#         '0110100',
#         '0110101',
#         '1110101',
#         '0000111',
#         '0100000',
#         '0111110',
#         '0111000',
#     ]
#     answer_ = solution(input_data)
#     print(f'answer : {answer_} | result {result_}')
