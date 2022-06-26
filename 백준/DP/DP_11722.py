#ㅠㅠ 생각을 하고 풀어야 하는데 앞에 푼 문제랑 유형이 똑같아서 자동으로 암기된 코드를 그대로
#적어버렸다....나중에 다시 풀어봐야겠다
n = int(input())
m = list(map(int, input().split()))

dp = [0 for _ in range(n)]

for i in range(n):
    for j in range(i):
        if m[i] < m[j] and dp[i] < dp[j]:
            dp[i] = dp[j]
    dp[i] += 1            
print(max(dp))    