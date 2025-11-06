# -------------------------------------------------
# [문제 1] 리스트 자르기 
# https://school.programmers.co.kr/learn/courses/30/lessons/181897
# 📘 설명: 정수 n과 정수 3개가 담긴 리스트 slicer 그리고 정수 여러 개가 담긴 리스트 num_list가 주어졌을때, slicer에 담긴 정수를 차례대로 a, b, c라고 할 때, n에 따라 다음과 같이 num_list를 슬라이싱 하는 문제 
# 💡 배운 점: 하나의 리스트에 있는 값들을 여러 변수에 할당하고 싶은 경우 a,b,c=slicer와 같은 기능 활
# -------------------------------------------------

def problem_1(n, slicer, num_list):
    answer = []
    a,b,c=slicer
    if n==1:
        answer=num_list[0:b+1]
    elif n==2:
        answer=num_list[a:]
    elif n==3:
        answer=num_list[a:b+1]
    else:
        answer=num_list[a:b+1:c]
    return answer

# -------------------------------------------------
# [문제 2] 첫 번째로 나오는 음수 
# https://school.programmers.co.kr/learn/courses/30/lessons/181896
# 📘 설명: 정수 리스트 num_list가 주어질 때, 첫 번째로 나오는 음수의 인덱스를 return하도록 solution 함수를 완성해주세요. 음수가 없다면 -1을 return하는 문제 
# 💡 배운 점: 리스트 순서 끝까지 해당 조건이 성립하지 않는 경우 if 조건으로 두고, else 안에서 if 마지막 순서이면~~으로 풀기 
# -------------------------------------------------

def problem_2(num_list):
    answer = 0
    for i in range(len(num_list)):
        if num_list[i] < 0:
            answer=i
            break
        else:
            if i==len(num_list)-1:
                answer=-1
    return answer
  
# -------------------------------------------------
# [문제 3] 배열 만들기 3  
# https://school.programmers.co.kr/learn/courses/30/lessons/181895
# 📘 설명: 배열 arr의 첫 번째 구간에 해당하는 배열과 두 번째 구간에 해당하는 배열을 앞뒤로 붙여 새로운 배열을 만들어 return 하는 solution 함수를 완성하는 문제 
# 💡 배운 점: 두 개 이상의 리스트 내부 요소를 하나의 리스트로 합치려면 요소별로 순서대로 append해야함 
# -------------------------------------------------

def problem_3(arr, intervals):
    answer = []
    for section in intervals:
        a, b = section
        for i in range(a,b+1):
            answer.append(arr[i])
    return answer
    
# -------------------------------------------------
# [문제 4] 2의 영역 
# https://school.programmers.co.kr/learn/courses/30/lessons/181894
# 📘 설명: 정수 배열 arr가 주어집니다. 배열 안의 2가 모두 포함된 가장 작은 연속된 부분 배열을 return 하는 solution 함수를 완성하는 문제 
# 💡 배운 점: min, max 함수 사용할 때는 min(list), max(list) 이런 식으로 하기 
# -------------------------------------------------

def problem_4(arr):
    answer = []
    two_list = []
    for i in range(len(arr)):
        if arr[i]==2:
            two_list.append(i)
    if not two_list:
        answer.append(-1)
    else:
        for i in range(min(two_list),max(two_list)+1):
            answer.append(arr[i])
    return answer
  
# -------------------------------------------------
# [문제 5] 배열 조각하기  
# https://school.programmers.co.kr/learn/courses/30/lessons/181893
# 📘 설명: 작업을 마친 후 남은 arr의 부분 배열을 return 하는 solution 함수를 완성하는 문제 
# 💡 배운 점: 문제 잘 읽기... 
# -------------------------------------------------

def problem_5(arr, query):
    answer = []
    answer = arr
    for i in range(len(query)):
        if i%2==0:
            answer=answer[:query[i]+1]
        else:
            answer=answer[query[i]:]
    return answer
