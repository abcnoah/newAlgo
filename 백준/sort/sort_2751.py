import sys

n = int(input()) # 입력 개수
sortedArr = list()

for _ in range(n):
    num = int(sys.stdin.readline())
    sortedArr.append(num)
sortedArr.sort()

for i in sortedArr:
    print(i)

##반복문 내에서 int(input())을 사용하였더니 시간초과가 나와서
#     import sys
#     sys.stdin.readline() 사용 후 해결
#     
#input과 sys.stdin.readline의 차이점
#일단 sys.stdin.readline()과 input()은 같은 역할을 하지 않는다.
#input() 내장 함수는 parameter로 prompt message를 받을 수 있다. 따라서 입력받기 전 prompt message를 출력해야 한다. 물론 prompt message가 없는 경우도 있지만, 이 경우도 약간의 부하로 작용할 수 있다. 하지만, sys.stdin.readline()은 prompt message를 인수로 받지 않는다.
#또한, input() 내장 함수는 입력받은 값의 개행 문자를 삭제시켜서 리턴한다. 즉 입력받은 문자열에 rstrip() 함수를 적용시켜서 리턴한다. 반면에 sys.stdin.readline()은 개행 문자를 포함한 값을 리턴한다. 이 때문에 조금 귀찮은 점이 있기도 하다.
# https://buyandpray.tistory.com/7 (참고사이트)