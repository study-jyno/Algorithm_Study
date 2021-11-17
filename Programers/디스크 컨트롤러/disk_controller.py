import heapq


def solution(jobs):
    answer = 0
    jobs_len = len(jobs)
    jobs.sort(key=lambda x: x[1])
    work_time = 0
    while jobs:
        work_job = None
        for job in jobs:
            if job[0] <= work_time:
                work_job = job
                jobs.remove(job)
                break
        if work_job is None:
            work_time += 1
        else:
            work_time += work_job[1]
            answer += work_time - work_job[0]

    return int(answer / jobs_len)


if __name__ == "__main__":
    jobs = [[0, 3], [1, 9], [2, 6]]
    jobs = [[24, 10], [28, 39], [43, 20], [37, 5], [47, 22], [20, 47], [15, 34], [15, 2], [35, 43], [26, 1]]
    return_value = 9
    answer = solution(jobs)
    print(f'answer : {answer} | result {return_value}')
