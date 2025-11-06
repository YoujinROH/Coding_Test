# -------------------------------------------------
# [문제 1] n 번째 원소부터
# https://school.programmers.co.kr/learn/courses/30/lessons/181892
# 📘 설명: 정수 리스트 num_list와 정수 n이 주어질 때, n 번째 원소부터 마지막 원소까지의 모든 원소를 담은 리스트를 return하도록 solution 함수를 완성하는 문제 
# 💡 배운 점: 항상 range의 start, end 잘 확인하기 
# -------------------------------------------------

def problem_1(num_list, n):
    answer = []
    for i in range(n-1,len(num_list)):
        answer.append(num_list[i])
    return answer
  
# -------------------------------------------------
# [문제 2] 순서 바꾸기 
# https://school.programmers.co.kr/learn/courses/30/lessons/181891
# 📘 설명: 정수 리스트 num_list와 정수 n이 주어질 때, num_list를 n 번째 원소 이후의 원소들과 n 번째까지의 원소들로 나눠 n 번째 원소 이후의 원소들을 n 번째까지의 원소들 앞에 붙인 리스트를 return하도록 solution 함수를 완성하는 문제 
# 💡 배운 점: 리스트 두 개 이상을 붙이고 싶으면 + 연산자 사용하기  
# -------------------------------------------------

def problem_2(num_list, n):
    answer = []
    answer = num_list[n:]+num_list[:n]
    return answer
  
# -------------------------------------------------
# [문제 3] 왼쪽 오른쪽
# https://school.programmers.co.kr/learn/courses/30/lessons/181890
# 📘 설명: 문자열 리스트 str_list에는 "u", "d", "l", "r" 네 개의 문자열이 여러 개 저장되어 있습니다. str_list에서 "l"과 "r" 중 먼저 나오는 문자열이 "l"이라면 해당 문자열을 기준으로 왼쪽에 있는 문자열들을 순서대로 담은 리스트를, 먼저 나오는 문자열이 "r"이라면 해당 문자열을 기준으로 오른쪽에 있는 문자열들을 순서대로 담은 리스트를 return하도록 solution 함수를 완성하는 문제 
# 💡 배운 점: 빈 리스트의 0번 인덱스를 접근하도록 하는 조건문을 쓰지 않도록 하기 
# -------------------------------------------------

def problem_3(str_list):
    answer = []
    l_list = []
    r_list = []
    for i in range(len(str_list)):
        if str_list[i]=="l":
            l_list.append(i)
        elif str_list[i]=='r':
            r_list.append(i)
    if not l_list and not r_list:
        answer = []
    elif not r_list:
        answer = str_list[:l_list[0]]
    elif not l_list:
        answer = str_list[r_list[0]+1:]
    else:
        if l_list[0] < r_list[0]:
            answer = str_list[:l_list[0]]
        elif r_list[0] < l_list[0]:
            answer = str_list[r_list[0]+1:]
    return answer
    
# -------------------------------------------------
# [문제 4] n 번째 원소까지  
# https://school.programmers.co.kr/learn/courses/30/lessons/181889
# 📘 설명: 정수 리스트 num_list와 정수 n이 주어질 때, num_list의 첫 번째 원소부터 n 번째 원소까지의 모든 원소를 담은 리스트를 return하도록 solution 함수를 완성하는 문제 
# 💡 배운 점: list start, end 유의하기 
# -------------------------------------------------

def problem_4(num_list, n):
    answer = []
    answer = num_list[:n]
    return answer
  
# -------------------------------------------------
# [문제 5] n개 간격의 원소들   
# https://school.programmers.co.kr/learn/courses/30/lessons/181888
# 📘 설명: 정수 리스트 num_list와 정수 n이 주어질 때, num_list의 첫 번째 원소부터 마지막 원소까지 n개 간격으로 저장되어있는 원소들을 차례로 담은 리스트를 return하도록 solution 함수를 완성하는 문제 
# 💡 배운 점: [start, end, step], 처음부터 끝까지 n개 간격이면 [::n]
# -------------------------------------------------

def problem_5(num_list, n):
    answer = []
    answer = num_list[::n]
    return answer
  
