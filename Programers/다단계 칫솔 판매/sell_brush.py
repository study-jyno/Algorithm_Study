def solution(enroll, referral, seller, amount):
    answer = [0 for x in range(len(enroll))]

    def get_parent_index(seller_name):
        seller_index = enroll.index(seller_name)
        if referral[seller_index] == '-':
            return None
        else:
            return enroll.index(referral[seller_index])

    def get_parent_route(seller_name):
        parent_route = [enroll.index(seller_name)]
        temp = seller_name
        while get_parent_index(temp):
            parent_index = get_parent_index(temp)
            parent_route.append(parent_index)
            temp = enroll[parent_index]
        return parent_route

    for sell, count in zip(seller, amount):
        parent_route = get_parent_route(sell)
        proceeds = count * 100
        for index, node in enumerate(parent_route):
            if proceeds <= 0:
                break
            answer[node] += proceeds - proceeds // 10
            proceeds = proceeds // 10

    return answer


if __name__ == "__main__":
    # enroll = ["john", "mary", "edward", "sam", "emily", "jaimie", "tod", "young"]
    # referral = ["-", "-", "mary", "edward", "mary", "mary", "jaimie", "edward"]
    # seller = ["young", "john", "tod", "emily", "mary"]
    # amount = [12, 4, 2, 5, 10]
    # result_ = [360, 958, 108, 0, 450, 18, 180, 1080]

    enroll = ["john", "mary", "edward", "sam", "emily", "jaimie", "tod", "young"]
    referral = ["-", "-", "mary", "edward", "mary", "mary", "jaimie", "edward"]
    seller = ["sam", "emily", "jaimie", "edward"]
    amount = [2, 3, 5, 4]
    result_ = [0, 110, 378, 180, 270, 450, 0, 0]

    answer_ = solution(enroll, referral, seller, amount)
    print(f'answer : {answer_} | result {result_}')
