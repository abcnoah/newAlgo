#for와 함께 쓰는 else는, for문이 중간에 break 등으로 끊기지 않고
#끝까지 수행 되었을 때 수행하는 코드

n = int(input())
num_list = list(map(int,input().split()))
cnt = 0

for num in num_list:
    if num != 1:
        for i in range(2, num):
            if num % i == 0:
                break    
        else:        
            cnt += 1
print(cnt)        