# [백준 2667] 단지번호 붙이기
'''
입력
첫 번째 줄에는 지도의 크기 N(정사각형이므로 가로와 세로의 크기는 같으며 5≤N≤25)이 입력되고, 
그 다음 N줄에는 각각 N개의 자료(0혹은 1)가 입력된다.

출력
첫 번째 줄에는 총 단지수를 출력하시오. 
그리고 각 단지내 집의 수를 오름차순으로 정렬하여 한 줄에 하나씩 출력하시오.

예제 입력
7
0110100
0110101
1110101
0000111
0100000
0111110
0111000

예제 출력
3
7
8
9
'''
from collections import deque
import sys
input = sys.stdin.readline

# 지도의 크기
N = int(input().rstrip())
# 지도 정보
maps = [input().rstrip() for _ in range(N)]
# 방문 여부
visited = [[False]*N for _ in range(N)]

def bfs(y, x):
    # 탐색 방향
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]
    # 탐색 주소 큐
    q = deque()
    q.append((y, x))
    visited[y][x] = True
    # 단지 내 집의 수
    house = 1
    while q:
        # 현재 위치
        cy, cx = q.popleft()
        # 네 방향 탐색
        for i in range(4):
            # 다음 인덱스
            ny = cy + dy[i]
            nx = cx + dx[i]
            # 지도 내 범위에서 방문하지 않고 값이 '1'인 위치
            if 0 <= ny < N and 0 <= nx < N and visited[ny][nx] == False and maps[ny][nx] == '1':
                house += 1 # 집 수 카운트
                visited[ny][nx] = True # 방문 처리
                q.append((ny, nx)) # 탐색 주소에 추가
    return house

# 단지 수
group = []
for y in range(N):
    for x in range(N):
        if visited[y][x] == False and maps[y][x] == '1':
            # 단지 내 집 수
            count = bfs(y, x)
            group.append(count)

# 총 단지 수
print(len(group))
# 단지 오름차순 정렬
for g in sorted(group):
    print(g)