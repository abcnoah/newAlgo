#a, b = input().rstrip().split()
#print(int(a, int(b)))

#파이썬은 int메서드를 이용해서 진법을 바로 변환가능....
N, b = input().split()
ary = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

N = N[::-1]
result = 0

for i,n in enumerate(N):
    result += (int(b)**i)*(ary.index(n))
print(result)
