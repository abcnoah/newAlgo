X = int(input())

arr = [0]*(X+1) ##인덱스를 1부터 시작하기 위함

for i in range(2, X+1): ##인덱스가 1일때는 값이 0이니까 2번 인덱스부터 시작하도록
    
    arr[i] = arr[i-1]+1 ##결국 모든 경우의 수의 min값을 배열에 업데이트 시켜준다 
    if i % 3 == 0:
        arr[i] = min(arr[i], arr[i//3] + 1)
    if i % 2 == 0:
        arr[i] = min(arr[i], arr[i//2] + 1)
print(arr[X])