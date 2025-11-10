# -------------------------------------------------
# [문제 1] 배열의 길이를 2의 거듭제곱으로 만들기   
# https://school.programmers.co.kr/learn/courses/30/lessons/181862
# 📘 설명: 문자열 myStr이 주어졌을 때 위 예시와 같이 "a", "b", "c"를 사용해 나눠진 문자열을 순서대로 저장한 배열을 return 하는 solution 함수를 완성하는 문제 
# 💡 배운 점: 리스트안에 값이 없거나 문자열이 공백일 때, if not 리스트 or if not 문자열 사용하면 됨. 반대는 if 리스트 or if 문자열 
# -------------------------------------------------

def problem_1(myStr):
    answer = []
    tmp = ''
    for i in range(len(myStr)):
        if myStr[i] == 'a' or myStr[i] == 'b' or myStr[i] == 'c':
            if tmp:
                answer.append(tmp)
                tmp=''
        else:
            tmp += myStr[i]
            if i==len(myStr)-1:
                answer.append(tmp)
    if not answer:
        answer.append('EMPTY')
    return answer
  
# -------------------------------------------------
# [문제 2] 배열 비교하기  
# https://school.programmers.co.kr/learn/courses/30/lessons/181861
# 📘 설명: 양의 정수 배열 arr가 매개변수로 주어질 때, arr의 앞에서부터 차례대로 원소를 보면서 원소가 a라면 X의 맨 뒤에 a를 a번 추가하는 일을 반복한 뒤의 배열 X를 return 하는 solution 함수를 작성하는 문제  
# 💡 배운 점: 이전에 많이 나왔던 유형 
# -------------------------------------------------

def problem_2(arr):
    answer = []
    for num in arr:
        for i in range(num):
            answer.append(num)
    return answer
  
# -------------------------------------------------
# [문제 3] 문자열 묶기 
# https://school.programmers.co.kr/learn/courses/30/lessons/181860
# 📘 설명: 길이가 같은 정수 배열 arr과 boolean 배열 flag가 매개변수로 주어질 때, flag를 차례대로 순회하며 flag[i]가 true라면 X의 뒤에 arr[i]를 arr[i] × 2 번 추가하고, flag[i]가 false라면 X에서 마지막 arr[i]개의 원소를 제거한 뒤 X를 return 하는 solution 함수를 작성하는 문제   
# 💡 배운 점: 리스트 마지막 요소 뽑아서 제거할 때는 pop() 함수가 유용함. 굳이 새 변수에 안넣어줘도 동작하는 함수 
# -------------------------------------------------

def problem_3(arr, flag):
    answer = []
    for i in range(len(flag)):
        if flag[i]==True:
            for j in range(arr[i]*2):
                answer.append(arr[i])
        else:
            for k in range(arr[i]):
                answer.pop()
    return answer
    
# -------------------------------------------------
# [문제 4] 배열의 길이에 따라 다른 연산하기 
# https://school.programmers.co.kr/learn/courses/30/lessons/181859
# 📘 설명: 작업을 마친 후 만들어진 stk을 return 하는 solution 함수를 완성하는 문제 
# 💡 배운 점: 리스트의 맨 마지막 요소에 접근하려면 list[-1]로 진행 
# -------------------------------------------------

def problem_4(arr): 
    stk = []
    i = 0
    while (i < len(arr)):
        if not stk:
            stk.append(arr[i])
            i+=1
        elif stk and stk[-1]==arr[i]:
            stk.pop()
            i+=1
        elif stk and stk[-1]!=arr[i]:
            stk.append(arr[i])
            i+=1
    if not stk:
        stk.append(-1)
    return stk
  
# -------------------------------------------------
# [문제 5] 뒤에서 5등까지  
# https://school.programmers.co.kr/learn/courses/30/lessons/181858
# 📘 설명: 정수 배열 arr가 주어지고 문제에서의 무작위의 수는 arr에 저장된 순서대로 주어질 예정이라고 했을 때, 완성될 배열을 return 하는 solution 함수를 완성하는 문제 
# 💡 배운 점: list에서 유니크한 원소를 뽑아내기에는 set()이 편하지만 set 함수는 순서를 고려하지 않으므로 유의해야함 
# -------------------------------------------------

def problem_5(arr, k):
    answer = []
    for num in arr:
        if num not in answer:
            answer.append(num)
        if len(answer)==k:
            break
    if len(answer)<k:
        for i in range(k-len(answer)):
            answer.append(-1)
    return answer
  
