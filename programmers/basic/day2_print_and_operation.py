# -------------------------------------------------
# [문제 1] 덧셈식 출력하기
# https://school.programmers.co.kr/learn/courses/30/lessons/181947
# 📘 설명: 두 정수 a, b가 주어질 때 다음과 같은 형태의 계산식을 출력하는 문제
# 💡 배운 점: 값과 문자열 같이 출력할 때 굳이 공백 안 넣어도 알아서 공백 생김 
# -------------------------------------------------

def promblem_1():
  a, b = map(int, input().strip().split(' '))
  print(a, "+", b, "=", a+b)

# -------------------------------------------------
# [문제 2] 문자열 붙여서 출력하기 
# https://school.programmers.co.kr/learn/courses/30/lessons/181946
# 📘 설명: 두 개의 문자열 str1, str2가 공백으로 구분되어 입력으로 주어지면, 입출력 예와 같이 str1과 str2을 이어서 출력하는 문제
# 💡 배운 점: 복수 개의 문자를 출력할 때 공백 없이 출력하고 싶으면 + 활용 
# -------------------------------------------------

def promblem_2():
  str1, str2 = input().strip().split(' ')
  print(str1+str2)

# -------------------------------------------------
# [문제 3] 문자열 돌리기
# https://school.programmers.co.kr/learn/courses/30/lessons/181945
# 📘 설명: 문자열 str이 주어졌을 때, 문자열을 시계방향으로 90도 돌려서 아래 입출력 예와 같이 출력하는 문제
# 💡 배운 점: for i in range()의 괄호 안에는 정수만 가능. 문자열 넣으려면 for i in str 이런식으로 가능 
# -------------------------------------------------

def promblem_3():
  str = input()
  for i in range(len(str)):
      print(str[i])

# -------------------------------------------------
# [문제 4] 홀짝 구분하기 
# https://school.programmers.co.kr/learn/courses/30/lessons/181944
# 📘 설명: 자연수 n이 입력으로 주어졌을 때 만약 n이 짝수이면 "n is even"을, 홀수이면 "n is odd"를 출력하는 문제
# 💡 배운 점: 홀짝 구분에는 %로 나머지 연산자 사용하기. 
# -------------------------------------------------

def promblem_4():
  a = int(input())
  if a%2==0:
      print(a, "is even")
  else:
      print(a, "is odd")

# -------------------------------------------------
# [문제 5] 문자열 겹쳐쓰기
# https://school.programmers.co.kr/learn/courses/30/lessons/181943
# 📘 설명: 문자열 my_string, overwrite_string과 정수 s가 주어졌을 때, 문자열 my_string의 인덱스 s부터 overwrite_string의 길이만큼을 문자열 overwrite_string으로 바꾼 문자열을 return 하는 solution 함수를 작성하는 문제
# 💡 배운 점: python 문자열 슬라이싱 a[start:end]의 경우, 인덱스가 범위를 넘어가더라도 오류가 나지 않음. 넘어가도 그냥 공백으로 출
# -------------------------------------------------

def promblem_5(my_string, overwrite_string, s):
    answer = ''
    num = len(overwrite_string)
    answer = my_string[:s] + overwrite_string + my_string[s+num:]
    return answer
