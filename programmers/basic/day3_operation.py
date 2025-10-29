# -------------------------------------------------
# [문제 1] 문자열 섞기
# https://school.programmers.co.kr/learn/courses/30/lessons/181942
# 📘 설명: 길이가 같은 두 문자열 str1과 str2가 주어졌을 때, 두 문자열의 각 문자가 앞에서부터 서로 번갈아가면서 한 번씩 등장하는 문자열을 만들어 return 하는 solution 함수를 완성하는 문제
# 💡 배운 점: 문자열은 + 활용하여 합칠 수 있는 것 활용하기
# -------------------------------------------------

def problem_1(str1, str2):
    answer = ''
    for i in range(len(str1)):
        answer += str1[i]
        answer += str2[i]
    return answer

# -------------------------------------------------
# [문제 2] 문자 리스트를 문자열로 변환하기 
# https://school.programmers.co.kr/learn/courses/30/lessons/181941
# 📘 설명: 문자들이 담겨있는 배열 arr가 주어졌을 때, arr의 원소들을 순서대로 이어 붙인 문자열을 return 하는 solution함수를 작성하는 문제
# 💡 배운 점: list indices must be integers or slices, not str 
# -------------------------------------------------

def problem_2(arr):
    answer = ''
    for i in arr:
        answer += i
    return answer
  
# -------------------------------------------------
# [문제 3] 문자열 곱하기
# https://school.programmers.co.kr/learn/courses/30/lessons/181940
# 📘 설명: 문자열 my_string과 정수 k가 주어질 때, my_string을 k번 반복한 문자열을 return 하는 solution 함수를 작성하는 문제
# 💡 배운 점: 문자열 여러번 출력하고 싶으면 *연산 사용
# -------------------------------------------------

def problem_3(my_string, k):
    answer = ''
    answer = my_string * k
    return answer

# -------------------------------------------------
# [문제 4] 더 크게 합치기
# https://school.programmers.co.kr/learn/courses/30/lessons/181939
# 📘 설명: 양의 정수 a와 b가 주어졌을 때, a ⊕ b와 b ⊕ a 중 더 큰 값을 return 하는 solution 함수를 완성하는 문제
# 💡 배운 점: 문자열로 해결할 수 있는 경우는 자릿수 비교 말고 문자열로 해결, 거듭제곱 연산은 **
# -------------------------------------------------

def problem_4(a, b):
    answer = 0
    word1 = str(a)
    word2 = str(b)
    if int(word1+word2) >= int(word2+word1):
        answer=int(word1+word2)
    else:
        answer=int(word2+word1)
    return answer

# -------------------------------------------------
# [문제 5] 두 수의 연산값 비교하기
# https://school.programmers.co.kr/learn/courses/30/lessons/181938
# 📘 설명: 양의 정수 a와 b가 주어졌을 때, a ⊕ b와 2 * a * b 중 더 큰 값을 return하는 solution 함수를 완성하는 문제
# 💡 배운 점: ⊕연산은 그냥 문자열 합치기로 접근 
# -------------------------------------------------

def problem_5(a, b):
    answer = 0
    if int(str(a)+str(b)) >= 2*a*b:
        answer=int(str(a)+str(b))
    else:
        answer=2*a*b
    return answer
