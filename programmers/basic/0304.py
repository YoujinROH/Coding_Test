# -------------------------------------------------
# [문제 1] 나누어 떨어지는 숫자 배열 
# https://school.programmers.co.kr/learn/courses/30/lessons/12910
# 📘 설명: array의 각 element 중 divisor로 나누어 떨어지는 값을 오름차순으로 정렬한 배열을 반환하는 함수, solution을 작성하는 문제  
# 💡 배운 점: sort 함수 쓰는 법; 정렬할 리스트.sort(), 값 반환하지 않음.
# -------------------------------------------------

def solution1(arr, divisor):
    answer = []
    for i in range(len(arr)):
        if arr[i]%divisor==0:
            answer.append(arr[i])
    if not answer:
        answer.append(-1)
    answer.sort()
    return answer

# -------------------------------------------------
# [문제 2] 서울에서 김서방 찾기  
# https://school.programmers.co.kr/learn/courses/30/lessons/12919
# 📘 설명: String형 배열 seoul의 element중 "Kim"의 위치 x를 찾아, "김서방은 x에 있다"는 String을 반환하는 함수, solution을 완성하는 문제 
# 💡 배운 점: 문자열 배열에서 원하는 값을 인덱싱하고 싶을 경우. list.index('원하는 값')을 활용해주면, index 번호가 숫자로 반환됨.   
# -------------------------------------------------

def solution2(seoul):
    answer = "김서방은 "
    answer += str(seoul.index("Kim"))
    answer += "에 있다"
    return answer
  
# -------------------------------------------------
# [문제 3] 콜라츠 추측 
# https://school.programmers.co.kr/learn/courses/30/lessons/12943
# 📘 설명: 콜라츠 추측 작업을 몇 번이나 반복해야 하는지 반환하는 함수, solution을 완성하는 문제  
# 💡 배운 점: 조건 잘 생각하기 
# -------------------------------------------------

def solution3(num):
    answer = 0
    count = 0
    while(num!=1 and count<=500):
        if num%2==0:
            num=num/2
        else:
            num=num*3+1
        count+=1
    if count>500:
        return -1
    return count
    
# -------------------------------------------------
# [문제 4] 핸드폰 번호 가리기  
# https://school.programmers.co.kr/learn/courses/30/lessons/12948
# 📘 설명: 전화번호가 문자열 phone_number로 주어졌을 때, 전화번호의 뒷 4자리를 제외한 나머지 숫자를 전부 *으로 가린 문자열을 리턴하는 함수, solution을 완성하는 문제 
# 💡 배운 점: 기본 문제 
# -------------------------------------------------

def solution4(phone_number):
    answer = ''
    for i in range(len(phone_number)):
        if i<=(len(phone_number)-5):
            answer += '*'
        else:
            answer += str(phone_number[i])
    return answer
  
# -------------------------------------------------
# [문제 5] 가운데 글자 가져오기     
# https://school.programmers.co.kr/learn/courses/30/lessons/12903
# 📘 설명: 단어 s의 가운데 글자를 반환하는 함수를 완성하는 문제  
# 💡 배운 점: 인덱스 넘버를 연산할때 나눗셈 연산자는 사용하지 말기. float 형으로 나오기 때문에 인덱싱 오류남.  
# -------------------------------------------------

def solution5(s):
    answer = ''
    if len(s)%2==0:
        answer += s[len(s)//2-1]
        answer += s[len(s)//2]
    else:
        answer += s[len(s)//2]
    return answer
