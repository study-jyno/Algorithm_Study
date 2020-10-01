import sys

def graph_to_int(graph):
    int_graph = []
    for i in graph.split("\n"):
        int_graph.append([int(item) for item in i.split(" ")])
    return int_graph
    
def graph_to_dict(graph):
    int_graph = graph_to_int(graph)
    dict_graph = {}
    for item in int_graph[1:]:
        if dict_graph.get(item[0]) :
            dict_graph[item[0]].append(item[1])
        else :
            dict_graph[item[0]] = [item[1]]
        if dict_graph.get(item[1]) :
            dict_graph[item[1]].append(item[0])
        else :
            dict_graph[item[1]] = [item[0]]
        # 양방향이기 때문에 둘 다 연결 되있다고 저장해 줘야 함
    # 값 정렬
    for item, value in dict_graph.items():
        dict_graph[item].sort()

    dict_graph['graph_info'] = int_graph[0]
    return dict_graph

    
def dfs(graph):
    result = ""
    dict_graph = graph_to_dict(graph)
    visit_node = []
    statement = dict_graph['graph_info'][2]
    stack = [dict_graph['graph_info'][2]] # stact node insert
    while stack : # stack is Null? -> stop loop
        statement = stack.pop()
        if statement in visit_node :
            continue
        visit_node.append(statement)
        # print(dict_graph)
        stack += sorted(dict_graph[statement], reverse=True)
    for i in visit_node :
        result += str(i) + " "
    return result.strip()


def bfs(graph):
    result = ""
    dict_graph = graph_to_dict(graph)
    visit_node = []
    statement = dict_graph['graph_info'][2]
    queue = [dict_graph['graph_info'][2]] # stact node insert
    while queue : # stack is Null? -> stop loop
        statement = queue[0]
        del queue[0]
        if statement in visit_node :
            continue
        visit_node.append(statement)
        # print(dict_graph)
        queue += dict_graph[statement]

    for i in visit_node :
        result += str(i) + " "
    return result.strip()

test_data = sys.stdin.readlines()
print(dfs(test_data))
print(bfs(test_data))


"""
def dfs(v):
    print(v, end=' ')
    visit[v] = 1
    for i in range(1, n + 1):
        if visit[i] == 0 and s[v][i] == 1:
            dfs(i)

def bfs(v):
    queue = [v]
    visit[v] = 0
    while(queue):
        v = queue[0]
        print(v, end=' ')
        del queue[0]
        for i in range(1, n + 1):
            if visit[i] == 1 and s[v][i] == 1:
                queue.append(i)
                visit[i] = 0

n, m, v = map(int, input().split())
s = [[0] * (n + 1) for i in range(n + 1)]
visit = [0 for i in range(n + 1)]
for i in range(m):
    x, y = map(int, input().split())
    s[x][y] = 1
    s[y][x] = 1
    
dfs(v)
print()
bfs(v)
"""