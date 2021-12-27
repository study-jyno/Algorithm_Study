# Link
https://programmers.co.kr/learn/courses/30/lessons/77485

# 구현 방법
지정된 행렬을 리스트로 만든 다음( index, value)
value를 한칸씩 뒤로 민 다음에 이 리스트를 만들어진 행렬에 삽입해 준다

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



# 맞는데 왜 틀리지?
맞았음 개이득

row, column 다루는 부분에서 혼란이 발생해 오래 걸렸다

# 다른 방법


# 다른 방법에서 궁금한점