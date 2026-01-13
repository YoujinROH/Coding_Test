# -------------------------------------------------
# [문제 1] 커피 심부름
# https://school.programmers.co.kr/learn/courses/30/lessons/181837
# 📘 설명: 각 직원이 적은 메뉴가 문자열 배열 order로 주어질 때, 카페에서 결제하게 될 금액을 return 하는 solution 함수를 작성하는 문제 
# 💡 배운 점: if in을 써서 문자열을 확인할때, 리스트 요소가 아니라 정말 문자열을 확인하고 싶으면 꼭 따옴표 포함해서 문자열로 제대로 표현하기 
# -------------------------------------------------

def problem_1(order):
    answer = 0
    for i in range(len(order)):
        if 'americano' in order[i]:
            answer += 4500
        elif 'cafelatte' in order[i]:
            answer += 5000
        else:
            answer += 4500
    return answer
  
# -------------------------------------------------
# [문제 2] 그림 확대 
# https://school.programmers.co.kr/learn/courses/30/lessons/181836
# 📘 설명: 그림 파일을 나타낸 문자열 배열 picture과 정수 k가 매개변수로 주어질 때, 이 그림 파일을 가로 세로로 k배 늘린 그림 파일을 나타내도록 문자열 배열을 return 하는 solution 함수를 작성하는 문제 
# 💡 배운 점: 행 추가 시점을 항상 또 확인하기
# -------------------------------------------------

def problem_2(picture, k):
    answer = []
    for i in range(len(picture)):
        tmp = ""
        for j in range(len(picture[i])):
            if picture[i][j] == '.':
                for l in range(k):
                    tmp+='.'
            else:
                for l in range(k):
                    tmp+='x'
        for l in range(k):
            answer.append(tmp)
    return answer
  
# -------------------------------------------------
# [문제 3] 조건에 맞게 수열 변환하기 3 
# https://school.programmers.co.kr/learn/courses/30/lessons/181835
# 📘 설명: 만약 k가 홀수라면 arr의 모든 원소에 k를 곱하고, k가 짝수라면 arr의 모든 원소에 k를 더한 후의 arr를 return 하는 solution 함수를 완성하는 문제 
# 💡 배운 점: 이전에 나왔던 유형들과 유
# -------------------------------------------------

def problem_3(arr, k):
    answer = []
    if k%2!=0:
        for i in range(len(arr)):
            answer.append(arr[i]*k)
    else:
        for i in range(len(arr)):
            answer.append(arr[i]+k)    
    return answer
    
# -------------------------------------------------
# [문제 4] l로 만들기 
# https://school.programmers.co.kr/learn/courses/30/lessons/181834
# 📘 설명: 알파벳 순서에서 "l"보다 앞서는 모든 문자를 "l"로 바꾼 문자열을 return 하는 solution 함수를 완성하는 문제 
# 💡 배운 점: 문자열도 대소 비교 가능 ex) 'a' < 'i'
# -------------------------------------------------

def problem_4(myString):
    answer = ''
    for i in range(len(myString)):
        if myString[i] < 'l':
            answer += 'l'
        else:
            answer += myString[i]
    return answer
  
# -------------------------------------------------
# [문제 5] 특별한 이차원 배열 1  
# https://school.programmers.co.kr/learn/courses/30/lessons/181833
# 📘 설명: 정수 n이 매개변수로 주어질 때, 다음과 같은 n × n 크기의 이차원 배열 arr를 return 하는 solution 함수를 작성하는 문제 
# 💡 배운 점: 처음부터 이차원 배열을 list=[[]] 이런식으로 하고 요소를 한 행당 추가하려면 어려움. 처음에는 list=[] 이렇게 일차원으로 두고, 요소를 넣을 때, list.append([]) 이런 식으로 행을 추가한 뒤, 요소를 넣어주기 
# -------------------------------------------------

def problem_5(n):
    answer = []
    for i in range(n):
        answer.append([])
        for j in range(n):
            if i==j:
                answer[i].append(1)
            else:
                answer[i].append(0)
    return answer
