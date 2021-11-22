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


if __name__ == "__main__":
    lines_all = [
        [
            "2016-09-15 01:00:04.001 2.0s",
            "2016-09-15 01:00:07.000 2s"
        ],
        [
            "2016-09-15 01:00:04.002 2.0s",
            "2016-09-15 01:00:07.000 2s"
        ],
        [
            "2016-09-15 20:59:57.421 0.351s",
            "2016-09-15 20:59:58.233 1.181s",
            "2016-09-15 20:59:58.299 0.8s",
            "2016-09-15 20:59:58.688 1.041s",
            "2016-09-15 20:59:59.591 1.412s",
            "2016-09-15 21:00:00.464 1.466s",
            "2016-09-15 21:00:00.741 1.581s",
            "2016-09-15 21:00:00.748 2.31s",
            "2016-09-15 21:00:00.966 0.381s",
            "2016-09-15 21:00:02.066 2.62s"
        ]
    ]
    result_all = [
        1,
        2,
        7
    ]
    for index, (lines, result_) in enumerate(zip(lines_all, result_all)):
        if index == 1:
            print()
        answer_ = solution(lines)
        print(f'answer : {answer_} | result {result_}')
