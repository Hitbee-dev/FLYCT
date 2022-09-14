# 적록색약
from collections import deque
import sys
input = sys.stdin.readline

n = int(input().rstrip())
# 일반인이 보는 지역
area_gl = [input().rstrip() for _ in range(n)]
# 적록색약인이 보는 지역
area_rg = [raw.replace('G', 'R') for raw in area_gl]

# 방향
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
# 일반인 방문 여부
visited_gl = [[False]*n for _ in range(n)]
# 적록색약인 방문 여부
visited_rg = [[False]*n for _ in range(n)]

def bfs(area, y, x, color, visited):
    q = deque()
    q.append((y, x))
    visited[y][x] = True
    while q:
        cy, cx = q.popleft()
        for i in range(4):
            ny = cy + dy[i]
            nx = cx + dx[i]
            if 0 <= nx < n and 0 <= ny < n and visited[ny][nx] == False and color == area[ny][nx]:
                q.append((ny, nx))
                visited[ny][nx] = True

# 일반인이 보는 구역 수
general = 0
# 적록색약인이 보는 구역 수
weakness = 0
for y in range(n):
    for x in range(n):
        if visited_gl[y][x] == False:
            bfs(area_gl, y, x, area_gl[y][x], visited_gl)
            general += 1
        if visited_rg[y][x] == False:
            bfs(area_rg, y, x, area_rg[y][x], visited_rg)
            weakness += 1

print(general, weakness)