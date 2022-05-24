import sys

n = int(sys.stdin.readline())
customerList = list()

for i in range(n):
    arr = list(map(str, sys.stdin.readline().split()))
    arr.append(i)
    customerList.append(arr)
    
                            #나이값을 int로 형변환 하며 정렬
customerList.sort(key=lambda x : (int(x[0]), int(x[2])))    

for customer in customerList:
    print(customer[0],customer[1])