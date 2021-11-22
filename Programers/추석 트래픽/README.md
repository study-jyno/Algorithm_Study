# Link

https://programmers.co.kr/learn/courses/30/lessons/17676?language=python3

# 구현 방법

각 line의 시작점과 끝 점에서부터 1초 사이에 있는 모든 line을 filter로 찾아서 count 한다
데이터 정리만 잘 되면 쉬운 문제 였다

    import datetime

    def solution(lines):
        answer = 0
        time_line_list = []
        for line in lines:
            end_time = datetime.datetime.strptime(line.split(' ')[1], '%H:%M:%S.%f')
            if '.' in line.split(' ')[2]:
                duration_time_format = '%S.%fs'
            else:
                duration_time_format = '%Ss'
            duration_time = datetime.datetime.strptime(line.split(' ')[2], duration_time_format)
            start_time = end_time - datetime.timedelta(seconds=duration_time.second,
                                                       microseconds=duration_time.microsecond - 1000)
            time_line_list.append([start_time, end_time])
        time_line_list.sort(key=lambda x: x[0])
    
        for line_ in time_line_list:
            for item in line_:
                s = item
                e = item + datetime.timedelta(seconds=1)
    
                def check_is_in(i):
                    if s <= i[1] and i[0] < e:
                        return True
                    else:
                        return False
    
                count = len(list(filter(check_is_in, time_line_list)))
                if count > answer:
                    answer = count
        return answer


# 맞는데 왜 틀리지?

# 다른 방법
내 방법이 최선이였다

# 다른 방법에서 궁금한점