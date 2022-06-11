#다시...
from collections import deque


def bfs(graph, start):
    visited = []
    need_visit = deque[start]
    
    if need_visit:
        m = need_visit.popleft()
        if m not in visited:
            visited.append(m)
            need_visit += graph[m] - set(visited)
    return ' '.join(str(i) for i in visited)

def dfs(graph, start):
    visited = []
    need_visit = [start]
    
    if need_visit:
        m = need_visit.pop()
        if m not in visited:
            visited.append(m)
            need_visit += graph[m] - set(visited)
    return ' '.join(str(i) for i in visited)

graph = {}
n = input().split()
node, edge, start = [int(i) for i in n]

for i in range(edge):
    edge_info = input().split()
    n1, n2 = [int(j) for j in edge_info]
    if n1 not in graph:
        graph[n1] = [n2]
    elif n2 not in graph[n1]:
        graph[n1].append(n2)
        
    if n2 not in graph:
        graph[n2] = [n1]
    elif n1 not in graph[n2]:
        graph[n2].append(n1)
print(dfs(graph, start))
print(bfs(graph, start))
        