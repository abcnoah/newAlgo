#아직 익숙해지지 않은 듯 하다...단순히 bfs로직만 짜라고 하면 짜겠는데
#이걸 활용해서 문제를 풀려고하니 어떻게 할지 감이 안오는 걸 보면 아직은 좀 더 익숙해져야 할 단계인 것 같다
#이 사람이 푼 풀이법이 내가 배운 bfs,dfs와 유사해서 참고했는데 아직 출력부분이 이해는 가지 않아서 다시 분석해야할 것 같다

import sys

n , m = map(int , sys.stdin.readline().split())

dic = {}

def dfs(dic, root):
  visited = []
  stack = [root]

  while stack:
    n = stack.pop()
    if n not in visited:
      visited.append(n)
      if n in dic:
        sub_stack = list(set(dic[n]) - set(visited))
        stack += sub_stack
  return visited

stack = []

for _ in range(m):
  nd1, nd2 = map(int , sys.stdin.readline().split())
  stack.append(nd1)
  stack.append(nd2)

  if nd1 not in dic:
    dic[nd1] = [nd2]
  else:
    dic[nd1].append(nd2)
  
  if nd2 not in dic:
    dic[nd2] = [nd1]
  else:
    dic[nd2].append(nd1)

ans = 0
stack = list(set(stack))
stack_len = len(stack)
while stack:
  vs = dfs(dic ,stack[0])
  if len(vs) != 0:
    ans += 1
  stack = [x for x in stack if x not in vs]

print(ans + n - stack_len)