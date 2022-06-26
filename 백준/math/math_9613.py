import sys

def gcd(a, b):
    while b != 0:
        a = a % b
        a, b = b, a
    return a

n = int(sys.stdin.readline())

for i in range(n):
    sum = 0 #각 케이스마다 출력할 최대공약수들의 합
    arr = list(map(int, sys.stdin.readline().split()))
    m = arr.pop(0) #숫자의 길이 = 반복횟수
    for j in range(m):
        for k in range(j+1, m):
            sum += gcd(arr[j], arr[k])
    print(sum)        
        