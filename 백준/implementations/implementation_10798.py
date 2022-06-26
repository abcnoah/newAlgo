words = [input() for i in range(5)]

for i in range(max(len(k) for k in words)):
    for j in range(5):
        #i의 인덱스값이 해당 행의 열값보다 작을때
        if i < len(words[j]):
            print(words[j][i], end='')