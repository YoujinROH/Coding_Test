# -------------------------------------------------
# [문제 1] 약수의 합 
# https://school.programmers.co.kr/learn/courses/30/lessons/12928
# 📘 설명: 정수 n을 입력받아 n의 약수를 모두 더한 값을 리턴하는 함수, solution을 완성하는 문제
# 💡 배운 점: 기본 문제 
# -------------------------------------------------

def solution1(n):
    answer = 0
    for i in range(1,n+1):
        if n%i==0:
            answer += i
    return answer

# -------------------------------------------------
# [문제 2] 정수 내림차순으로 배치하기 
# https://school.programmers.co.kr/learn/courses/30/lessons/12933
# 📘 설명: n의 각 자릿수를 큰것부터 작은 순으로 정렬한 새로운 정수를 리턴하는 함수를 완성하는 문제 
# 💡 배운 점: int형은 len() 불가능. sort 내림차순으로 하려면 reverse=True 적용. list 요소를 join 함수로 합치려면 문자열.join(리스트) 형태로 해야 함. 
# -------------------------------------------------

def solution2(n):
    answer = ''
    tmp_list = []
    for i in range(len(str(n))):
        tmp_list.append(str(n)[i])
    tmp_list.sort(reverse=True)
    answer = int(answer.join(tmp_list))
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
