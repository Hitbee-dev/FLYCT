# [백준 14501] 퇴사
'''
첫째 줄에 N (1 ≤ N ≤ 15)이 주어진다.
둘째 줄부터 N개의 줄에 Ti와 Pi가 공백으로 구분되어서 주어지며, 1일부터 N일까지 순서대로 주어진다. (1 ≤ Ti ≤ 5, 1 ≤ Pi ≤ 1,000)

예제 1 # 45
7
3 10
5 20
1 10
1 20
2 15
4 40
2 200
'''

import sys
input = sys.stdin.readline

# 일하는 일수
N = int(input().rstrip())
# 상담일수 T, 상담 금액 P
T, P = [0]*N, [0]*N
# 최댓값 리스트(인덱스 에러를 방지하기 위해 N+1)
dp = [0]*(N+1)
for i in range(N):
    T[i], P[i] = map(int, input().split())

# 뒤에서부터 검사
for i in range(N-1, -1, -1):
    # 현재 + 다음 상담일수가 N일을 넘어가면 금액 그대로
    if i + T[i] > N:
        dp[i] = dp[i+1]
    else: # 상담일수 갱신 점화식 (이전 상담 금액과 현재 금액 + 다음 상담의 금액 비교)
        dp[i] = max(dp[i+1], P[i] + dp[i + T[i]])

print(dp[0])