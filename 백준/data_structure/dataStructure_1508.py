n, k = map(int,input().split())

num = [i for i in range(1, n+1)]
perNum = [0 for _ in range(n)]#뽑아서 담을 배열
index = 0 #인덱스 값 담을 변수

for i in range(n):
    index += k-1 #num은 0번부터 시작하니까 인덱스는 k-1
    if index >= len(num):
      index = index % len(num)
    perNum[i]  = num.pop(index)    
#print(perNum)
print('<', ', '.join(str(i) for i in perNum), '>', sep="") #문자열 출력할 때 join쓰는게 아직 어색하다