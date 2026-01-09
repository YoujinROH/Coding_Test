# -------------------------------------------------
# [문제 1] 뒤에서 5등 위로  
# https://school.programmers.co.kr/learn/courses/30/lessons/181852
# 📘 설명: 정수로 이루어진 리스트 num_list가 주어졌을 때, num_list에서 가장 작은 5개의 수를 제외한 수들을 오름차순으로 담은 리스트를 return하도록 solution 함수를 완성하는 문제
# 💡 배운 점: sort() 함수는 따로 변수 저장할 필요 없다는 것 기억하기
# -------------------------------------------------

def problem_1(num_list):
    num_list.sort()
    answer = num_list[5:]
    return answer
  
# -------------------------------------------------
# [문제 2] 전국 대회 선발 고사 
# https://school.programmers.co.kr/learn/courses/30/lessons/181851
# 📘 설명: 각 학생들의 선발 고사 등수를 담은 정수 배열 rank와 전국 대회 참여 가능 여부가 담긴 boolean 배열 attendance가 매개변수로 주어졌을 때, 등수가 높은 순서대로 각각 a, b, c번이라고 할 때 10000 × a + 100 × b + c를 return 하는 solution 함수를 작성하는 문제 
# 💡 배운 점: sorted()는 무조건 list를 반환. dictionary의 .items()를 뽑으면 dict_items의 객체(튜플들의 묶음). sorted(students.items(), key=lambda x; x[1])는 students.items()를 sort하라! 대신 기준은 x[1]로!
# -------------------------------------------------

def problem_2(rank, attendance):
    students = {}
    for i in range(len(rank)):
        if attendance[i]:
            students[i] = rank[i]
    sorted_students = sorted(students.items(), key=lambda x: x[1])
    a, b, c = sorted_students[0][0], sorted_students[1][0], sorted_students[2][0]
    return 10000 * a + 100 * b + c
  
# -------------------------------------------------
# [문제 3] 정수 부분 
# https://school.programmers.co.kr/learn/courses/30/lessons/181850
# 📘 설명: 실수 flo가 매개 변수로 주어질 때, flo의 정수 부분을 return하도록 solution 함수를 완성하는 문제
# 💡 배운 점: 몫 연산자는 //
# -------------------------------------------------

def problem_3(flo):
    answer = flo//1
    return answer
    
# -------------------------------------------------
# [문제 4] 문자열 정수의 합 
# https://school.programmers.co.kr/learn/courses/30/lessons/181849
# 📘 설명: 한 자리 정수로 이루어진 문자열 num_str이 주어질 때, 각 자리수의 합을 return하도록 solution 함수를 완성하는 문제 
# 💡 배운 점: 문자열 for in range 함수 쓸 때, len으로 하던지 명확히 문자단위로 하되, i를 문자로 고려하던지 하기
# -------------------------------------------------

def problem_4(num_str):
    answer = 0
    for i in range(len(num_str)):
        answer += int(num_str[i])
    return answer
  
# -------------------------------------------------
# [문제 5] 문자열을 정수로 변환하기 
# https://school.programmers.co.kr/learn/courses/30/lessons/181848
# 📘 설명: 숫자로만 이루어진 문자열 n_str이 주어질 때, n_str을 정수로 변환하여 return하도록 solution 함수를 완성하는 문제 
# 💡 배운 점: str to int를 위해서는 int() 함수를 사용하기
# -------------------------------------------------

def solution(n_str):
    return int(n_str) 
