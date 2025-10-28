# -------------------------------------------------
# [문제 1] 문자열 출력하기
# https://school.programmers.co.kr/learn/courses/30/lessons/181952
# 📘 설명: 문자열 str이 주어질 때, 그대로 출력하는 문제
# 💡 배운 점: input() / print() 기본 입출력 확인
# -------------------------------------------------

def promblem_1():
  str = input()
  print(str)

# -------------------------------------------------
# [문제 2] a와 b 출력하기
# https://school.programmers.co.kr/learn/courses/30/lessons/181951
# 📘 설명: 정수 a와 b가 주어질 때, 각 수를 입력받아 입출력 예와 같은 형식으로 출력하는 문제
# 💡 배운 점: map(function, iterable1, ... , iterablen); function: 각 요소에 적용할 함수, iterable: 함수를 적용할 데이터 집합
# -------------------------------------------------

def promblem_2():
  a, b = map(int, input().strip().split(' '))
  print('a =',a)
  print('b =',b)

# -------------------------------------------------
# [문제 3] 문자열 반복해서 출력하기
# https://school.programmers.co.kr/learn/courses/30/lessons/181950
# 📘 설명: 문자열 str과 정수 n이 주어졌을 때, str이 n번 반복된 문자열을 만들어 출력하는 문제
# 💡 배운 점: strip(): 양쪽 공백 제거, split(' '): 공백 기준으로 문자를 나눔
# -------------------------------------------------

def promblem_3():
  str, n = input().strip().split(' ')
  n = int(n)
  print(n*str)

# -------------------------------------------------
# [문제 4] 대소문자 바꿔서 출력하기
# https://school.programmers.co.kr/learn/courses/30/lessons/181949
# 📘 설명: 영어 알파벳으로 이루어진 문자열 str이 주어졌을 때, 각 알파벳을 대문자는 소문자로 소문자는 대문자로 변환해서 출력하는 문제
# 💡 배운 점: 해당 문자열.swapcase(): 대소문자 변환 한 번에 가능
# -------------------------------------------------

def promblem_4():
  str = input()
  print(str.swapcase())

# -------------------------------------------------
# [문제 5] 특수문자 출력하기
# https://school.programmers.co.kr/learn/courses/30/lessons/181948
# 📘 설명: 다음과 같이 출력하는 문제 (!@#$%^&*(\'"<>?:;)
# 💡 배운 점: \, ', " 출력을 위해서는 \ 필수
# -------------------------------------------------

def promblem_5():
  print('!@#$%^&*(\\\'\"<>?:;')
