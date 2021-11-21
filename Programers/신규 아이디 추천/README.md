# Link

https://programmers.co.kr/learn/courses/30/lessons/72410?language=python3

# 구현 방법

명시된 절차대로 진행

# 다른 방법

    import re
    
    def solution(new_id):
        st = new_id
        st = st.lower()
        st = re.sub('[^a-z0-9\-_.]', '', st)
        st = re.sub('\.+', '.', st)
        st = re.sub('^[.]|[.]$', '', st)
        st = 'a' if len(st) == 0 else st[:15]
        st = re.sub('^[.]|[.]$', '', st)
        st = st if len(st) > 2 else st + "".join([st[-1] for i in range(3-len(st))])
        return st

# 다른 방법에서 궁금한점

정규표현식 공부를 더 하자...

## 코드 중에 이해가 안되는 부분