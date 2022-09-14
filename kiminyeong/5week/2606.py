# [백준 2606] 바이러스
'''
문제
어느 날 1번 컴퓨터가 웜 바이러스에 걸렸다. 
컴퓨터의 수와 네트워크 상에서 서로 연결되어 있는 정보가 주어질 때, 
1번 컴퓨터를 통해 웜 바이러스에 걸리게 되는 컴퓨터의 수를 출력하는 프로그램을 작성하시오.

입력
7
6
1 2
2 3
1 5
5 2
5 6
4 7

출력
4
'''
from collections import deque
import sys
input = sys.stdin.readline

# 컴퓨터 수
n = int(input().rstrip())
# 네트워크 상에서 연결된 컴퓨터 수
m = int(input().rstrip())
computers = [tuple(map(int, input().split())) for _ in range(m)]
# 컴퓨터 방문 여부
visited = [0]*n

# 1에서 시작하는 컴퓨터 쌍
q = deque(filter(lambda x:x[0]==1 or x[1]==1, computers))
while q:
    (s, e) = q.popleft()
    computers.remove((s, e))
    # 방문한 컴퓨터 1로 변경
    visited[s-1] = 1
    visited[e-1] = 1
    # 다음 연결된 컴퓨터 쌍을 q에 추가(양방향 검사)
    for data in filter(lambda x:(x[0]==s or x[0]==e or x[1]==s or x[1]==e), computers):
        if data not in q:
            q.append(data)
        
# 방문한 컴퓨터 카운트
count = visited.count(1)
if count > 0:
    # 1번 컴퓨터 제외
    count -= 1 
print(count)