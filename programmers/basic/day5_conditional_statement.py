# -------------------------------------------------
# [문제 1] 코드 처리하기
# https://school.programmers.co.kr/learn/courses/30/lessons/181932
# 📘 설명: 문자열 code를 통해 만들어진 문자열 ret를 return 하는 solution 함수를 완성하는 문제
# 💡 배운 점: 문자열 "1"과 정수 1 구분하기, “빈 결과(default)”는 함수의 마지막 return 직전에 처리, A if 조건 else B
# -------------------------------------------------

def problem_1(code):
    ret = ''
    mode = 0
    for idx in range(len(code)):
        if code[idx]=="1":
            mode=1-mode
        elif mode==0 and idx%2==0:
            ret+=code[idx]
        elif mode==1 and idx%2!=0:
            ret+=code[idx]
    return ret if ret else "EMPTY"

# -------------------------------------------------
# [문제 2] 등차수열의 특정한 항만 더하기
# https://school.programmers.co.kr/learn/courses/30/lessons/181931
# 📘 설명: 두 정수 a, d와 길이가 n인 boolean 배열 included가 주어질 때, 첫째항이 a, 공차가 d인 등차수열에서 included[i]가 i + 1항을 의미할 때, 이 등차수열의 1항부터 n항까지 included가 true인 항들만 더한 값을 return 하는 solution 함수를 작성하는 문제 
# 💡 배운 점: boolean true는 1, false는 0
# -------------------------------------------------

def problem_2(a, d, included):
    answer = 0
    for i in range(len(included)):
        if included[i]==1:
            answer+=a+(d*i)
    return answer
  
# -------------------------------------------------
# [문제 3] 주사위 게임2
# https://school.programmers.co.kr/learn/courses/30/lessons/181930
# 📘 설명: 세 정수 a, b, c가 매개변수로 주어질 때, 얻는 점수를 return 하는 solution 함수를 작성하는 문제
# 💡 배운 점: 조건문 작성시에는 표현이 쉬운 조건문 먼저 if, elif로 걸러내고 나머지는 else로 묶어버리는 접근법 활용하기 
# -------------------------------------------------

def problem_3(a, b, c):
    answer = 0
    if a!=b and b!=c and a!=c:
        answer = a+b+c
    elif a==b and b==c and a==c:
        answer = (a+b+c)*(a**2+b**2+c**2)*(a**3+b**3+c**3)
    else:
        answer = (a+b+c)*(a**2+b**2+c**2)
    return answer

# -------------------------------------------------
# [문제 4] 원소들의 곱과 합
# https://school.programmers.co.kr/learn/courses/30/lessons/181929
# 📘 설명: 정수가 담긴 리스트 num_list가 주어질 때, 모든 원소들의 곱이 모든 원소들의 합의 제곱보다 작으면 1을 크면 0을 return하도록 solution 함수를 완성하는 문제
# 💡 배운 점: 숫자들의 곱 구할 때, 0되지 않게 조심하기 
# -------------------------------------------------

def problem_4(num_list):
    answer1 = 1
    answer2 = 0
    for i in range(len(num_list)):
        answer1 *= num_list[i]
        answer2 += num_list[i]
    if answer1 < (answer2**2):
        return 1
    else:
        return 0

# -------------------------------------------------
# [문제 5] 이어 붙인 수
# https://school.programmers.co.kr/learn/courses/30/lessons/181928
# 📘 설명: 정수가 담긴 리스트 num_list가 주어집니다. num_list의 홀수만 순서대로 이어 붙인 수와 짝수만 순서대로 이어 붙인 수의 합을 return하도록 solution 함수를 완성하는 문제
# 💡 배운 점: return 너무 정적으로 활용하지 않기 
# -------------------------------------------------

def problem_5(num_list):
    answer_odd = ""
    answer_even = ""
    for i in range(len(num_list)):
        if num_list[i]%2==0:
            answer_even += str(num_list[i])
        else:
            answer_odd += str(num_list[i])
    return int(answer_odd)+int(answer_even)
