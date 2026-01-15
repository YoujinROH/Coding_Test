# -------------------------------------------------
# [문제 1] 문자 출력
# https://school.programmers.co.kr/learn/courses/30/lessons/340207
# 📘 설명: 주어진 코드는 변수에 데이터를 저장하고 출력하는 코드입니다. 아래와 같이 출력되도록 빈칸을 채워 코드를 완성하는 문제 
# 💡 배운 점: 문자열 출력 도중 한 줄 띄고 출력하고 싶으면 \n 사용하기  
# -------------------------------------------------

message = "Let's go!"

print("3\n2\n1")
print(message)

# -------------------------------------------------
# [문제 2] 각도 합치기
# https://school.programmers.co.kr/learn/courses/30/lessons/340206
# 📘 설명: 각도를 나타내는 두 정수 angle1과 angle2가 주어질 때, 이 두 각의 합을 0도 이상 360도 미만으로 출력하는 코드가 올바르게 작동하도록 한 줄을 수정하는 문제 
# 💡 배운 점: 각도나 어떤 기준점 뒤로부터 다시 0이되는? 그런 수의 경우는 % 나머지 연산자 활용하기  
# -------------------------------------------------

angle1 = int(input())
angle2 = int(input())

sum_angle = angle1 + angle2
print(sum_angle%360)
  
# -------------------------------------------------
# [문제 3] 수 나누기 
# https://school.programmers.co.kr/learn/courses/30/lessons/340205
# 📘 설명: 2자리 이상의 정수 number가 있을 때, 이 수를 2자리씩 자른 뒤, 자른 수를 모두 더해서 그 합을 출력하는 코드가 올바르게 작동하도록 한 줄을 수정하는 문제 
# 💡 배운 점: int는 len()함수 적용이 안되므로, str()을 사용해서 변환한 뒤 사용할 수 있도록 하기 
# -------------------------------------------------

number = int(input())

answer = 0

for i in range(len(str(number))//2):
    answer += number % 100
    number //= 100

print(answer)
    
# -------------------------------------------------
# [문제 4] 병과분류 
# https://school.programmers.co.kr/learn/courses/30/lessons/340204
# 📘 설명: 환자의 코드를 나타내는 문자열 code를 입력받아 위 표에 맞는 병과를 출력하도록 빈칸을 채워 코드를 완성하는 문제 
# 💡 배운 점: 문자열의 경우는 항상 큰따옴표 넣어주기! 
# -------------------------------------------------

code = input()
last_four_words = code[-4:]

if last_four_words == "_eye":
    print("Ophthalmologyc")
elif last_four_words == "head":
    print("Neurosurgery")
elif last_four_words == "infl":
    print("Orthopedics")
elif last_four_words == "skin":
    print("Dermatology")
else:
    print("direct recommendation")
  
# -------------------------------------------------
# [문제 5] 심폐소생술 
# https://school.programmers.co.kr/learn/courses/30/lessons/340203
# 📘 설명: 주어진 solution 함수는 심폐소생술을 하는 방법의 순서가 담긴 문자열들이 무작위 순서로 담긴 리스트 cpr이 주어질 때 각각의 방법이 몇 번째 단계인지 순서대로 담아 return하는 함수가 있을 때, solution 함수가 올바르게 작동하도록 빈칸을 채워 solution 함수를 완성하는 문제 
# 💡 배운 점: 항상 반복문에서 range 길이를 뭘 기준으로 갈 지 생각하고 하기
# -------------------------------------------------

def solution(cpr):
    answer = []
    basic_order = ["check", "call", "pressure", "respiration", "repeat"]
    for action in cpr:
        for i in range(len(basic_order)):
            if action == basic_order[i]:
                answer.append(i+1)
    return answer

# -------------------------------------------------
# [문제 6] 물 부족
# https://school.programmers.co.kr/learn/courses/30/lessons/340202
# 📘 설명: 현재 저수지에 저장된 물의 양을 나타내는 정수 storage와 지난 달 물 사용량을 나타내는 정수 usage, 월별 물 사용량이 전 달 대비 어떻게 변하는지 저장된 정수 리스트 change가 주어질 때 몇 달 뒤 물이 부족해지는지 return 하도록 solution 함수를 작성하는 문제 
# 💡 배운 점: 이번 사용량과 다음 사용량 같은 것을 구하는 문제의 경우, 다음사용량 = 이번사용량 * (1 + 변화퍼센트)로 사용량에 퍼센트 계산을 곱셈으로 해주는 것임 덧셈이 아님!! 
# -------------------------------------------------

def solution(storage, usage, change):
    total_usage = 0
    for i in range(len(change)):
        usage = int(usage * (1 + change[i]/100))
        total_usage += usage
        if total_usage > storage:
            return i
    
    return -1

# -------------------------------------------------
# [문제 7] 버스  
# https://school.programmers.co.kr/learn/courses/30/lessons/340201
# 📘 설명: 주어진 solution함수는 버스의 좌석 개수 seat, 기점에서 출발한 버스가 순서대로 방문한 정거장에서 승객이 승/하차한 정보를 담은 2차원 문자열 리스트 passengers가 주어질 때, 버스에 남아있는 좌석의 개수를 return 하는 함수가 있다면 solution 함수가 올바르게 작동하도록 빈칸을 채워 solution함수를 완성하는 문제  
# 💡 배운 점: 종이 필기 말고 타이핑으로 필기하는 연습 기르기 
# -------------------------------------------------

def func1(num):
    if 0 > num:
        return 0
    else:
        return num

def func2(num):
    if num > 0:
        return 0
    else:
        return num

def func3(station):
    num = 0
    for people in station:
        if people == "Off":
            num += 1
    return num

def func4(station):
    num = 0
    for people in station:
        if people == "On":
            num += 1
    return num


def solution(seat, passengers):
    num_passenger = 0
    for station in passengers:
        num_passenger += func4(station)

        num_passenger -= func3(station)

    answer = func1(seat - num_passenger)

    return answer

# -------------------------------------------------
# [문제 8] 닉네임 규칙 
# https://school.programmers.co.kr/learn/courses/30/lessons/340200
# 📘 설명: 주어진 solution 함수는 사용할 수 없는 닉네임 nickname을 받아 사용할 수 있는 닉네임으로 바꿔주는 함수일 때, solution 함수가 올바르게 작동하도록 한 줄을 수정하는 문제
# 💡 배운 점: 한 줄만 바꿔야하는데 조건문 -> 조건문 & 반복문 모두 필요한 조건으로 수정해야한다면 while문 사용하기 
# -------------------------------------------------

def solution(nickname):
    answer = ""
    for letter in nickname:
        if letter == "l":
            answer += "I"
        elif letter == "w":
            answer += "vv"
        elif letter == "W":
            answer += "VV"
        elif letter == "O":
            answer += "0"
        else:
            answer += letter
    while(len(answer) < 4):
        answer += "o"
    if len(answer) > 8:
        answer = answer[:8]
    return answer

# -------------------------------------------------
# [문제 9] 지폐 접기  
# https://school.programmers.co.kr/learn/courses/30/lessons/340199
# 📘 설명: 지갑의 가로, 세로 크기를 담은 정수 리스트 wallet과 지폐의 가로, 세로 크기를 담은 정수 리스트 bill가 주어질 때, 지갑에 넣기 위해서 지폐를 최소 몇 번 접어야 하는지 return하도록 solution함수를 완성하는 문제  
# 💡 배운 점: 조건문 사용할 때, 항상 and 조건이 맞을 지 or 조건이 맞을 지 잘 생각하기 
# -------------------------------------------------

def solution(wallet, bill): 
    answer = 0
    while(max(wallet) < max(bill) or min(wallet) < min(bill)):
        answer += 1
        bill = [max(bill)//2,min(bill)]
    return answer

# -------------------------------------------------
# [문제 10] 공원  
# https://school.programmers.co.kr/learn/courses/30/lessons/340198
# 📘 설명: 지민이가 가진 돗자리들의 한 변의 길이들이 담긴 정수 리스트 mats, 현재 공원의 자리 배치도를 의미하는 2차원 문자열 리스트 park가 주어질 때 지민이가 깔 수 있는 가장 큰 돗자리의 한 변 길이를 return 하도록 solution 함수를 완성하는 문제
# 💡 배운 점: nxn이 가능한지 찾는 문제는 한 덩어리로 True False를 판단하는게 나음 
# -------------------------------------------------

def solution(mats, park):
    mats.sort(reverse=True)
    n, m = len(park), len(park[0])

    for jimin_mat in mats:
        for i in range(n - jimin_mat + 1):
            for j in range(m - jimin_mat + 1):
                can_put = True
                for x in range(jimin_mat):
                    for y in range(jimin_mat):
                        if park[i + x][j + y] != "-1":
                            can_put = False
                            break
                    if not can_put:
                        break

                if can_put:
                    return jimin_mat

    return -1
