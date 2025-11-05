# -------------------------------------------------
# [문제 1] 문자열의 앞의 n글자
# https://school.programmers.co.kr/learn/courses/30/lessons/181907
# 📘 설명: 문자열 my_string과 정수 n이 매개변수로 주어질 때, my_string의 앞의 n글자로 이루어진 문자열을 return 하는 solution 함수를 작성하는 문제 
# 💡 배운 점: 슬라이싱 [start:stop:step] 실제 인덱스는 stop-1까지만 반복 진행 
# -------------------------------------------------

def problem_1(my_string, n):
    answer = ''
    answer = my_string[:n]
    return answer

# -------------------------------------------------
# [문제 2] 접두사인지 확인하기 
# https://school.programmers.co.kr/learn/courses/30/lessons/181906
# 📘 설명: 문자열 my_string과 is_prefix가 주어질 때, is_prefix가 my_string의 접두사라면 1을, 아니면 0을 return 하는 solution 함수를 작성하는 문제 
# 💡 배운 점: 슬라이싱할때 stop-1까지만 진행된다는 것 명심하기 
# -------------------------------------------------

def problem_2(my_string, is_prefix):
    answer = 0
    string_list = []
    for i in range(len(my_string)):
        string_list.append(my_string[:i+1])
    if is_prefix in string_list:
        answer = 1
    return answer
  
# -------------------------------------------------
# [문제 3] 문자열 뒤집기 
# https://school.programmers.co.kr/learn/courses/30/lessons/181905
# 📘 설명: 문자열 my_string과 정수 s, e가 매개변수로 주어질 때, my_string에서 인덱스 s부터 인덱스 e까지를 뒤집은 문자열을 return 하는 solution 함수를 작성하는 문제 
# 💡 배운 점: my_string[e:s-1:-1]와 같이 역슬라이싱일때 인덱스가 0(s=0)에 가까우면 문제가 발생할 수 있음. step이 양수일때는 end 직전까지 포함 step이 음수일때는 end 다음까지 포함. step=-1일때, start가 end보다 왼쪽에 있으면 결과는 빈 문자열. 특히 end가 -1을 의미하면 방향이 반대라 슬라이싱이 아무것도 반환하지 않음. 그래서 이때는 음수 슬라이싱 대신 정방향 슬라이싱 [::-1]을 쓰는게 안전함.
# -------------------------------------------------

def problem_3(my_string, s, e):
    answer = ''
    answer = my_string[:s]+my_string[s:e+1][::-1]+my_string[e+1:]
    return answer
    
# -------------------------------------------------
# [문제 4] 세로 읽기 
# https://school.programmers.co.kr/learn/courses/30/lessons/181904
# 📘 설명: my_string을 한 줄에 m 글자씩 가로로 적었을 때 왼쪽부터 세로로 c번째 열에 적힌 글자들을 문자열로 return 하는 solution 함수를 작성하는 문제 
# 💡 배운 점: out of range 유의하기 
# -------------------------------------------------

def problem_4(my_string, m, c):
    answer = ''
    for i in range(len(my_string)//m):
        answer+=my_string[m*i+c-1]
    return answer
  
# -------------------------------------------------
# [문제 5] qr code  
# https://school.programmers.co.kr/learn/courses/30/lessons/181908
# 📘 설명: 두 정수 q, r과 문자열 code가 주어질 때, code의 각 인덱스를 q로 나누었을 때 나머지가 r인 위치의 문자를 앞에서부터 순서대로 이어 붙인 문자열을 return 하는 solution 함수를 작성하는 문제 
# 💡 배운 점: 나머지 연산자 %  
# -------------------------------------------------

def problem_5(q, r, code): 
    answer = ''
    for i in range(len(code)):
        if i%q==r:
            answer+=code[i]
    return answer
