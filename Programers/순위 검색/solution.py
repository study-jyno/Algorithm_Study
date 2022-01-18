def solution(info, query):
    answer = []
    lang = {}
    position = {}
    career = {}
    soul = {}
    score = {}
    info_dict_list = [lang, position, career, soul, score]
    for info_index, info_item in enumerate(info):
        for index, item in enumerate(info_item.split(' ')):
            if index == 4:
                item = int(item)
            if item in info_dict_list[index]:
                info_dict_list[index][item].append(info_index)
            else:
                info_dict_list[index][item] = [info_index]

    for query_item in query:
        query_result_set = set(list(range(len(info))))
        query_list = list(enumerate(query_item.replace(' and ', ' ').split(' ')))
        for index, item in query_list[:-1]:
            if item == '-':
                continue
            query_result_set = query_result_set & set(info_dict_list[index][item])
        # 수는 따로 합시다
        over_score_key_list = [x for x in score.keys() if x >= int(query_list[-1][1])]
        over_score_index = []
        for i in over_score_key_list:
            over_score_index += score[i]

        query_result_set = query_result_set & set(over_score_index)
        answer.append(len(list(query_result_set)))
    return answer


def solution_2(info, query):
    answer = []

    data_set = {}
    """
    data_set = {
    'java' : { # info_d[0]
        'front' :{ # info_d[1]
            'senior' : { # info_d[2]
                'chicken' : [10, 20] # info_d[3]
                }
            }
        }
    }
    data_set[info_d[0]][info_d[1]][info_d[2]][info_d[3]] = []
    """
    data = {}
    for a in ['cpp', 'java', 'python', '-']:
        for b in ['backend', 'frontend', '-']:
            for c in ['junior', 'senior', '-']:
                for d in ['chicken', 'pizza', '-']:
                    data.setdefault((a, b, c, d), list())
    for i in info:
        i = i.split()
        for a in [i[0], '-']:
            for b in [i[1], '-']:
                for c in [i[2], '-']:
                    for d in [i[3], '-']:
                        data[(a, b, c, d)].append(int(i[4]))

    for k in data:
        data[k].sort()

    for query_item in query:
        q = query_item.replace(' and ', ' ').split(' ')

        pool = data[tuple(q[:-1])]
        find = int(q[4])
        l = 0
        r = len(pool)
        mid = 0
        while l < r:
            mid = (r + l) // 2
            if pool[mid] >= find:
                r = mid
            else:
                l = mid + 1
        answer.append(len(pool) - l)
    return answer


if __name__ == "__main__":
    info = ["java backend junior pizza 150",
            "python frontend senior chicken 210",
            "python frontend senior chicken 150",
            "cpp backend senior pizza 260",
            "java backend junior chicken 80",
            "python backend senior chicken 50"]
    query = ["java and backend and junior and pizza 100",
             "python and frontend and senior and chicken 200",
             "cpp and - and senior and pizza 250",
             "- and backend and senior and - 150",
             "- and - and - and chicken 100",
             "- and - and - and - 150"]
    result_ = [1, 1, 1, 1, 2, 4]

    answer_ = solution_2(info, query)
    print(f'answer : {answer_} | result {result_}')
