# -------------------------------------------------
# [문제 1] 0 떼기 (progress)
# https://school.programmers.co.kr/learn/courses/30/lessons/181857
# 📘 설명: arr의 길이가 2의 정수 거듭제곱이 되도록 arr 뒤에 정수 0을 추가하려고 할 때, arr에 최소한의 개수로 0을 추가한 배열을 return 하는 solution 함수를 작성하는 문제 
# 💡 배운 점: [0] * n 이런식으로 [0,0,0,0,...] 리스트를 만들어갈 수 있음. 리스트도 문자열처럼 += 로 합칠 수 있음. append 대체로 활용 가능.
# -------------------------------------------------

def problem_1(arr):
    answer = 1
    n = len(arr)
    
    while (answer < n):
        answer*=2
    
    arr += [0] * (answer - n)
    return arr
  
# -------------------------------------------------
# [문제 2] 두 수의 합 (progress)
# https://school.programmers.co.kr/learn/courses/30/lessons/181856
# 📘 설명: 두 정수 배열 arr1과 arr2가 주어질 때, 위에서 정의한 배열의 대소관계에 대하여 arr2가 크다면 -1, arr1이 크다면 1, 두 배열이 같다면 0을 return 하는 solution 함수를 작성하는 문제 
# 💡 배운 점: 리스트 안의 요소의 합을 구할 때는 sum() 함수 활용하기 
# -------------------------------------------------

def problem_2(arr1, arr2):
    if len(arr1)!=len(arr2):
        if len(arr1) > len(arr2):
            return 1
        else:
            return -1
    else:
        if sum(arr1) > sum(arr2):
            return 1
        elif sum(arr1) < sum(arr2):
            return -1
        else:
            return 0
  
# -------------------------------------------------
# [문제 3] 문자열 변환 (progress)
# https://school.programmers.co.kr/learn/courses/30/lessons/181855
# 📘 설명: strArr의 원소들을 길이가 같은 문자열들끼리 그룹으로 묶었을 때 가장 개수가 많은 그룹의 크기를 return 하는 solution 함수를 완성하는 문제 
# 💡 배운 점: 비교 연산자 == 랑 대입 연산자 = 헷갈리지 않기. 딕셔너리 밸류값을 뽑으려면 dict.values() 활용하기 
# -------------------------------------------------

def problem_3(strArr):
    answer = {}
    for word in strArr:
        if len(word) not in answer:
            answer[len(word)] = 1
        else:
            answer[len(word)] += 1
    return max(answer.values())
    
# -------------------------------------------------
# [문제 4] 배열의 원소 삭제하기 
# https://school.programmers.co.kr/learn/courses/30/lessons/181854
# 📘 설명: arr의 길이가 홀수라면 arr의 모든 짝수 인덱스 위치에 n을 더한 배열을, arr의 길이가 짝수라면 arr의 모든 홀수 인덱스 위치에 n을 더한 배열을 return 하는 solution 함수를 작성하는 문제 
# 💡 배운 점: 인덱스 기준 짝수이면 0, 2, 4,... 인덱스를 의미 
# -------------------------------------------------

def problem_4(arr, n):
    if len(arr)%2!=0:
        for i in range(len(arr)):
            if i%2==0:
                arr[i]+=n
    else:
        for i in range(len(arr)):
            if i%2!=0:
                arr[i]+=n          
    return arr
  
# -------------------------------------------------
# [문제 5] 부분 문자열인지 확인하기  
# https://school.programmers.co.kr/learn/courses/30/lessons/181853
# 📘 설명: num_list에서 가장 작은 5개의 수를 오름차순으로 담은 리스트를 return하도록 solution 함수를 완성하는 문제 
# 💡 배운 점: sort() 함수는 반환값이 None이므로 num_list.sort()[:5] 이런식으로 바로 정렬과 인덱싱은 동시에는 불가능 
# -------------------------------------------------

def problem_5(num_list):
    num_list.sort()
    return num_list[:5]
    return answer
