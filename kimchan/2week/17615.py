'''
공을 왼쪽으로 모을때(파란공, 빨간공)
공을 오른쪽으로 모을때(파란공, 빨간공)
공이 한 색으로만 되어있을 때

총 5가지의 예외처리를 하면 될듯?
'''

import sys
input = sys.stdin.readline
result = {}
N = int(input().strip())
S = input().strip()
new_s = []

print(S.lstrip('R')) 
print(S.lstrip('R').count('R')) 
# 빨간공과 파란공 묶기
buf = []
for s in S:
    if buf == []:
        buf.append(s)
    else:
        if buf[-1] == s:
            buf.append(s)
        else:
            new_s.append(buf)
            buf = [s]
if buf != []:
    new_s.append(buf)

count = 0
# new_s의 홀수번째 인덱스가 B의 개수
for idx, s in enumerate(new_s):
    if idx % 2 == 1:
        count += len(s)
result["r_left"] = count
count = 0

# new_s의 짝수번째 인덱스가 B의 개수
for idx, s in enumerate(new_s):
    if idx % 2 != 1 and idx != 0:
        count += len(s)
result["b_left"] = count
count = 0

# new_s의 짝수번째 인덱스가 B의 개수
for idx, s in enumerate(reversed(new_s)):
    if idx % 2 != 1 and idx != 0:
        count += len(s)
result["r_right"] = count
count = 0

# new_s의 홀수번째 인덱스가 B의 개수
for idx, s in enumerate(reversed(new_s)):
    if idx % 2 == 1:
        count += len(s)
result["b_right"] = count
count = 0
print(min(result.values()))

# solution(short-coding)
input()
b=input()
print(min([b.lstrip('R').count('R'),b.lstrip('B').count('B'),b.rstrip('R').count('R'),b.rstrip('B').count('B')]))