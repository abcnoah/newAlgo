#이 문제의 포인트는 크기가 3 이상일 때 i번째 열을 선택하는 경우를 생각하는 것과
#리스트를 하나 더 만들어서 메모이제이션을 활용하는 것

#i번째 를 포함 시킨다. (여기서 또 2가지 경우 i + [i-1] + 합계[i-3], i + 합계[i-2])
#포함시키지 않는다. 합계[i-1] 선택


n = int(input())
#각각의 포도주 용량을 담을 리스트
m = [0 for _ in range(n)]
#포도주 용량들의 합을 담을 리스트
dp = [0 for _ in range(n)]

for i in range(n):
    m[i] = int(input())
for i in range(n):
    if i == 0:
        dp[i] = m[i]
    elif i == 1:
        dp[i] = m[i-1] + m[i]
    elif i == 2:
        dp[i] = max(m[i] + m[i-1], m[i] + m[i-2], dp[1])
    else:
        dp[i] = max(dp[i-1], m[i] + m[i-1] + dp[i-3], m[i] + dp[i-2])
print(max(dp))