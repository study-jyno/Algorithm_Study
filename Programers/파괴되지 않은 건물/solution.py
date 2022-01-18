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


def solution_2(board, skill):
    answer = 0
    temp_dict = {}
    for item in skill:
        target_index_list = get_target_index_list([item[1], item[2]], [item[3], item[4]])
        skill_type = 1
        if item[0] == 1:
            skill_type = -1
        for t_index in target_index_list:
            tuple_index = tuple(t_index)
            if tuple_index not in temp_dict:
                temp_dict[tuple_index] = board[t_index[0]][t_index[1]]
            temp_dict[tuple_index] += (skill_type) * item[5]
            # board[t_index[0]][t_index[1]] += (skill_type) * item[5]
    for item in temp_dict.values():
        if item > 0:
            answer += 1
    # for row in board:
    #     for data in row:
    #         if data > 0:
    #             answer += 1
    return answer


if __name__ == "__main__":
    board_list = [
        [[5, 5, 5, 5, 5], [5, 5, 5, 5, 5], [5, 5, 5, 5, 5], [5, 5, 5, 5, 5]],
        [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    ]
    skill_list = [
        [[1, 0, 0, 3, 4, 4], [1, 2, 0, 2, 3, 2], [2, 1, 0, 3, 1, 2], [1, 0, 1, 3, 3, 1]],
        [[1, 1, 1, 2, 2, 4], [1, 0, 0, 1, 1, 2], [2, 2, 0, 2, 0, 100]]
    ]
    result_list = [10, 6]
    for board, skill, result in zip(board_list, skill_list, result_list):
        answer = solution_2(board, skill)
        print(f'answer : {answer} | result {result}')
