# [백준 1966] 프린터 큐
'''
조건
1. 현재 Queue의 가장 앞에 있는 문서의 ‘중요도’를 확인한다.
2. 나머지 문서들 중 현재 문서보다 중요도가 높은 문서가 하나라도 있다면, 
   이 문서를 인쇄하지 않고 Queue의 가장 뒤에 재배치 한다. 그렇지 않다면 바로 인쇄를 한다.

예제 입력
3
1 0
5
4 2
1 2 3 4
6 0
1 1 9 1 1 1

예제 출력
1
2
5
'''
from collections import deque
import sys
input = sys.stdin.readline

# 테스트케이스
T = int(input().rstrip())

for _ in range(T):
    # 문서의 개수 N과 몇 번째로 출력될지 궁금한 문서의 위치 M
    N, M = map(int, input().split())
    # N개 문서의 중요도
    importance = [(i, v) for i, v in enumerate(map(int, input().split()))]
    # 몇 번째로 출력될지 궁금한 문서
    question = importance[M]
    # 프린터 큐
    queue = deque(importance)
    while queue:
        # 현재 문서
        paper = queue.popleft()
        # 나머지 문서들 중 현재 문서의 중요도보다 큰 문서가 하나라도 있으면 queue 뒤로 보내기
        for other in queue:
            if other[1] > paper[1]:
                queue.append(paper)
                break
        # 현재 문서가 궁금한 문서이면서 queue에 없을 때 출력 순서
        if paper == question and paper not in queue:
            print(len(importance) - len(queue))
            break