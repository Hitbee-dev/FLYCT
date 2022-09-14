# [프로그래머스] 최댓값과 최솟값
'''
문자열 s에는 공백으로 구분된 숫자들이 저장되어 있습니다. 
str에 나타나는 숫자 중 최소값과 최대값을 찾아 이를 "(최소값) (최대값)"형태의 문자열을 반환하는 함수, solution을 완성하세요.
'''
def solution(s):
    # 공백으로 구분한 리스트
    nums = sorted(list(map(int, s.split())))
    # 최솟값
    min_num = str(nums[0])
    # 최댓값
    max_num = str(nums[-1])
    # 공백으로 구분한 문자열로 리턴
    return min_num+ ' ' + max_num