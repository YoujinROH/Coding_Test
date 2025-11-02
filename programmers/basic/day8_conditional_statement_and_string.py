# -------------------------------------------------
# [문제 1] 간단한 논리 연산
# https://school.programmers.co.kr/learn/courses/30/lessons/181917
# 📘 설명: boolean 변수 x1, x2, x3, x4가 매개변수로 주어질 때, 다음의 식의 true/false를 return 하는 solution 함수를 작성하는 문제 
# 💡 boolean 선언할 때, True, False로 선언 혹은 0, 1도 가능 
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
# [문제 2] 주사위 게임 3 (progress)
# https://school.programmers.co.kr/learn/courses/30/lessons/181921
# 📘 설명: 정수 l과 r이 주어졌을 때, l 이상 r이하의 정수 중에서 숫자 "0"과 "5"로만 이루어진 모든 정수를 오름차순으로 저장한 배열을 return 하는 solution 함수를 완성하는 문제 
# 💡 배운 점: if all(ch in ['0', '5'] for ch in str(i)) 이런식으로도 접근 가능, 또한 if len(result)==0 도 if not result로 변경 가능 
# -------------------------------------------------

def problem_2(l, r):
    result = [] 
    for i in range(l, r+1):
        for j in range(len(str(i))):
            if str(i)[j]=="0" or str(i)[j]=="5":
                if j==len(str(i))-1:
                    result.append(i)  
            else:
                j=len(str(i))-1
                break
    if len(result)==0:
        result.append(-1)
    return result
  
# -------------------------------------------------
# [문제 3] 글자 이어 붙여 문자열 만들기 
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
