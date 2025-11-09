# -------------------------------------------------
# [문제 1] x 사이의 개수 
# https://school.programmers.co.kr/learn/courses/30/lessons/181867
# 📘 설명: myString을 문자 "x"를 기준으로 나눴을 때 나눠진 문자열 각각의 길이를 순서대로 저장한 배열을 return 하는 solution 함수를 완성하는 문제 
# 💡 배운 점: 특정 문자열 기준으로 전체 문자열을 나눠 리스트로 만들고 싶다면 split 사용하기 
# -------------------------------------------------

def problem_1(myString):
    answer = []
    stringlist = myString.split("x")
    for string in stringlist:
        answer.append(len(string))
    return answer
  
# -------------------------------------------------
# [문제 2] 문자열 잘라서 정렬하기 
# https://school.programmers.co.kr/learn/courses/30/lessons/181866
# 📘 설명: "x"를 기준으로 해당 문자열을 잘라내 배열을 만든 후 사전순으로 정렬한 배열을 return 하는 solution 함수를 완성하는 문제 
# 💡 배운 점: split을 사용하여 특정 문자를 기준으로 문자열을 나누면 리스트 요소로 공백도 들어갈 수 있기에 이는 따로 처리해야함 
# -------------------------------------------------

def problem_2(myString):
    answer = []
    stringlist = myString.split("x")
    for word in stringlist:
        if len(word)!=0:
            answer.append(word)
    answer.sort()
    return answer
  
# -------------------------------------------------
# [문제 3] 간단한 식 계산하기 
# https://school.programmers.co.kr/learn/courses/30/lessons/181865
# 📘 설명: binomial은 "a op b" 형태의 이항식이고 a와 b는 음이 아닌 정수, op는 '+', '-', '*' 중 하나입니다. 주어진 식을 계산한 정수를 return 하는 solution 함수를 작성하는 문제  
# 💡 배운 점: 오타 조심하기 
# -------------------------------------------------

def problem_3(binomial):
    answer = 0
    stringlist = binomial.split(" ")
    if stringlist[1]=='+':
        answer = int(stringlist[0]) + int(stringlist[2])
    elif stringlist[1]=='-':
        answer = int(stringlist[0]) - int(stringlist[2])
    elif stringlist[1]=='*':
        answer = int(stringlist[0]) * int(stringlist[2])
    return answer
    
# -------------------------------------------------
# [문제 4] 문자열 바꿔서 찾기      
# https://school.programmers.co.kr/learn/courses/30/lessons/181864
# 📘 설명: myString의 "A"를 "B"로, "B"를 "A"로 바꾼 문자열의 연속하는 부분 문자열 중 pat이 있으면 1을 아니면 0을 return 하는 solution 함수를 완성하는 문제 
# 💡 배운 점: 문자열은 리스트처럼 인덱싱으로 접근 가능함 
# -------------------------------------------------

def problem_4(myString, pat):
    answer = 0
    newString = ''
    for i in range(len(myString)):
        if myString[i] == 'A':
            newString += 'B'
        elif myString[i] == 'B':
            newString += 'A'
        else:
            newString += myString[i]
    if pat in newString:
        answer = 1
    return answer
  
# -------------------------------------------------
# [문제 5] my_string 
# https://school.programmers.co.kr/learn/courses/30/lessons/181863
# 📘 설명: 문자열 rny_string이 주어질 때, rny_string의 모든 'm'을 "rn"으로 바꾼 문자열을 return 하는 solution 함수를 작성하는 문제    
# 💡 배운 점: 보통 어떤 문자열에 변형을 준 문자열을 만들어야하면 그냥 새로운 문자열을 만드는게 편함 
# -------------------------------------------------

def solution(rny_string):
    answer = ''
    for string in rny_string:
        if string == 'm':
            answer += 'rn'
        else:
            answer += string
    return answer
  
