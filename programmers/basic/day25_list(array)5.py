# -------------------------------------------------
# [문제 1] 정수를 나선형으로 배치하기
# https://school.programmers.co.kr/learn/courses/30/lessons/181832
# 📘 설명: n × n 배열에 1부터 n2 까지 정수를 인덱스 [0][0]부터 시계방향 나선형으로 배치한 이차원 배열을 return 하는 solution 함수를 작성하는 문제
# 💡 배운 점: 이차원 배열 사용해서 어떤 패턴을 가진 문제는 먼저 board=[[0] * n for _ in range(n)] 이런 식으로 배열 깔아두고 방향 개념 활용해서 진행하기 
# -------------------------------------------------

def problem_1(n):
    answer = [[0] * n for _ in range(n)]
    
    dx = [0,1,0,-1]
    dy = [1,0,-1,0]
    
    x,y = 0,0
    direction = 0
    
    for num in range(1, n*n+1):
        answer[x][y] = num
        
        nx = x + dx[direction]
        ny = y + dy[direction]
        
        if nx < 0 or nx >= n or ny < 0 or ny >= n or answer[nx][ny] != 0:
            direction = (direction + 1) % 4
            nx = x + dx[direction]
            ny = y + dy[direction]
            
        x, y = nx, ny
        
    return answer
  
# -------------------------------------------------
# [문제 2] 특별한 이차원 배열 2 
# https://school.programmers.co.kr/learn/courses/30/lessons/181831
# 📘 설명: n × n 크기의 이차원 배열 arr이 매개변수로 주어질 때, arr이 다음을 만족하면 1을 아니라면 0을 return 하는 solution 함수를 작성하는 문제  
# 💡 배운 점: 이차원 배열에서 등장하는 경우의 조건이 다 맞아야하는 때는 num count를 해서 최종 결과를 비교하기 
# -------------------------------------------------

def problem_2(arr):
    num = 0
    answer = 0
    for i in range(len(arr)):
        for j in range(len(arr)):
            if arr[i][j]==arr[j][i]:
                num += 1
    if num == len(arr)**2:
        answer = 1
    return answer
  
# -------------------------------------------------
# [문제 3] 정사각형으로 만들기  
# https://school.programmers.co.kr/learn/courses/30/lessons/181830
# 📘 설명: arr의 행의 수가 더 많다면 열의 수가 행의 수와 같아지도록 각 행의 끝에 0을 추가하고, 열의 수가 더 많다면 행의 수가 열의 수와 같아지도록 각 열의 끝에 0을 추가한 이차원 배열을 return 하는 solution 함수를 작성하는 문제 
# 💡 배운 점: [1,2,3]과 같은 여러 리스트 요소를 한번에 [0,0]와 같은 기존 리스트에 추가해서 [0,0,1,2,3]과 같이 만드려면 extend 함수 사용하
# -------------------------------------------------

def problem_3(arr):
    row = len(arr)
    col = len(arr[0])
    size = max(row, col)
    
    if col < row:
        for i in arr:
            i.extend([0] * (size - col))
        
    if row < col:
        for _ in range(size - row):
            arr.append([0] * size)
            
    return arr
    
# -------------------------------------------------
# [문제 4] 이차원 배열 대각선 순회하기
# https://school.programmers.co.kr/learn/courses/30/lessons/181829
# 📘 설명: 2차원 정수 배열 board와 정수 k가 주어졌을 때, i + j <= k를 만족하는 모든 (i, j)에 대한 board[i][j]의 합을 return 하는 solution 함수를 완성하는 문제
# 💡 배운 점: 항상 col 길이는 len(배열[0])이고 row 길이는 len(배열)로 차이가 있다는 것 기억하기 
# -------------------------------------------------

def problem_4(board, k):
    answer = 0
    for i in range(len(board)):
        for j in range(len(board[0])):
            if i + j <= k:
                answer += board[i][j]
    return answer
  
