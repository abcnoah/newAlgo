from collections import deque

#깊이 우선 탐색(스택)
def DFS(graph, start):
  visited = []
  need_visit = [start]
    
  while need_visit:
    m = need_visit.pop()
    if m not in visited:
      visited.append(m)
      if m in graph:
          temp = list(set(graph[m]) - set(visited))
          temp.sort(reverse = True)
          need_visit += temp  
  return " ".join(str(i) for i in visited)
    

#너비 우선 탐색(좌측부터 팝)
def BFS(graph, start):
  visited = []
  need_visit = deque([start])
  while need_visit:
    m = need_visit.popleft()
    if m not in visited:
      visited.append(m)
      if m in graph:  
          temp = list(set(graph[m]) - set(visited))
          temp.sort()
          need_visit += temp
  return " ".join(str(i) for i in visited)
    


graph = {}
n = input().split(' ')
node, edge, start = [int(i) for i in n] 

for i in range(edge):
  edge_info = input().split(' ')
  n1, n2 = [int(j) for j in edge_info]

  if n1 not in graph:
    graph[n1] = [n2]
  elif n2 not in graph[n1]:
    graph[n1].append(n2)
    
  if n2 not in graph:
    graph[n2] = [n1]
  elif n1 not in graph[n2]:
    graph[n2].append(n1)

print(DFS(graph, start))
print(BFS(graph, start))
  