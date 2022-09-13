# [백준 2621] 카드게임
'''
문제
<점수를 정하는 규칙>

1. 카드 5장이 모두 같은 색이면서 숫자가 연속적일 때, 점수는 가장 높은 숫자에 900을 더한다. 예를 들어, 카드가 Y4, Y3, Y2, Y5, Y6 일 때 점수는 906(=6+900)점이다.
2. 카드 5장 중 4장의 숫자가 같을 때 점수는 같은 숫자에 800을 더한다. 예를 들어, 카드가 B3, R3, B7, Y3, G3 일 때 점수는 803(=3+800)점이다.
3. 카드 5장 중 3장의 숫자가 같고 나머지 2장도 숫자가 같을 때 점수는 3장이 같은 숫자에 10을 곱하고 2장이 같은 숫자를 더한 다음 700을 더한다. 예를 들어, 카드가 R5, Y5, G7, B5, Y7 일 때 점수는 757(=5x10+7+700)점이다.
4. 5장의 카드 색깔이 모두 같을 때 점수는 가장 높은 숫자에 600을 더한다. 예를 들어, 카드가 Y3, Y4, Y8, Y6, Y7 일 때 점수는 608(=8+600)점이다.
5. 카드 5장의 숫자가 연속적일 때 점수는 가장 높은 숫자에 500을 더한다. 예를 들어 R7, R8, G9, Y6, B5 일 때 점수는 509(=9+500)점이다.
6. 카드 5장 중 3장의 숫자가 같을 때 점수는 같은 숫자에 400을 더한다. 예를 들어 R7, Y7, R2, G7, R5 일 때 점수는 407(=7+400)점이다.
7. 카드 5장 중 2장의 숫자가 같고 또 다른 2장의 숫자가 같을 때 점수는 같은 숫자 중 큰 숫자에 10을 곱하고 같은 숫자 중 작은 숫자를 더한 다음 300을 더한다. 예를 들어, R5, Y5, Y4, G9, B4 일 때 점수는 354(=5X10+4+300)점이다.
8. 카드 5장 중 2장의 숫자가 같을 때 점수는 같은 숫자에 200을 더한다. 예를 들어, R5, Y2, B5, B3, G4 일 때 점수는 205(=5+200)점이다.
9. 위의 어떤 경우에도 해당하지 않을 때 점수는 가장 큰 숫자에 100을 더한다. 예를 들어, R1, R2, B4, B8, Y5 일 때 점수는 108(=8+100)점이다.

입력으로 카드 5장이 주어질 때, 카드 게임의 점수를 구하는 프로그램을 작성하시오. 두 가지 이상의 규칙을 적용할 수 있는 경우에는 가장 높은 점수가 카드 게임의 점수이다.

입력
B 3
B 7
R 1
B 2
Y 7

출력
207
'''
import sys
# 카드 색
colors = {}
# 카드 숫자
numbers = {}
for i in range(5):
    color, number = sys.stdin.readline().split()
    if color in colors:
        colors[color] += 1
    else:
        colors[color] = 1
    if int(number) in numbers:
        numbers[int(number)] += 1
    else:
        numbers[int(number)] = 1

# 숫자들이 연속되어 있는지 확인
isSequence = True
sorted_numbers = sorted(list(numbers.keys()))
for i, number in enumerate(sorted_numbers, start=sorted_numbers[0]):
    if len(sorted_numbers) != 5 or number != i:
        isSequence = False
        break

# 같은 숫자 개수에 따른 필터링 함수
def filtered_numbers(i):
    filtered = []
    for number in filter(lambda x:x[1]==i, numbers.items()):
        filtered.append(number[0])
    return filtered

# 카드 게임 점수
score = 0
# 카드 5장이 모두 같은 색이고 숫자들이 연속적이면, 가장 높은 숫자에 900 더함 
if 5 in colors.values() and isSequence:
    score += sorted_numbers[-1] + 900
# 카드 5장 중 4장의 숫자가 같으면, 점수는 같은 숫자에 800을 더함
elif 4 in numbers.values():
    score += filtered_numbers(4)[0] + 800
# 카드 5장 중 3장의 숫자가 같고 나머지 2장도 숫자가 같을 때 점수는 3장이 같은 숫자에 10을 곱하고 2장이 같은 숫자를 더한 다음 700을 더한다.
elif 3 in numbers.values() and 2 in numbers.values():
    score += filtered_numbers(3)[0]*10 + filtered_numbers(2)[0] + 700
# 5장의 카드 색깔이 모두 같을 때 점수는 가장 높은 숫자에 600을 더한다.
elif 5 in colors.values():
    score += sorted_numbers[-1] + 600
# 카드 5장의 숫자가 연속적일 때 점수는 가장 높은 숫자에 500을 더한다.
elif isSequence:
    score += sorted_numbers[-1] + 500
# 카드 5장 중 3장의 숫자가 같을 때 점수는 같은 숫자에 400을 더한다.
elif 3 in numbers.values():
    score += filtered_numbers(3)[0] + 400
# 카드 5장 중 2장의 숫자가 같고 또 다른 2장의 숫자가 같을 때 점수는 같은 숫자 중 큰 숫자에 10을 곱하고 같은 숫자 중 작은 숫자를 더한 다음 300을 더한다.
elif len(filtered_numbers(2)) == 2:
    filtered = sorted(filtered_numbers(2), reverse=True)
    score += filtered[0]*10 + filtered[1] + 300
# 카드 5장 중 2장의 숫자가 같을 때 점수는 같은 숫자에 200을 더한다.
elif 2 in numbers.values():
    score += filtered_numbers(2)[0] + 200
# 위의 어떤 경우에도 해당하지 않을 때 점수는 가장 큰 숫자에 100을 더한다.
else:
    score += sorted_numbers[-1] + 100

print(score)