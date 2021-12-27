def solution(rows, columns, queries):
    answer = []
    solve_map = [[(i * columns + j + 1) for j in range(columns)] for i in range(rows)]

    # row : x  | col : y
    def create_rotate_index_list(query):
        min_row, max_row = min(query[0], query[2]) - 1, max(query[0], query[2]) - 1
        min_col, max_col = min(query[1], query[3]) - 1, max(query[1], query[3]) - 1

        result_list = []
        for i in range(min_col, max_col):  # 윗쪽
            result_list.append([min_row, i])

        for i in range(min_row, max_row):  # 오른쪽
            result_list.append([i, max_col])

        for i in range(max_col, min_col, -1):  # 아랫쪽
            result_list.append([max_row, i])

        for i in range(max_row, min_row, -1):  # 왼쪽
            result_list.append([i, min_col])

        return result_list

    for query in queries:
        rotate_index_list = create_rotate_index_list(query)
        value_list = [solve_map[i[0]][i[1]] for i in rotate_index_list]
        answer.append(min(value_list))

        value_list = [value_list[-1]] + value_list[:-1]
        for index, value in zip(rotate_index_list, value_list):
            solve_map[index[0]][index[1]] = value
    return answer


if __name__ == "__main__":
    input_data = [
        {
            'rows': 6,
            'columns': 6,
            'queries': [[2, 2, 5, 4], [3, 3, 6, 6], [5, 1, 6, 3]],
        },
        {
            'rows': 3,
            'columns': 3,
            'queries': [[1, 1, 2, 2], [1, 2, 2, 3], [2, 1, 3, 2], [2, 2, 3, 3]],
        },
        {
            'rows': 100,
            'columns': 97,
            'queries': [[1, 1, 100, 97]],
        },

    ]
    result_ = [
        [8, 10, 25],
        [1, 1, 5, 3],
        [1]
    ]
    for item, result in zip(input_data, result_):
        answer_ = solution(item['rows'], item['columns'], item['queries'])
        print(f'answer : {answer_} | result {result}')
