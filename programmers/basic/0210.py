# -------------------------------------------------
# [문제 1] 짝수와 홀수 
# https://school.programmers.co.kr/learn/courses/30/lessons/12937
# 📘 설명: 정수 num이 짝수일 경우 "Even"을 반환하고 홀수인 경우 "Odd"를 반환하는 함수, solution을 완성하는 문제
# 💡 배운 점: 기본 문제 
# -------------------------------------------------

def solution1(num):
    answer = ''
    if num%2==0:
        answer='Even'
    else:
        answer='Odd'
    return answer

# -------------------------------------------------
# [문제 2] 평균 구하기  
# https://school.programmers.co.kr/learn/courses/30/lessons/12944
# 📘 설명: 정수를 담고 있는 배열 arr의 평균값을 return하는 함수, solution을 완성하는 문제  
# 💡 배운 점: 기본 문제 (나누기 연산자 /)
# -------------------------------------------------

def solution2(arr):
    answer = 0
    num_sum = 0
    for i in range(len(arr)):
        num_sum += arr[i]
    answer=num_sum/len(arr)
    return answer
  
# -------------------------------------------------
# [문제 3] x만큼 간격이 있는 n개의 숫자 
# https://school.programmers.co.kr/learn/courses/30/lessons/12954
# 📘 설명: 함수 solution은 정수 x와 자연수 n을 입력 받아, x부터 시작해 x씩 증가하는 숫자를 n개 지니는 리스트를 리턴해야 할 때, 제한 조건을 보고 조건을 만족하는 함수, solution을 완성하는 문제 
# 💡 배운 점: range 범위, 값 변화량 꼼꼼히 확인하기 
# -------------------------------------------------

def solution3(x, n):
    answer = []
    answer.append(x)
    tmp = x
    for i in range(n-1):
        tmp += x
        answer.append(tmp)
    return answer
    
# -------------------------------------------------
# [문제 4] 나머지가 1이 되는 수 찾기   
# https://school.programmers.co.kr/learn/courses/30/lessons/87389
# 📘 설명: n을 x로 나눈 나머지가 1이 되도록 하는 가장 작은 자연수 x를 return 하도록 solution 함수를 완성하는 문제 
# 💡 배운 점: 1로 나누면 무슨 수든 나머지가 0이되므로, 2부터 시작해서 조건 확인하기  
# -------------------------------------------------

def solution4(n):
    x=2
    while((n-1)%x!=0):
        x+=1
    return x
  
# -------------------------------------------------
# [문제 5] 문자열을 정수로 바꾸기   
# https://school.programmers.co.kr/learn/courses/30/lessons/12925
# 📘 설명: 문자열 s를 숫자로 변환한 결과를 반환하는 함수, solution을 완성하는 문제  
# 💡 배운 점: 문제 꼼꼼히 잘 읽기. 예시에서 표현되지 않는 조건이 있을 수 있음 
# -------------------------------------------------

def solution5(s):
    answer = 0
    if s[0] == '-':
        for i in range(1, len(s)):
            answer -= int(s[i])*(10**(len(s)-i-1))
    elif s[0] == '+':
         for i in range(1, len(s)):
            answer += int(s[i])*(10**(len(s)-i-1))     
    else:
        for i in range(0, len(s)):
            answer += int(s[i])*(10**(len(s)-i-1))   
    return answer
    return answer
