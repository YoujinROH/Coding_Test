# -------------------------------------------------
# [문제 1] 0 떼기
# https://school.programmers.co.kr/learn/courses/30/lessons/181847
# 📘 설명: 정수로 이루어진 문자열 n_str이 주어질 때, n_str의 가장 왼쪽에 처음으로 등장하는 0들을 뗀 문자열을 return하도록 solution 함수를 완성하는 문제
# 💡 배운 점: 어떤 조건을 기준으로 반복하다가 멈추고 싶으면 for문과 break을 적절히 활용
# -------------------------------------------------

def problem_1(n_str):
    index = 0
    for i in range(len(n_str)):
        if not int(n_str[i])==0:
            index = i
            break
    return n_str[i:]

  
# -------------------------------------------------
# [문제 2] 두 수의 합
# https://school.programmers.co.kr/learn/courses/30/lessons/181846
# 📘 설명: 0 이상의 두 정수가 문자열 a, b로 주어질 때, a + b의 값을 문자열로 return 하는 solution 함수를 작성하는 문제 
# 💡 배운 점: 따로 없음.. int() str() 함수 사용법 정도 되새기
# -------------------------------------------------

def problem_2(a, b):
    return str(int(a) + int(b))
  
# -------------------------------------------------
# [문제 3] 문자열 변환
# https://school.programmers.co.kr/learn/courses/30/lessons/181845
# 📘 설명: 정수 n이 주어질 때, n을 문자열로 변환하여 return하도록 solution 함수를 완성하는 문제  
# 💡 배운 점: 정수 -> 문자열 변환 위해서는 str() 함수 사
# -------------------------------------------------

def problem_4(n):
    return str(n)
    
# -------------------------------------------------
# [문제 4] 배열의 원소 삭제하기
# https://school.programmers.co.kr/learn/courses/30/lessons/181844
# 📘 설명: 정수 배열 arr과 delete_list가 있을 때, arr의 원소 중 delete_list의 원소를 모두 삭제하고 남은 원소들은 기존의 arr에 있던 순서를 유지한 배열을 return 하는 solution 함수를 작성하는 문제
# 💡 배운 점: if a not in list 기억하
# -------------------------------------------------

def problem_4(arr, delete_list): 
    answer = []
    for i in range(len(arr)):
        if arr[i] not in delete_list:
            answer.append(arr[i])
    return answer
  
# -------------------------------------------------
# [문제 5] 부분 문자열인지 확인하기  
# https://school.programmers.co.kr/learn/courses/30/lessons/181843
# 📘 설명: 문자열 my_string과 target이 매개변수로 주어질 때, target이 문자열 my_string의 부분 문자열이라면 1을, 아니라면 0을 return 하는 solution 함수를 작성하는 문제 
# 💡 배운 점: 문자열 a가 문자열 b안에 있는지 확인하려면 굳이 문자열 경우의수대로 보고 비교 할 필요 X. 그냥 in 함수 사용하기 
# -------------------------------------------------

def problem_5(my_string, target):
    answer = 0
    if target in my_string:
        answer = 1
    return answer
