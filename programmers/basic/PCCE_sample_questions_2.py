# -------------------------------------------------
# [문제 1] 출력
# https://school.programmers.co.kr/learn/courses/30/lessons/250133
# 📘 설명: 주어진 초기 코드는 변수에 데이터를 저장하고 출력하는 코드입니다. 아래와 같이 출력되도록 빈칸을 채워 코드를 완성하는 문제  
# 💡 배운 점: 문자열에 따옴표 붙이는 것만 기억하면 기본 문제   
# -------------------------------------------------

string_msg = "Spring is beginning"

int_val = 3

string_val = "3"

print(string_msg)
print(int_val + 10)
print(string_val + "10")

# -------------------------------------------------
# [문제 2] 피타고라스의 정리
# https://school.programmers.co.kr/learn/courses/30/lessons/250132
# 📘 설명: 직각삼각형의 한 변의 길이를 나타내는 정수 a와 빗변의 길이를 나타내는 정수 c가 주어질 때, 다른 한 변의 길이의 제곱, b_square 을 출력하도록 한 줄을 수정해 코드를 완성하는 문제 
# 💡 배운 점: 기본 문제   
# -------------------------------------------------

a = int(input())
c = int(input())

b_square = c**2 - a**2
print(b_square)
  
# -------------------------------------------------
# [문제 3] 나이 계산  
# https://school.programmers.co.kr/learn/courses/30/lessons/250131
# 📘 설명: 출생 연도를 나타내는 정수 year와 구하려는 나이의 종류를 나타내는 문자열 age_type이 주어질 때 2030년에 몇 살인지 출력하도록 빈칸을 채워 코드를 완성하는 문제  
# 💡 배운 점: 기본 문제. 그냥 사용자 입력 받을 때, a = input(), a = int(input()) 이 형식이나 잊지 않고 기억해두기  
# -------------------------------------------------

year = int(input())
age_type = input()

if age_type == "Korea":
    answer = 2030 - year + 1
elif age_type == "Year":
    answer = 2030 - year

print(answer)
    
# -------------------------------------------------
# [문제 4] 저축  
# https://school.programmers.co.kr/learn/courses/30/lessons/250130
# 📘 설명: 첫 달에 저축하는 금액을 나타내는 정수 start, 두 번째 달 부터 70만 원 이상 모일 때까지 매월 저축하는 금액을 나타내는 정수 before, 100만 원 이상 모일 때 까지 매월 저축하는 금액을 나타내는 정수 after가 주어질 때, 100만 원 이상을 모을 때까지 걸리는 개월 수를 출력하도록 빈칸을 채워 코드를 완성하는 문제 
# 💡 배운 점: 기본 문제 
# -------------------------------------------------

start = int(input())
before = int(input())
after = int(input())

money = start
month = 1
while money < 70:
    money += before
    month += 1
while money < 100:
    money += after
    month += 1
print(month)
  
# -------------------------------------------------
# [문제 5] 산책  
# https://school.programmers.co.kr/learn/courses/30/lessons/250129
# 📘 설명: 산책루트가 담긴 문자열 route가 주어질 때, 도착점의 위치를 return하도록 빈칸을 채워 solution함수를 완성하는 문제  
# 💡 배운 점: 문자열 항상 따옴표 유의하기 
# -------------------------------------------------

def solution(route):
    east = 0
    north = 0
    for i in route:
        if i == "N":
            north += 1
        elif i == "S" :
            north -= 1
        elif i == "E" :
            east += 1
        elif i == "W":
            east -= 1

    return [east, north]

# -------------------------------------------------
# [문제 6] 가채점 
# https://school.programmers.co.kr/learn/courses/30/lessons/250128
# 📘 설명: 성적을 문의하려는 학생들의 번호가 담긴 정수 리스트 numbers와 가채점한 점수가 성적을 문의하려는 학생 순서대로 담긴 정수 리스트 our_score, 실제 성적이 번호 순서대로 담긴 정수 리스트 score_list가 주어지고, solution 함수는 가채점한 점수가 실제 성적과 동일하다면 "Same"을, 다르다면 "Different"를 순서대로 리스트에 담아 return하는 함수일 때, solution 함수가 올바르게 작동하도록 한 줄을 수정하는 문제 
# 💡 배운 점: 항상 인덱스 번호 맞는지 확인하기 
# -------------------------------------------------

def solution(numbers, our_score, score_list):
    answer = []
    for i in range(len(numbers)):
        if our_score[i] == score_list[numbers[i]-1]:
            answer.append("Same")
        else:
            answer.append("Different")
    
    return answer

# -------------------------------------------------
# [문제 7] 가습기   
# https://school.programmers.co.kr/learn/courses/30/lessons/250127
# 📘 설명: 상우가 설정한 가습기의 모드를 나타낸 문자열 mode_type, 현재 공기 중 습도를 나타낸 정수 humidity, 설정값을 나타낸 정수 val_set이 주어질 때 현재 가습기가 몇 단계로 작동 중인지 return하도록 빈칸을 채워 solution 함수를 완성하는 문제   
# 💡 배운 점: 기본 문제  
# -------------------------------------------------

def func1(humidity, val_set):
    if humidity < val_set:
        return 3
    return 1

def func2(humidity):
    if humidity >= 50:
        return 0
    elif humidity >= 40:
        return 1
    elif humidity >= 30:
        return 2
    elif humidity >= 20:
        return 3
    elif humidity >= 10:
        return 4
    else:
        return 5

def func3(humidity, val_set):
    if humidity < val_set:
        return 1
    return 0

def solution(mode_type, humidity, val_set):
    answer = 0
    if mode_type == "auto":
        answer = func2(humidity)
    elif mode_type == "target":
        answer = func1(humidity, val_set)
    elif mode_type == "minimum":
        answer = func3(humidity, val_set)
    return answer

# -------------------------------------------------
# [문제 8] 창고 정리  
# https://school.programmers.co.kr/learn/courses/30/lessons/250126
# 📘 설명: 주어진 solution 함수는 정리되기 전 창고의 물건 이름이 담긴 문자열 리스트 storage와 각 물건의 개수가 담긴 정수 리스트 num이 주어질 때, 정리된 창고에서 개수가 가장 많은 물건의 이름을 return 하는 함수라면, 그 solution 함수가 올바르게 작동하도록 한 줄을 수정하는 문제
# 💡 배운 점: index() 함수는 함수 내부의 값이 제일 먼저 등장하는 인덱스를 반환함. ex) a = ['apple', 'banana', 'cherry'], a.index('banana') -> 1
# -------------------------------------------------

def solution(storage, num):
    clean_storage = []
    clean_num = []
    for i in range(len(storage)):
        if storage[i] in clean_storage:
            pos = clean_storage.index(storage[i])
            clean_num[pos] += num[i]
        else:
            clean_storage.append(storage[i])
            clean_num.append(num[i])
            
    # 아래 코드에는 틀린 부분이 없습니다.
            
    max_num = max(clean_num)
    answer = clean_storage[clean_num.index(max_num)]
    return answer

# -------------------------------------------------
# [문제 9] 이웃한 칸   
# https://school.programmers.co.kr/learn/courses/30/lessons/250125
# 📘 설명: 보드의 각 칸에 칠해진 색깔 이름이 담긴 이차원 문자열 리스트 board와 고른 칸의 위치를 나타내는 두 정수 h, w가 주어질 때 board[h][w]와 이웃한 칸들 중 같은 색으로 칠해져 있는 칸의 개수를 return 하도록 solution 함수를 완성하는 문제   
# 💡 배운 점: 의사 코드 주어지는 경우 적극 활용. 방향 문제는 항상 y좌표 = [0, 1, -1, 0], x좌표 = [1, 0, 0, -1] 활용하기   
# -------------------------------------------------

def solution(board, h, w):
    count = 0
    n = len(board)
    
    dh = [0, 1, -1, 0]
    dw = [1, 0, 0, -1]
    
    for i in range(4):
        h_check = h + dh[i]
        w_check = w + dw[i]
        if (h_check >= 0 and h_check < n) and (w_check >= 0 and w_check < n):
            if board[h][w] == board[h_check][w_check]:
                count += 1
    return count

# -------------------------------------------------
# [문제 10] 데이터 분석   
# https://school.programmers.co.kr/learn/courses/30/lessons/250121
# 📘 설명: data에서 ext 값이 val_ext보다 작은 데이터만 뽑은 후, sort_by에 해당하는 값을 기준으로 오름차순으로 정렬하여 return 하도록 solution 함수를 완성하는 문제 
# 💡 배운 점: 문자열 조건이 맞는지 해당하는 조건문을 중복적으로 사용할 때는 index 딕셔너리 활용하는 것이 빠름. 리스트.sort(key=lambda x: x[조건])은 꼭 좀 기억하기 
# -------------------------------------------------

def solution(data, ext, val_ext, sort_by):
    index_num = {"code":0, "date":1, "maximum":2, "remain":3}
    filtered = [d for d in data if d[index_num[ext]]<val_ext]
    filtered.sort(key=lambda x: x[index_num[sort_by]])
    return filtered
