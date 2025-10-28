🧠 Coding_Test

Python으로 코딩테스트 문제를 연습하고 알고리즘 개념을 정리하는 저장소입니다.
문제 사이트(Programmers, Baekjoon)별로 정리하며, 난이도에 따라 폴더를 구분했습니다.

📂 Folder Structure

programmers/

basic/ → Lv.0~Lv.1 입문 문제

intermediate/ → Lv.2~Lv.3 중급 문제

high/ → Lv.4 이상 고급 문제

baekjoon/

basic/ → 브론즈~실버4

intermediate/ → 실버~골드

high/ → 골드 이상

notes/ → 알고리즘 개념 정리 (예: BFS, DP 등)

templates/ → 자주 쓰는 코드 템플릿 (입출력, DFS/BFS 등)

📅 Study Plan
기간	목표	내용
10월	Python 문법 및 입출력 익히기	프로그래머스 Lv.0~1
11월	기본 알고리즘 익히기	정렬, 완전탐색, 재귀
12월	실전 감각 키우기	DFS/BFS, DP, 구현 문제
🧩 Example Problem

[Programmers] 문자열 뒤집기

# 문제: 문자열 뒤집기
# 목표: reversed() 없이 직접 구현해보기
# 배운 점: 문자열은 immutable, 슬라이싱으로 뒤집을 수 있음
def solution(my_string):
    return my_string[::-1]

🚀 Commit Rules
Prefix	설명
feat	새 문제 풀이 추가
fix	코드 수정 / 버그 수정
docs	노트나 README 추가
refactor	코드 구조 개선

예시 커밋 메시지

feat: solve 문자열 뒤집기 (programmers/basic)

docs: add BFS note

refactor: update input template

🪴 Log
날짜	학습 내용
10/27	문자열, 조건문 복습 / join(), split() 차이 정리
10/28	프로그래머스 Lv.0 배열 문제 3개 풀이
10/29	백준 브론즈 문제 2개 풀이 및 함수 연습
