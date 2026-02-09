# -------------------------------------------------
# [문제 1] 소수 만들기 
# https://school.programmers.co.kr/learn/courses/30/lessons/12977
# 📘 설명: 숫자들이 들어있는 배열 nums가 매개변수로 주어질 때, nums에 있는 숫자들 중 서로 다른 3개를 골라 더했을 때 소수가 되는 경우의 개수를 return 하도록 solution 함수를 완성하는 문
# 💡 배운 점: 인덱스의 합과 값의 합 구분하기  
# -------------------------------------------------

def solution1(nums):
    answer = 0

    for i in range(len(nums)-2):
        for j in range(i+1, len(nums)-1):
            for k in range(j+1, len(nums)):
                check = 0
                for l in range(2, nums[i]+nums[j]+nums[k]):
                    if (nums[i]+nums[j]+nums[k])%l==0:
                        check = 1
                        break
                if check == 0:
                    answer += 1
                    
    return answer

# -------------------------------------------------
# [문제 2] 예상 대진표 
# https://school.programmers.co.kr/learn/courses/30/lessons/12985
# 📘 설명: 게임 참가자 수 N, 참가자 번호 A, 경쟁자 번호 B가 함수 solution의 매개변수로 주어질 때, 처음 라운드에서 A번을 가진 참가자는 경쟁자로 생각하는 B번 참가자와 몇 번째 라운드에서 만나는지 return 하는 solution 함수를 완성하는 문제 
# 💡 배운 점: while (while문이 돌아갈 조건)  
# -------------------------------------------------

def solution2(n,a,b):
    answer = 0
    while(a!=b):
        answer += 1
        if a%2!=0:
            a=a+1
        if b%2!=0:
            b=b+1
        a=a//2
        b=b//2
    return answer
  
# -------------------------------------------------
# [문제 3] 숫자 짝꿍 
# https://school.programmers.co.kr/learn/courses/30/lessons/131128
# 📘 설명: 두 정수 X, Y가 주어졌을 때, X, Y의 짝꿍을 return하는 solution 함수를 완성하 문제 
# 💡 배운 점: 리스트 요소를 나중에 한번에 문자열로 바꾸고 싶으면 .join() 활용
# -------------------------------------------------

def solution3(X, Y):
    answer = ''
    dict_X = {0:0,1:0,2:0,3:0,4:0,5:0,6:0,7:0,8:0,9:0}
    dict_Y = {0:0,1:0,2:0,3:0,4:0,5:0,6:0,7:0,8:0,9:0}
    for i in range(len(str(X))):
        dict_X[int(str(X)[i])] += 1
    for j in range(len(str(Y))):
        dict_Y[int(str(Y)[j])] += 1
    for k in range(9,-1,-1):
        answer = answer + (str(k) * min(dict_X[k], dict_Y[k]))
        if k==0 and answer=="":
            answer = "-1"
        elif k==0 and answer[0]=="0":
            answer = "0"
    return answer
    
# -------------------------------------------------
# [문제 4] 올바른 괄호  
# https://school.programmers.co.kr/learn/courses/30/lessons/12909
# 📘 설명: '(' 또는 ')' 로만 이루어진 문자열 s가 주어졌을 때, 문자열 s가 올바른 괄호이면 true를 return 하고, 올바르지 않은 괄호이면 false를 return 하는 solution 함수를 완성하는 문제 
# 💡 배운 점: elif는 위에 if에 걸릴경우 그냥 지나가는 것 꼭 기억하기 
# -------------------------------------------------

def solution4(s):
    answer = True
    cnt_left = 0
    cnt_right = 0
    
    if s[0] != "(" or s[-1] != ")":
        return False
    
    for i in range(len(s)):
        if s[i] == "(":
            cnt_left += 1
        if s[i] == ")":
            cnt_right += 1
        if cnt_right > cnt_left:
            return False
    
    if cnt_right != cnt_left:
        return False

    return True
  
# -------------------------------------------------
# [문제 5] 최고의 집합  
# https://school.programmers.co.kr/learn/courses/30/lessons/12938
# 📘 설명: 집합의 원소의 개수 n과 모든 원소들의 합 s가 매개변수로 주어질 때, 최고의 집합을 return 하는 solution 함수를 완성하는 문제 
# 💡 배운 점: for range 문에서 step이 -1일 때는 step이 양수일때처럼 stop보다 클때까지만 반복 ex) (4, 2, -1) 이면 4, 3까지만 
# -------------------------------------------------

def solution5(n, s):
    first_num = s//n
    answer = [first_num] * n
    if s//n == 0:
        return [-1]
    elif s%n!=0:
        for i in range(n-1, n-(s%n)-1, -1):
            answer[i] += 1
    return answer
