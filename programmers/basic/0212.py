# -------------------------------------------------
# [문제 1] 자릿수 더하기 
# https://school.programmers.co.kr/learn/courses/30/lessons/12931
# 📘 설명: 자연수 N이 주어지면, N의 각 자릿수의 합을 구해서 return 하는 solution 함수를 완성하는 문제 
# 💡 배운 점: 기본 문제 
# -------------------------------------------------

def solution1(n):
    answer = 0
    for i in range(len(str(n))):
        answer += int(str(n)[i])
    return answer

# -------------------------------------------------
# [문제 2] 두 정수 사이의 합 
# https://school.programmers.co.kr/learn/courses/30/lessons/12912
# 📘 설명: 두 정수 a, b가 주어졌을 때 a와 b 사이에 속한 모든 정수의 합을 리턴하는 함수, solution을 완성하는 문제 
# 💡 배운 점: range를 주어진 변수를 활용할 때 꼭 대소 관계 관련해서 꼼꼼히 보기  
# -------------------------------------------------

def solution2(a, b):
    answer = 0
    for i in range(min(a,b), max(a,b)+1):
        answer += i
    return answer
  
# -------------------------------------------------
# [문제 3] 문자열 내 p와 y의 개수 
# https://school.programmers.co.kr/learn/courses/30/lessons/12916
# 📘 설명: s에 'p'의 개수와 'y'의 개수를 비교해 같으면 True, 다르면 False를 return 하는 solution 함수를 완성하는 문제 
# 💡 배운 점: 기본 문제
# -------------------------------------------------

def solution3(s):
    answer = True
    s = s.lower()
    if s.count('p') != s.count('y'):
        return False
    return True
    
# -------------------------------------------------
# [문제 4] 음양 더하기  
# https://school.programmers.co.kr/learn/courses/30/lessons/76501
# 📘 설명: 정수 배열 absolutes와 이 정수들의 부호를 차례대로 담은 불리언 배열 signs가 매개변수로 주어집니다. 실제 정수들의 합을 구하여 return 하도록 solution 함수를 완성하는 문제 
# 💡 배운 점: 기본 문제 
# -------------------------------------------------

def solution4(absolutes, signs):
    answer = 0
    for i in range(len(absolutes)):
        if signs[i] == True:
            answer += absolutes[i]
        else:
            answer -= absolutes[i]
    return answer
  
# -------------------------------------------------
# [문제 5] 없는 숫자 더하기    
# https://school.programmers.co.kr/learn/courses/30/lessons/86051
# 📘 설명: numbers에서 찾을 수 없는 0부터 9까지의 숫자를 모두 찾아 더한 수를 return 하도록 solution 함수를 완성하는 문제  
# 💡 배운 점: 기본 문제 
# -------------------------------------------------

def solution5(numbers):
    answer = 0
    for i in range(10):
        if i not in numbers:
            answer += i
    return answer
  
