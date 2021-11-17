# Link
https://programmers.co.kr/learn/courses/30/lessons/42627?language=python3

# 구현 방법
힙을 사용해 정렬 수 해당 시간에 실행할 수 있는 작업 중 처리 시간이 가장 짧은 일부터 처리

heapq를 사용해 정렬하고 싶었지만 그러지 못했고 list를 처리시간순으로 정렬 한 후 가장 작은 처리 시간 중 할 수 있는 일을 먼저 처리하는 방식으로 진행했다

# 다른 방법
    import heapq
    from collections import deque
    
    def solution(jobs):
        tasks = deque(sorted([(x[1], x[0]) for x in jobs], key=lambda x: (x[1], x[0])))
        q = []
        heapq.heappush(q, tasks.popleft())
        current_time, total_response_time = 0, 0
        while len(q) > 0:
            dur, arr = heapq.heappop(q)
            current_time = max(current_time + dur, arr + dur)
            total_response_time += current_time - arr
            while len(tasks) > 0 and tasks[0][1] <= current_time:
                heapq.heappush(q, tasks.popleft())
            if len(tasks) > 0 and len(q) == 0:
                heapq.heappush(q, tasks.popleft())
        return total_response_time // len(jobs)

# 다른 방법에서 궁금한점
## deque?
양방향 큐
## 코드 중에 이해가 안되는 부분
    current_time = max(current_time + dur, arr + dur)
    total_response_time += current_time - arr
            
뭐하는건가 했는데 나처럼 할게 없으면 기다리는게 아니라
지금 하는지 아님 나중에 하는지(current_time + dur, arr + dur)
둘 중 더 큰게 실제 기다리는 것과 동일하기 때문에 이렇게 진행