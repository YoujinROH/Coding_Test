# -------------------------------------------------
# [문제 1] n의 배수
# https://school.programmers.co.kr/learn/courses/30/lessons/181937
# 📘 설명: 정수 num과 n이 매개 변수로 주어질 때, num이 n의 배수이면 1을 return n의 배수가 아니라면 0을 return하도록 solution 함수를 완성하는 문제
# 💡 배운 점: 배수 계산에는 % 나머지 연산자 활용
# -------------------------------------------------

def problem_1(num, n):
    answer = 0
    if num%n==0:
        answer=1
    else:
        answer=0
    return answer

# -------------------------------------------------
# [문제 2] 공배수
# https://school.programmers.co.kr/learn/courses/30/lessons/181936
# 📘 설명: 정수 number와 n, m이 주어질 때, number가 n의 배수이면서 m의 배수이면 1을 아니라면 0을 return하도록 solution 함수를 완성하는 문제
# 💡 배운 점: A 이면서 B인 경우는 and 연산자 
# -------------------------------------------------

def problem_2(number, n, m):
    answer = 0
    if number%n==0 and number%m==0:
        answer=1
    else:
        answer=0
    return answer
  
# -------------------------------------------------
# [문제 3] 홀짝에 따라 다른 값 반환하기
# https://school.programmers.co.kr/learn/courses/30/lessons/181935
# 📘 설명: 양의 정수 n이 매개변수로 주어질 때, n이 홀수라면 n 이하의 홀수인 모든 양의 정수의 합을 return 하고 n이 짝수라면 n 이하의 짝수인 모든 양의 정수의 제곱의 합을 return 하는 solution 함수를 작성하는 문제
# 💡 배운 점: 몫 연산자는 //
# -------------------------------------------------

def problem_3(n):
    answer = 0
    if n%2==1:
        for i in range((n//2)+1):
            answer+=n-(2*i)
    else:
        for i in range((n//2)+1):
            answer+=(n-(2*i))**2
    return answer

# -------------------------------------------------
# [문제 4] 조건 문자열
# https://school.programmers.co.kr/learn/courses/30/lessons/181934
# 📘 설명: 두 문자열 ineq와 eq가 주어질 때, ineq는 "<"와 ">"중 하나고, eq는 "="와 "!"중 하나인 경우 두 정수 n과 m이 주어질 때, n과 m이 ineq와 eq의 조건에 맞으면 1을 아니면 0을 return하도록 solution 함수를 완성하는 문제
# 💡 배운 점: 그냥 조건문으로 문제 풀기 
# -------------------------------------------------

def problem_4(ineq, eq, n, m):
    answer = 0
    if ineq=="<":
        if eq=="=":
            if n<=m:
                answer=1
            else:
                answer=0
        else:
            if n<m:
                answer=1
            else:
                answer=0
    else:
        if eq=="=":
            if n>=m:
                answer=1
            else:
                answer=0
        else:
            if n>m:
                answer=1
            else:
                answer=0
    return answer

# -------------------------------------------------
# [문제 5] flag에 따라 다른 값 반환하기
# https://school.programmers.co.kr/learn/courses/30/lessons/181933
# 📘 설명: 두 정수 a, b와 boolean 변수 flag가 매개변수로 주어질 때, flag가 true면 a + b를 false면 a - b를 return 하는 solution 함수를 작성하는 문제
# 💡 배운 점: True는 1 False는 0 
# -------------------------------------------------

def problem_5(a, b, flag):
    answer = 0
    if flag==1:
        answer=a+b
    else:
        answer=a-b
    return answer
