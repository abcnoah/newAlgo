#간단하게 파이썬 내장함수로 처리했는데
#진법변환이 생각이 안나서 오랜만에 다시 찾아봤다
#8진법의경우 3자리씩 끊어서 계산한 값을 각각의 자리값에 넣어주고
#ex) 111 101 011(2) -> 753(8)
#16진법의 경우 4자리씩 끊어서 계산한 값을 각각의 자리값에 넣어준다.
print(oct(int(input(),2))[2:])