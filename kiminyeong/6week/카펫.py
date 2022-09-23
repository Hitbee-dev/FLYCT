# [프로그래머스] 카펫
def solution(brown, yellow):
    # 가로가 될 수 있는 최댓값(brown//2-1)부터 최솟값(3)까지 탐색
    for width in range(brown//2-1, 2, -1):
        # 세로는 가로의 값에 의해 결정(최소 3)
        height = brown//2 - width + 2
        # 가로가 세로보다 커야하고, 가로와 세로로 구한 넓이가 brown과 yellow 칸의 합과 같아야 함
        if width >= height and width * height == brown + yellow:
            return [width, height]