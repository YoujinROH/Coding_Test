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
# [문제 3] 하샤드 
# https://school.programmers.co.kr/learn/courses/30/lessons/12947
# 📘 설명: 자연수 x를 입력받아 x가 하샤드 수인지 아닌지 검사하는 함수, solution을 완성하는 문제 
# 💡 배운 점: 기본 문제 int형 str형 잘 바뀌었는지 꼼꼼히 확인할 것 
# -------------------------------------------------

def solution3(x):
    answer = True
    tmp = 0
    for i in range(len(str(x))):
        tmp += int(str(x)[i])
    if x%tmp != 0:
        answer = False
    return answer
    
# -------------------------------------------------
# [문제 4] 정수 제곱근 판별   
# https://school.programmers.co.kr/learn/courses/30/lessons/12934
# 📘 설명: n이 양의 정수 x의 제곱이라면 x+1의 제곱을 리턴하고, n이 양의 정수 x의 제곱이 아니라면 -1을 리턴하는 함수를 완성하는 문제 
# 💡 배운 점: 제곱근은 n ** 0.5 하면 되고, 정수부분? 몫 반환 형태가 아니라 전체 계산으로 소수점으로 나옴(딱 안 떨어지는 연산의 경우) 
# -------------------------------------------------

def solution4(n):
    tmp = n ** 0.5 
    if tmp % 1 != 0:
        return -1
    else:
        return (tmp+1)**2
  
# -------------------------------------------------
# [문제 5] 자연수 뒤집어 배열로 만들기    
# https://school.programmers.co.kr/learn/courses/30/lessons/12932
# 📘 설명: 자연수 n을 뒤집어 각 자리 숫자를 원소로 가지는 배열 형태로 리턴하는 문제  
# 💡 배운 점: 반복문을 step을 -1로 하고 싶으면 꼭 stop을 명시해주기 
# -------------------------------------------------

def solution5(n):
    answer = []
    for i in range(len(str(n))-1,-1,-1):
        answer.append(int(str(n)[i]))
    return answer
    
