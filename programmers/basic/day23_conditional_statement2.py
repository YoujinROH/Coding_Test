# -------------------------------------------------
# [문제 1] 부분 문자열
# https://school.programmers.co.kr/learn/courses/30/lessons/181842
# 📘 설명: 문자열 str1과 str2가 주어질 때, str1이 str2의 부분 문자열이라면 1을 부분 문자열이 아니라면 0을 return하도록 solution 함수를 완성하는 문제
# 💡 배운 점: 부분 문자열은 if in 함수 쓰면 확실히 편해짐
# -------------------------------------------------

def problem_1(str1, str2):
    answer = 0
    if str1 in str2:
        answer=1
    return answer

  
# -------------------------------------------------
# [문제 2] 꼬리 문자열
# https://school.programmers.co.kr/learn/courses/30/lessons/181841
# 📘 설명: 문자열 리스트 str_list와 제외하려는 문자열 ex가 주어질 때, str_list에서 ex를 포함한 문자열을 제외하고 만든 꼬리 문자열을 return하도록 solution 함수를 완성하는 문제
# 💡 배운 점: 항상 쉬운 문제도 한번 점검하기
# -------------------------------------------------

def problem_2(str_list, ex):
    answer = ''
    for i in range(len(str_list)):
        if ex not in str_list[i]:
            answer += str_list[i]
    return answer
  
# -------------------------------------------------
# [문제 3] 정수 찾기
# https://school.programmers.co.kr/learn/courses/30/lessons/181840
# 📘 설명: 정수 리스트 num_list와 찾으려는 정수 n이 주어질 때, num_list안에 n이 있으면 1을 없으면 0을 return하도록 solution 함수를 완성하는 문제 
# 💡 배운 점: if in 함수는 리스트 요소를 찾는데에도 유용하게 사용 가능
# -------------------------------------------------

def problem_3(num_list, n):
    answer = 0
    if n in num_list:
        answer = 1
    return answer
    
# -------------------------------------------------
# [문제 4] 주사위 게임 1
# https://school.programmers.co.kr/learn/courses/30/lessons/181839
# 📘 설명: 두 정수 a와 b가 매개변수로 주어질 때, 얻는 점수를 return 하는 solution 함수를 작성하는 문제 
# 💡 배운 점: 절대값을 위한 abs() 함수는 아무것도 import하지 않고 써도 되는 내장 함수
# -------------------------------------------------

def problem_4(a, b):
    answer = 0
    if a%2!=0 and b%2!=0:
        answer = a ** 2 + b ** 2
    elif a%2!=0 or b%2!=0:
        answer = 2 * (a + b)
    elif a%2==0 and b%2==0:
        answer = abs(a-b)
    return answer
  
# -------------------------------------------------
# [문제 5] 날짜 비교하기  
# https://school.programmers.co.kr/learn/courses/30/lessons/181838
# 📘 설명: 만약 date1이 date2보다 앞서는 날짜라면 1을, 아니면 0을 return 하는 solution 함수를 완성하는 함수
# 💡 배운 점: 정수 비교 문제라도 가끔은 문자열로 합친 뒤에 정수로 다시 변경하여 비교하는 것도 쉬운 방법이 될 수 있음 
# -------------------------------------------------

def problem_5(date1, date2):
    answer = 0
    datestr1 = str(date1[0]) + str(date1[1]) + str(date1[2])
    datestr2 = str(date2[0]) + str(date2[1]) + str(date2[2])
    if int(datestr1) < int(datestr2):
        answer = 1
    return answer
