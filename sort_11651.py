import sys

n = int(sys.stdin.readline())
li = list()

for _ in range(n):
    x, y = map(int, sys.stdin.readline().split())
    li.append([x,y])    
li.sort(key=lambda x : (x[1], x[0]))  

for i in range(n):
    print(li[i][0], li[i][1])