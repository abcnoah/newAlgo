n = int(input())
#for문 내에서 append를 할 경우 메모리 낭비가 심하니까 미리 n+1크기만큼 생성
dp = [0]*(n+1)

for i in range(1, n+1):
    if i == 1:
        dp[i] = 1
    elif i == 2:    
        dp[i] = 1
    else:
        dp[i] = dp[i-1] + dp[i-2]
print(dp[n])        