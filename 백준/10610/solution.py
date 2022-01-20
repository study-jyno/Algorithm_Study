from itertools import permutations


def solution(input_data):
    if '0' not in input_data:
        return -1
    del_index = input_data.index('0')
    removed_list = input_data[:del_index] + input_data[del_index + 1:]
    for combi_str in permutations(removed_list, len(removed_list)):
        total_sum = 0
        total_str = ''
        for item in combi_str:
            total_sum += int(item)
            total_str += item
        if len(total_str) != len(str(int(total_str))):
            continue
        if total_sum % 3 == 0:
            return total_str + '0'
    return -1


# data = input()
#
# if '0' not in data:
#     print(-1)
#
# del_index = data.index('0')
# removed_list = data[:del_index] + data[del_index + 1:]
#
# for combi_str in permutations(removed_list, len(removed_list)):
#     sum = 0
#     total_str = ''
#     for item in combi_str:
#         sum += int(item)
#         total_str += item
#     if len(total_str) != len(str(int(total_str))):
#         continue
#     if sum % 3 == 0:
#         print(total_str + '0')
# print(-1)

if __name__ == "__main__":
    input_list = ['30', '102', '2931', '80875542']
    result_list = [30, 210, -1, 88755420]
    for input_data, result in zip(input_list, result_list):
        answer_ = solution(input_data)
        print(f'answer : {answer_} | result {result}')
