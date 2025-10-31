# -------------------------------------------------
# [문제 1] 마지막 두 원소 
# https://school.programmers.co.kr/learn/courses/30/lessons/181927
# 📘 설명: 정수 리스트 num_list가 주어질 때, 마지막 원소가 그전 원소보다 크면 마지막 원소에서 그전 원소를 뺀 값을 마지막 원소가 그전 원소보다 크지 않다면 마지막 원소를 두 배한 값을 추가하여 return하도록 solution 함수를 완성하는 문제 
# 💡 배운 점: len을 쓰면 항상 마지막 요소 인덱스 번호는 len-1 
# -------------------------------------------------

def problem_1(num_list):
    if num_list[len(num_list)-1] > num_list[len(num_list)-2]:
        num_list.append(num_list[len(num_list)-1]-num_list[len(num_list)-2])
    else:
        num_list.append(2*(num_list[len(num_list)-1]))
    return num_list

# -------------------------------------------------
# [문제 2] 수 조작하기 1 
# https://school.programmers.co.kr/learn/courses/30/lessons/181926
# 📘 설명: 규칙에 따라 n을 바꿨을 때 가장 마지막에 나오는 n의 값을 return 하는 solution 함수를 완성하는 문제 
# 💡 배운 점: 문자열을 순서대로 접근하고 싶으면 for문 활용 
# -------------------------------------------------

def solution_2(n, control):
    for word in control:
        if word=="w":
            n+=1
        elif word=="s":
            n-=1
        elif word=="d":
            n+=10
        elif word=="a":
            n-=10
    return n
  
# -------------------------------------------------
# [문제 3] 수 조작하기 2 
# https://school.programmers.co.kr/learn/courses/30/lessons/181925
# 📘 설명: 주어진 정수 배열 numLog에 대해 조작을 위해 입력받은 문자열을 return 하는 solution 함수를 완성하는 문제 
# 💡 배운 점: for문 range 작성할 때, 인덱스 범위 벗어나지 않게 조심하기 
# -------------------------------------------------

def problem_3(numLog):
    answer=""
    for i in range(len(numLog)-1):
        if numLog[i+1]-numLog[i]==1:
            answer+="w"
        elif numLog[i+1]-numLog[i]==-1:
            answer+="s"
        elif numLog[i+1]-numLog[i]==10:
            answer+="d"
        elif numLog[i+1]-numLog[i]==-10:
            answer+="a"
    return answer
# -------------------------------------------------
# [문제 4] 수열과 구간 쿼리 3 
# https://school.programmers.co.kr/learn/courses/30/lessons/181924
# 📘 설명: 규칙에 따라 queries를 처리한 이후의 arr를 return 하는 solution 함수를 완성하는 문제 
# 💡 배운 점: 2차원 행렬의 len은 row 수
# -------------------------------------------------

def problem_4(arr, queries):
    tmp = 0
    for i in range(len(queries)):
        tmp = arr[queries[i][0]]
        arr[queries[i][0]] = arr[queries[i][1]]
        arr[queries[i][1]] = tmp
    return arr

# -------------------------------------------------
# [문제 5] 수열과 구간 쿼리 2 
# https://school.programmers.co.kr/learn/courses/30/lessons/181923
# 📘 설명: 각 쿼리의 순서에 맞게 답을 저장한 배열을 반환하는 solution 함수를 완성하는 문제
# 💡 배운 점: 변수를 굉장히 큰 값으로 초기화 하고 싶으면 answer = float('inf') 활용 
# -------------------------------------------------

def problem_5(arr, queries):
    result = []
    for s,e,k in queries:
        answer=1000000
        for i in range(s,e+1):
            if arr[i]>k and arr[i]<answer:
                answer=arr[i]
        if answer==1000000:
            answer=-1
        result.append(answer)  
    return result
