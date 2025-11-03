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
# [문제 3] 글자 이어 붙여 문자열 만들기 (progress)
# https://school.programmers.co.kr/learn/courses/30/lessons/181920
# 📘 설명: 정수 start_num와 end_num가 주어질 때, start_num부터 end_num까지의 숫자를 차례로 담은 리스트를 return하도록 solution 함수를 완성하는 문제  
# 💡 배운 점: 리스트에 요소 추가할 때 list.append() append 함수 활용하기 
# -------------------------------------------------

def solution(start_num, end_num):
    result = []
    for i in range(start_num, end_num+1):
        result.append(i)
    return result
    
# -------------------------------------------------
# [문제 4] 9로 나눈 나머지 
# https://school.programmers.co.kr/learn/courses/30/lessons/181919
# 📘 설명: 임의의 1,000 보다 작거나 같은 양의 정수 n이 주어질 때 초기값이 n인 콜라츠 수열을 return 하는 solution 함수를 완성하는 문제  
# 💡 배운 점: 어떤 조건일 때까지 반복일 때는 while문 사용하기 
# -------------------------------------------------

def problem_4(n):
    answer = []
    x = n
    while (x!=1):
        if x%2==0:
            answer.append(x)
            x=x//2
        else:
            answer.append(x)
            x=3*x+1
    answer.append(1)    
    return answer

# -------------------------------------------------
# [문제 5] 문자열 여러 번 뒤집기  
# https://school.programmers.co.kr/learn/courses/30/lessons/181918
# 📘 설명: 작업을 마친 후 만들어진 stk를 return 하는 solution 함수를 완성하는 문제 
# 💡 배운 점: 슬라이싱 말고 list.pop()을 사용하면 마지막 원소 제거를 쉽고 메모리 낭비 없이 가능  
# -------------------------------------------------

def problem_5(arr):
    stk = []
    i = 0
    while (i<len(arr)):
        if not stk:
            stk.append(arr[i])
            i+=1
        else:
            if stk[len(stk)-1] < arr[i]:
                stk.append(arr[i])
                i+=1
            else:
                stk=stk[0:len(stk)-1]
    return stk
