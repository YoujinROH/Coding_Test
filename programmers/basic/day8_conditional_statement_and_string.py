# -------------------------------------------------
# [문제 1] 간단한 논리 연산
# https://school.programmers.co.kr/learn/courses/30/lessons/181917
# 📘 설명: boolean 변수 x1, x2, x3, x4가 매개변수로 주어질 때, 다음의 식의 true/false를 return 하는 solution 함수를 작성하는 문제 
# 💡 배운 점: boolean 선언할 때, True, False로 선언 혹은 0, 1도 가능 
# -------------------------------------------------

def problem_1(x1, x2, x3, x4):
    answer = True
    if x1==True or x2==True:
        if x3==True or x4==True:
            answer=True
        else:
            answer=False
    else:
        answer=False
    return answer

# -------------------------------------------------
# [문제 2] 주사위 게임 3 
# https://school.programmers.co.kr/learn/courses/30/lessons/181916
# 📘 설명: 네 주사위를 굴렸을 때 나온 숫자가 정수 매개변수 a, b, c, d로 주어질 때, 얻는 점수를 return 하는 solution 함수를 작성하는 문제 
# 💡 배운 점: 딕셔너리 접근법 복습하기
# -------------------------------------------------

def problem_2(a, b, c, d):
    dice_num = [a, b, c, d]
    dice_count = {}
    
    for i in dice_num:
        if i in dice_count:
            dice_count[i] += 1
        else:
            dice_count[i] = 1
    
    keys = list(dice_count.keys())
    values = list(dice_count.values())
    
    if len(dice_count) == 1:
        p = keys[0]
        return 1111 * p
    
    elif len(dice_count) == 2:
        if 3 in values:
            p = keys[values.index(3)]
            q = keys[values.index(1)]
            return (10 * p + q) ** 2
        else:
            p, q = keys
            return (p + q) * abs(p - q)
    
    elif len(dice_count) == 3:
        p = keys[values.index(2)]
        q, r = [k for k in keys if k != p]
        return q * r
    
    else:
        return min(dice_num)
  
# -------------------------------------------------
# [문제 3] 글자 이어 붙여 문자열 만들기
# https://school.programmers.co.kr/learn/courses/30/lessons/181915
# 📘 설명: my_string의 index_list의 원소들에 해당하는 인덱스의 글자들을 순서대로 이어 붙인 문자열을 return 하는 solution 함수를 작성하는 문제 
# 💡 배운 점: for문 활용할 때, out of range나 인덱스에 넘버말고 문자 들어가는 거 주의하기  
# -------------------------------------------------

def problem_3(my_string, index_list):
    answer = ''
    my_string=list(my_string)
    for i in range(len(index_list)):
        answer+=my_string[index_list[i]]
    return answer
    
# -------------------------------------------------
# [문제 4] 9로 나눈 나머지 
# https://school.programmers.co.kr/learn/courses/30/lessons/181914
# 📘 설명: 음이 아닌 정수가 문자열 number로 주어질 때, 이 정수를 9로 나눈 나머지를 return 하는 solution 함수를 작성하는 문제   
# 💡 배운 점: input의 type 잘 확인하기. string인지 int인지 
# -------------------------------------------------

def problem_4(number):
    answer = 0
    answer = int(number)%9
    return answer

# -------------------------------------------------
# [문제 5] 문자열 여러 번 뒤집기  
# https://school.programmers.co.kr/learn/courses/30/lessons/181913
# 📘 설명: my_string에 queries의 명령을 순서대로 처리한 후의 문자열을 return 하는 solution 함수를 작성하는 문제  
# 💡 배운 점: for i in range(len(a)-1, -1, -1), start, stop, step이고 -1 step으로 0까지 가고 싶으면 하나 더 간 -1을 stop으로 설정해주어야함 
# -------------------------------------------------

def problem_5(my_string, queries): 
    answer = ''
    answer = my_string
    for s,e in queries:
        tmp_in = ''
        tmp_out = ''
        tmp_in = answer[s:e+1]
        for i in range(len(tmp_in)-1,-1,-1):
            tmp_out+=tmp_in[i]
        answer = answer[0:s]+tmp_out+answer[e+1:]
    return answer
