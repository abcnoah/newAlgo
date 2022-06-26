import sys
n = int(sys.stdin.readline())

for _ in range(n):
    vps = sys.stdin.readline().strip()
    vps_chk = []
    for j in vps:
      if vps_chk:
        if j == '(':
            vps_chk.append(j)
        elif j == ')':
            if vps_chk[-1] == '(':
                vps_chk.pop()
            else:
                vps_chk.append(j)
      else:
        vps_chk.append(j)
    if len(vps_chk) == 0:
        print('YES')
    else:
        print('NO')