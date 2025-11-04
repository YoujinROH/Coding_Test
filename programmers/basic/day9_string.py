# -------------------------------------------------
# [문제 1] 배열 만들기 5 
# https://school.programmers.co.kr/learn/courses/30/lessons/181912
# 📘 설명: 배열 intStrs의 각 원소마다 s번 인덱스에서 시작하는 길이 l짜리 부분 문자열을 잘라내 정수로 변환했을 때 그 정수값이 k보다 큰 값들을 담은 배열을 return 하는 solution 함수를 완성하는 문제 
# 💡 배운 점: 슬라이싱할때 인덱스 항상 확인 
# -------------------------------------------------

def problem_1(intStrs, k, s, l):
    answer = []
    for word in intStrs:
        if int(word[s:s+l]) > k:
            answer.append(int(word[s:s+l]))
    return answer

# -------------------------------------------------
# [문제 2] 부분 문자열 이어 붙여 문자열 만들기 
# https://school.programmers.co.kr/learn/courses/30/lessons/181911
# 📘 설명: 각 my_strings의 원소의 parts에 해당하는 부분 문자열을 순서대로 이어 붙인 문자열을 return 하는 solution 함수를 작성하는 문제 
# 💡 배운 점: 슬라이싱할때 stop-1까지만 진행된다는 것 명심하기 
# -------------------------------------------------

def problem_2(my_strings, parts):
    answer = ''
    index = 0
    for word in my_strings:
        answer+=word[parts[index][0]:parts[index][1]+1]
        index+=1
    return answer
  
# -------------------------------------------------
# [문제 3] 문자열의 뒤의 n글자 
# https://school.programmers.co.kr/learn/courses/30/lessons/181910
# 📘 설명: 문자열 my_string과 정수 n이 매개변수로 주어질 때, my_string의 뒤의 n글자로 이루어진 문자열을 return 하는 solution 함수를 작성하는 문제 
# 💡 배운 점: 슬라이싱할 때 문자열 끝까지 뽑고 싶으면 그냥 [start:] 이런식으로 stop은 비워둬도 됨   
# -------------------------------------------------

def problem_3(my_string, n):
    answer = ''
    answer=my_string[len(my_string)-n:]
    return answer
    
# -------------------------------------------------
# [문제 4] 접미사 배열 
# https://school.programmers.co.kr/learn/courses/30/lessons/181909
# 📘 설명: 문자열 my_string이 매개변수로 주어질 때, my_string의 모든 접미사를 사전순으로 정렬한 문자열 배열을 return 하는 solution 함수를 작성하는 문제 
# 💡 배운 점: sort()함수의 경우 impure function으로 객체를 직접 수정하고 return값이 None임. sorted()함수는 pure function으로 return값으로 받아서 반영해야함 
# -------------------------------------------------

def problem_4(my_string):
    answer = []
    for i in range(len(my_string)):
        answer.append(my_string[i:])
    answer.sort()
    return answer

# -------------------------------------------------
# [문제 5] 접미사인지 확인하기  
# https://school.programmers.co.kr/learn/courses/30/lessons/181908
# 📘 설명: 문자열 my_string과 is_suffix가 주어질 때, is_suffix가 my_string의 접미사라면 1을, 아니면 0을 return 하는 solution 함수를 작성하는 문제 
# 💡 배운 점: list에 해당 요소가 있는지 확인하려면 if a is in list 함수 쓰면 편함 
# -------------------------------------------------

def problem_5(my_string, is_suffix):
    answer = 0
    word_list = []
    for i in range(len(my_string)):
        word_list.append(my_string[i:])
    if is_suffix in word_list:
        answer=1
    return answer
