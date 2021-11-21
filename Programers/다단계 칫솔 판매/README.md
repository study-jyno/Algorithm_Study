# Link
https://programmers.co.kr/learn/courses/30/lessons/77486?language=python3

# 구현 방법
seller 하나 마다 전체 그래프에 값을 반영하는 방식으로 진행 예정

# 맞는데 왜 틀리지?
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

답지 공개해서 확인 하는중

# 다른 방법
    def solution(enroll, referral, seller, amount):
        answer = [0]*len(enroll)
        idx_list={}
        for idx,name in enumerate(enroll):
            idx_list[name]=idx
        for idx,name in enumerate(seller):
            price=100*amount[idx]
            answer[idx_list[name]]+=price
            while referral[idx_list[name]]!="-":
                answer[idx_list[name]]-=price//10
                name=referral[idx_list[name]]
                answer[idx_list[name]]+=price//10
                price=price//10
                if price==0:
                    break
            answer[idx_list[name]]-=price//10
        return answer



# 또 다른 방법
    def solution(enroll, referral, seller, amount):
    graph,ans = {},{e:0 for e in enroll}

    for e,r in zip(enroll,referral): graph[e]=r

    for s,a in zip(seller,amount):
        money = a*100
        rate = money//10
        ans[s] += money-rate
        x = graph[s]

        while x != "-":
            if rate==0: break
            ans[x] += rate-rate//10
            rate//=10
            x = graph[x]

    return list(ans.values())

# 다른 방법에서 궁금한점
내 방법은 판매자가 관련있는 모든 부모를 찾고 부모를 따라 올라가면서 하는 방식인데 다른 방식에서는 그냥 바로 찾아가면서 진행함 - 이건 상관 없는듯
어디서 차이가 발생하는 걸까

1. list index 검색으로 하는것이 아니라 딕셔너리를 사용해 인덱스 검색 속도를 향상 시켰음
