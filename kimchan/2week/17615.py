'''
공을 왼쪽으로 모을때(파란공, 빨간공)
공을 오른쪽으로 모을때(파란공, 빨간공)
공이 한 색으로만 되어있을 때

총 5가지의 예외처리를 하면 될듯?
'''

import sys
input = sys.stdin.readline
result = {}
N = 9
S = ['R', 'B', 'B', 'B', 'R', 'B', 'R', 'R', 'R']
# S = ['R', 'R', 'R', 'R', 'R', 'R', 'R', 'R', 'R']
# N = int(input().strip())
# S = list(input().strip())
r_idx = []
b_idx = []

# r, b index나누기
for idx, s in enumerate(S):
    if s == 'R':
        r_idx.append(idx)
    else:
        b_idx.append(idx)

result = S.copy()
print(r_idx, b_idx)