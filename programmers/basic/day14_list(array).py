# -------------------------------------------------
# [문제 1] 홀수 vs 짝수 
# https://school.programmers.co.kr/learn/courses/30/lessons/181887
# 📘 설명: 홀수 번째 원소들의 합과 짝수 번째 원소들의 합 중 큰 값을 return 하도록 solution 함수를 완성하는 문제 
# 💡 배운 점: 조건에 따라 더 큰 값을 return 하고 싶으면 return max(a, b) 활용 
# -------------------------------------------------

def problem_1(num_list):
    odd_sum = 0
    even_sum = 0
    for i in range(1,len(num_list)+1):
        if i%2==0:
            even_sum+=num_list[i-1]
        else:
            odd_sum+=num_list[i-1]
    return max(even_sum, odd_sum)
  
# -------------------------------------------------
# [문제 2] 5명씩
# https://school.programmers.co.kr/learn/courses/30/lessons/181886
# 📘 설명: 앞에서 부터 5명씩 묶은 그룹의 가장 앞에 서있는 사람들의 이름을 담은 리스트를 return하도록 solution 함수를 완성하는 문제 
# 💡 배운 점: for range를 1번부터 시작했다면 i번째 요소 뽑을 때, i-1로 해야하는 지 i로 해야하는지 잘 확인하고 진행하기 
# -------------------------------------------------

def problem_2(names):
    answer = []
    for i in range(1,len(names)+1,5):
        answer.append(names[i-1])
    return answer
  
# -------------------------------------------------
# [문제 3] 할 일 목록
# https://school.programmers.co.kr/learn/courses/30/lessons/181885
# 📘 설명: 오늘 해야 할 일이 담긴 문자열 배열 todo_list와 각각의 일을 지금 마쳤는지를 나타내는 boolean 배열 finished가 매개변수로 주어질 때, todo_list에서 아직 마치지 못한 일들을 순서대로 담은 문자열 배열을 return 하는 solution 함수를 작성하는 문제  
# 💡 배운 점: boolean은 True/False (앞은 대문자)  
# -------------------------------------------------

def problem_3(todo_list, finished):
    answer = []
    for i in range(len(todo_list)):
        if finished[i]==False:
            answer.append(todo_list[i])
    return answer
    
# -------------------------------------------------
# [문제 4] n보다 커질 때까지 더하기  
# https://school.programmers.co.kr/learn/courses/30/lessons/181884
# 📘 설명: 정수 배열 numbers와 정수 n이 매개변수로 주어집니다. numbers의 원소를 앞에서부터 하나씩 더하다가 그 합이 n보다 커지는 순간 이때까지 더했던 원소들의 합을 return 하는 solution 함수를 작성하는 문제  
# 💡 배운 점: python 증감 연산자는 a+=1 b-=1 이런 식으로만 가능 i++ 불가능!! 
# -------------------------------------------------

def problem_4(numbers, n):
    answer = 0
    i=0
    while (answer <= n):
        answer+=numbers[i]
        i+=1
    return answer
  
# -------------------------------------------------
# [문제 5] 수열과 구간 쿼리 1  
# https://school.programmers.co.kr/learn/courses/30/lessons/181883
# 📘 설명: 규칙에 따라 queries를 처리한 이후의 arr를 return 하는 solution 함수를 완성하는 문제 
# 💡 배운 점: 리스트 안에 요소를 1씩 더해주려면 arr[i] += 1 이런 식으로 증감연산자 활용 가능 
# -------------------------------------------------

def problem_5(arr, queries):
    for s, e in queries:
        for i in range(s,e+1):
            arr[i] += 1
          
    return arr
