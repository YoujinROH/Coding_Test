# -------------------------------------------------
# [문제 1] 특정 문자열로 끝나는 가장 긴 부분 문자열 찾기 
# https://school.programmers.co.kr/learn/courses/30/lessons/181872
# 📘 설명: myString의 부분 문자열중 pat로 끝나는 가장 긴 부분 문자열을 찾아서 return 하는 solution 함수를 완성하는 문제
# 💡 배운 점: 문자열 안에 특정 문자열이 맨 마지막에 나타나는 인덱스를 구하는 것은 rfind() 함수를 쓰면 됨 
# -------------------------------------------------

def problem_1(myString, pat):
    idx = myString.rfind(pat) 
    return myString[:idx + len(pat)]
  
# -------------------------------------------------
# [문제 2] 문자열이 몇 번 등장하는지 세기 
# https://school.programmers.co.kr/learn/courses/30/lessons/181871
# 📘 설명: myString에서 pat이 등장하는 횟수를 return 하는 solution 함수를 완성하는 문제 
# 💡 배운 점: 등장횟수 찾을 때는 원본 문자열을 찾을 문자열 길이만큼의 문자열로 나눠두고 확인 
# -------------------------------------------------

def problem_2(myString, pat):
    answer = 0
    stringlist = []
    for i in range(len(myString)-len(pat)+1):
        stringlist.append(myString[i:i+len(pat)])
    for word in stringlist:
        if word==pat:
            answer+=1
    return answer
  
# -------------------------------------------------
# [문제 3] ad 제거하기 
# https://school.programmers.co.kr/learn/courses/30/lessons/181870
# 📘 설명: 배열 내의 문자열 중 "ad"라는 부분 문자열을 포함하고 있는 모든 문자열을 제거하고 남은 문자열을 순서를 유지하여 배열로 return 하는 solution 함수를 완성하는 문제 
# 💡 배운 점: 문자열 안에 어떤 문자열이 없는지 확인할때는 not in 사용 
# -------------------------------------------------

def problem_3(strArr):
    answer = []
    for word in strArr:
        if 'ad' not in word:
            answer.append(word)
    return answer
    
# -------------------------------------------------
# [문제 4] 공백으로 구분하기 1     
# https://school.programmers.co.kr/learn/courses/30/lessons/181869
# 📘 설명: 단어가 공백 한 개로 구분되어 있는 문자열 my_string이 매개변수로 주어질 때, my_string에 나온 단어를 앞에서부터 순서대로 담은 문자열 배열을 return 하는 solution 함수를 작성하는 문제 
# 💡 배운 점: 문자열을 공백 기준으로 나눠 리스트에 저장하기 위해서는 split() 함수 사용하기 
# -------------------------------------------------

def problem_4(my_string):
    answer = []
    answer = my_string.split(" ")
    return answer
  
# -------------------------------------------------
# [문제 5] 공백으로 구분하기 2   
# https://school.programmers.co.kr/learn/courses/30/lessons/181868
# 📘 설명: 단어가 공백 한 개 이상으로 구분되어 있는 문자열 my_string이 매개변수로 주어질 때, my_string에 나온 단어를 앞에서부터 순서대로 담은 문자열 배열을 return 하는 solution 함수를 작성하는 문제   
# 💡 배운 점: split() 함수는 굳이 공백 기준으로 나누지 않아도 연속된 공백을 모두 제거하고 문자열만 리스트로 나눠줌   
# -------------------------------------------------

def solution(my_string):
    return my_string.split()
