# -------------------------------------------------
# [문제 1] 조건에 맞게 수열 변환하기 1
# https://school.programmers.co.kr/learn/courses/30/lessons/181882
# 📘 설명: 정수 배열 arr가 주어집니다. arr의 각 원소에 대해 값이 50보다 크거나 같은 짝수라면 2로 나누고, 50보다 작은 홀수라면 2를 곱하여, 그 결과인 정수 배열을 return 하는 solution 함수를 완성하는 문제 
# 💡 배운 점: 홀수인 경우는 a%2!=0 이런식으로 조건문 주기  
# -------------------------------------------------

def problem_1(arr):
    for i in range(len(arr)):
        if arr[i] >= 50 and arr[i]%2==0:
            arr[i]=arr[i]//2
        elif arr[i] < 50 and arr[i]%2!=0:
            arr[i]=arr[i]*2
    return arr
  
# -------------------------------------------------
# [문제 2] 조건에 맞게 수열 변환하기 2 
# https://school.programmers.co.kr/learn/courses/30/lessons/181881
# 📘 설명: 정수 배열 arr가 주어졌을 때, arr의 각 원소에 대해 값이 50보다 크거나 같은 짝수라면 2로 나누고, 50보다 작은 홀수라면 2를 곱하고 다시 1을 더하는 작업을 x번 반복한 결과인 배열을 arr(x)라고 표현하고, arr(x) = arr(x + 1)인 x가 항상 존재한다고 가정했을 때, 이러한 x 중 가장 작은 값을 return 하는 solution 함수를 완성하는 문제 
# 💡 배운 점: 리스트끼리 비교하는 거 굳이 원소 간의 비교 안해도 되고 전체 비교 list1==list2 해도 됨 
# -------------------------------------------------

def problem_2(arr):
    count = 0
    while True:
        new_arr = []
        for n in arr:
            if n >= 50 and n % 2 == 0:
                new_arr.append(n // 2)
            elif n < 50 and n % 2 == 1:
                new_arr.append(n * 2 + 1)
            else:
                new_arr.append(n)
        
        if new_arr == arr: 
            return count
        arr = new_arr
        count += 1
  
# -------------------------------------------------
# [문제 3] 1로 만들기 
# https://school.programmers.co.kr/learn/courses/30/lessons/181880
# 📘 설명: 정수들이 담긴 리스트 num_list가 주어질 때, num_list의 모든 원소를 1로 만들기 위해서 필요한 나누기 연산의 횟수를 return하도록 solution 함수를 완성하는 문제 
# 💡 배운 점: while문 활용하기   
# -------------------------------------------------

def problem_3(num_list):
    answer = 0
    tmp=0
    for i in range(len(num_list)):
        tmp=num_list[i]
        while (tmp!=1):
            if tmp%2==0:
                tmp=tmp//2
            else:
                tmp=(tmp-1)//2
            answer+=1
    return answer
    
# -------------------------------------------------
# [문제 4] 길이에 따른 연산   
# https://school.programmers.co.kr/learn/courses/30/lessons/181879
# 📘 설명: 정수가 담긴 리스트 num_list가 주어질 때, 리스트의 길이가 11 이상이면 리스트에 있는 모든 원소의 합을 10 이하이면 모든 원소의 곱을 return하도록 solution 함수를 완성하는 문제  
# 💡 배운 점: 리스트 요소를 전부 더하는 sum() 함수 존재. 그러나 곱하는 것은 math 라이브러리의 함수를 써야함 
# -------------------------------------------------

def problem_4(num_list):
    answer = 0
    if len(num_list) >= 11:
        answer=sum(num_list)
    else:
        answer=1
        for num in num_list:
            answer*=num
    return answer
  
# -------------------------------------------------
# [문제 5] 원하는 문자열 찾기  
# https://school.programmers.co.kr/learn/courses/30/lessons/181878
# 📘 설명: 알파벳으로 이루어진 문자열 myString과 pat이 주어집니다. myString의 연속된 부분 문자열 중 pat이 존재하면 1을 그렇지 않으면 0을 return 하는 solution 함수를 완성하는 문제 
# 💡 배운 점: upper 함수는 string.upper() 의 형식으로 사용  
# -------------------------------------------------

def problem_5(myString, pat):
    if pat.upper() in myString.upper():
        return 1
    else:
        return 0
