# -------------------------------------------------
# [문제 1] 제일 작은 수 제거하기  
# https://school.programmers.co.kr/learn/courses/30/lessons/12935
# 📘 설명: 정수를 저장한 배열, arr 에서 가장 작은 수를 제거한 배열을 리턴하는 함수, solution을 완성하는 문제  
# 💡 배운 점: 리스트의 요소를 삭제하는 3가지 방법; remove, pop, del; 리스트.remove('값'), 리스트.pop(인덱스), del 리스트[인덱스(슬라이싱 가능)]
# -------------------------------------------------

def solution1(arr):
    arr.remove(min(arr))
    if not arr:
        return [-1]
    return arr

# -------------------------------------------------
# [문제 2] 내적  
# https://school.programmers.co.kr/learn/courses/30/lessons/70128
# 📘 설명: 길이가 같은 두 1차원 정수 배열 a, b가 매개변수로 주어졌을 때, a와 b의 내적을 return 하도록 solution 함수를 완성하는 문제 
# 💡 배운 점: 기본 문제    
# -------------------------------------------------

def solution2(a, b):
    answer = 0
    for i in range(len(a)):
        answer += a[i]*b[i]
    return answer
  
# -------------------------------------------------
# [문제 3] 수박수박수박수박수박수? 
# https://school.programmers.co.kr/learn/courses/30/lessons/12922
# 📘 설명: 길이가 n이고, "수박수박수박수...."와 같은 패턴을 유지하는 문자열을 리턴하는 함수, solution을 완성하는 문제   
# 💡 배운 점: 기본 문제  
# -------------------------------------------------

def solution3(n):
    answer = ''
    for i in range(n):
        if i%2==0:
            answer += "수"
        else:
            answer += "박"
    return answer
    
# -------------------------------------------------
# [문제 4] 약수의 개수와 덧셈  
# https://school.programmers.co.kr/learn/courses/30/lessons/77884
# 📘 설명: left부터 right까지의 모든 수들 중에서, 약수의 개수가 짝수인 수는 더하고, 약수의 개수가 홀수인 수는 뺀 수를 return 하도록 solution 함수를 완성하는 문제 
# 💡 배운 점: 아래와 같은 완전 탐색은 시간 복잡도 O(n). i가 약수이면 n//i도 약수이므로 루프를 n**0.5 즉 루트 n까지만 돌아도 됨. 다만 약수를 직접 반환해야할 때는 n//i도 추가해서 반환하기.
# -------------------------------------------------

def solution4(left, right):
    answer = 0
    for i in range(left, right+1):
        cnt = 0
        for j in range(1,i+1):
            if i%j==0:
                cnt += 1
        if cnt%2==0:
            answer += i
        else:
            answer -= i
    return answer
  
# -------------------------------------------------
# [문제 5] 문자열 내림차순으로 배치하기      
# https://school.programmers.co.kr/learn/courses/30/lessons/12917
# 📘 설명: 문자열 s에 나타나는 문자를 큰것부터 작은 순으로 정렬해 새로운 문자열을 리턴하는 함수, solution을 완성하는 문제 
# 💡 배운 점: 문자열 한 덩어리 하나의 각각 알파벳을 리스트 요소화 하려면 그냥 새리스트변수=list(문자열)로 하면 됨. join 함수는 새로운변수=구분자.join(합칠리스트)로 사용하는 것 기억하기. sort는 리스트.sort()이지만, sorted는 새변수=sorted(리스트)임. 
# -------------------------------------------------

def solution5(s):
    char_list = list(s)
    char_list.sort(reverse=True)
    answer = "".join(char_list)
    return answer
    return answer
