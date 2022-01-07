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

    answer_ = solution(info, query)
    print(f'answer : {answer_} | result {result_}')
