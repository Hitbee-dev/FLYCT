'''
0과, 1의 갯수를 절반으로 제거하여 새로운 문자열을 만들려고한다.
가능한 문자열 중 사전순으로 가장 빠른 것을 구하시오.
1은 앞에서부터 0은 뒤에서부터 지우기 (가장 작은 수를 만들기 위함)
'''

import sys
input = sys.stdin.readline
S = list(input().strip())
zeros_len = S.count('0')//2
ones_len = S.count('1')//2
S_copy = S.copy()

# 앞에서부터 1을 전부 9로 치환
for i in range(len(S)):
    if ones_len != 0:
        if S[i] == '1':
            S_copy[i] = '9'
            ones_len -= 1

# 뒤에서부터 0을 전부 9로 치환
for i in reversed(range(len(S))):
    if zeros_len != 0:
        if S[i] == '0':
            S_copy[i] = '9'
            zeros_len -= 1

# 9로 치환된 문자 모두 제거
for i in range(S_copy.count('9')):
    S_copy.remove('9')

# 출력
for result in S_copy:
    print(result, end='')