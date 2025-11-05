# -------------------------------------------------
# [문제 1] 문자 개수 세기 
# https://school.programmers.co.kr/learn/courses/30/lessons/181902
# 📘 설명: 알파벳 대소문자로만 이루어진 문자열 my_string이 주어질 때, my_string에서 'A'의 개수, my_string에서 'B'의 개수,..., my_string에서 'Z'의 개수, my_string에서 'a'의 개수, my_string에서 'b'의 개수,..., my_string에서 'z'의 개수를 순서대로 담은 길이 52의 정수 배열을 return 하는 solution 함수를 작성하는 문제 
# 💡 배운 점: ord(char)을 활용하면 아스키 코드 숫자를 반환할 수 있음. 대문자 A 기준 소문자 a는 +26. 예를 들어 ord('A')+26=ord('a') 
# -------------------------------------------------

def problem_1(my_string):
    answer = []
    alphabet = {'A':0,'B':0,'C':0,'D':0,'E':0,'F':0,'G':0,'H':0,'I':0,'J':0,'K':0,'L':0,'M':0,'N':0,'O':0,'P':0,'Q':0,'R':0,'S':0,'T':0,'U':0,'V':0,'W':0,'X':0,'Y':0,'Z':0,'a':0,'b':0,'c':0,'d':0,'e':0,'f':0,'g':0,'h':0,'i':0,'j':0,'k':0,'l':0,'m':0,'n':0,'o':0,'p':0,'q':0,'r':0,'s':0,'t':0,'u':0,'v':0,'w':0,'x':0,'y':0,'z':0}
    for char in my_string:
        if char in alphabet:
            alphabet[char]+=1
    answer = list(alphabet.values())
    return answer

# -------------------------------------------------
# [문제 2] 배열 만들기 1
# https://school.programmers.co.kr/learn/courses/30/lessons/181901
# 📘 설명: 정수 n과 k가 주어졌을 때, 1 이상 n이하의 정수 중에서 k의 배수를 오름차순으로 저장한 배열을 return 하는 solution 함수를 완성하는 문제 
# 💡 배운 점: k의 배수를 순차적으로 저장하려면 for range 문 사용해서 step을 k로 두기 
# -------------------------------------------------

def problem_2(n, k):
    answer = []
    for i in range(k,n+1,k):
        answer.append(i)
    answer.sort()
    return answer
  
# -------------------------------------------------
# [문제 3] 글자 지우기  
# https://school.programmers.co.kr/learn/courses/30/lessons/181900
# 📘 설명: 문자열 my_string과 정수 배열 indices가 주어질 때, my_string에서 indices의 원소에 해당하는 인덱스의 글자를 지우고 이어 붙인 문자열을 return 하는 solution 함수를 작성하는 문제 
# 💡 배운 점: 어떤 리스트에 있는 인덱스 제외 문자만 선택하여 문자열을 만들 때는 not in 조건문 사용하기 
# -------------------------------------------------

def problem_3(my_string, indices): 
    answer = ''
    for i in range(len(my_string)):
        if i not in indices:
            answer+=my_string[i]
    return answer
    
# -------------------------------------------------
# [문제 4] 카운트 다운 
# https://school.programmers.co.kr/learn/courses/30/lessons/181899
# 📘 설명: 정수 start_num와 end_num가 주어질 때, start_num에서 end_num까지 1씩 감소하는 수들을 차례로 담은 리스트를 return하도록 solution 함수를 완성하는 문제 
# 💡 배운 점: for i in range(start, end, step)
# -------------------------------------------------

def problem_4(start_num, end_num):
    answer = []
    for i in range(start_num,end_num-1,-1):
        answer.append(i)
    return answer
  
# -------------------------------------------------
# [문제 5] 가까운 1 찾기 
# https://school.programmers.co.kr/learn/courses/30/lessons/181898
# 📘 설명: 정수 idx가 주어졌을 때, idx보다 크면서 배열의 값이 1인 가장 작은 인덱스를 찾아서 반환하는 solution 함수를 완성하는 문제 
# 💡 배운 점: for range문을 쓰는 문제일 때, start와 end가 정확히 어디인지 확인하기 
# -------------------------------------------------

def problem_5(arr, idx): 
    answer = 0
    for i in range(idx, len(arr)):
        if arr[i] == 1:
            answer=i
            break
        else:
            if i==len(arr)-1:
                answer=-1
    return answer
