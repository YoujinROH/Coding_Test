# -------------------------------------------------
# [문제 1] 대문자로 바꾸기 
# https://school.programmers.co.kr/learn/courses/30/lessons/181877
# 📘 설명: 모든 알파벳을 대문자로 변환하여 return 하는 solution 함수를 완성하는 문제 
# 💡 배운 점: 대문자로 바꾸는 함수는 upper()
# -------------------------------------------------

def problem_1(myString):
    return myString.upper()
  
# -------------------------------------------------
# [문제 2] 소문자로 바꾸기 
# https://school.programmers.co.kr/learn/courses/30/lessons/181876
# 📘 설명: 모든 알파벳을 소문자로 변환하여 return 하는 solution 함수를 완성하는 문제 
# 💡 배운 점: 소문자로 바꾸는 함수는 lower()
# -------------------------------------------------

def problem_2(myString):
    return myString.lower()
  
# -------------------------------------------------
# [문제 3] 배열에서 문자열 대소문자 변환하기 
# https://school.programmers.co.kr/learn/courses/30/lessons/181875
# 📘 설명: 배열에서 홀수번째 인덱스의 문자열은 모든 문자를 대문자로, 짝수번째 인덱스의 문자열은 모든 문자를 소문자로 바꿔서 반환하는 solution 함수를 완성하는 문제 
# 💡 배운 점: upper(), lower() 
# -------------------------------------------------

def problem_3(strArr):
    answer = []
    for i in range(len(strArr)):
        if i%2==0:
            answer.append(strArr[i].lower())
        else:
            answer.append(strArr[i].upper())
    return answer
    
# -------------------------------------------------
# [문제 4] A 강조하기    
# https://school.programmers.co.kr/learn/courses/30/lessons/181874
# 📘 설명: myString에서 알파벳 "a"가 등장하면 전부 "A"로 변환하고, "A"가 아닌 모든 대문자 알파벳은 소문자 알파벳으로 변환하여 return 하는 solution 함수를 완성하는 문제 
# 💡 배운 점: 문자열을 다른걸로 바꾸고 싶다면 빈 문자열을 만들어서 추가하는 방식으로 해야함 myString[i] = myString[i].upper() 이런식으로는 안 됨!! 
# -------------------------------------------------

def problem_4(myString):
    answer=''
    for i in range(len(myString)):
        if myString[i] == "a":
            answer += myString[i].upper()
        elif myString[i] == "A":
            answer += myString[i]
        else:
            answer += myString[i].lower()
    return answer
  
# -------------------------------------------------
# [문제 5] 특정한 문자를 대문자로 바꾸기  
# https://school.programmers.co.kr/learn/courses/30/lessons/181873
# 📘 설명: 영소문자로 이루어진 문자열 my_string과 영소문자 1글자로 이루어진 문자열 alp가 매개변수로 주어질 때, my_string에서 alp에 해당하는 모든 글자를 대문자로 바꾼 문자열을 return 하는 solution 함수를 작성하는 문제  
# 💡 배운 점: str끼리 같은 지 확인하려면 my_string[i]==alp 이런식으로 그냥 ==연산자 쓰면 됨  
# -------------------------------------------------

def problem_5(my_string, alp):
    answer = ''
    for i in range(len(my_string)):
        if my_string[i]==alp:
            answer += my_string[i].upper()
        else:
            answer += my_string[i]
    return answer
