# 1. 기본입출력
# n = input()
# print(n+10) # why occured error?
# n = int(input())
# print(n+10)
# n = input().split()
# print(f"n : {n}")
# a,b = map(int, input().split())
# print(f" a : {a}, b : {b}")
# 2. 데이터 구조(), 타입(str, int, float)
# 3. 리스트, 튜플, 셋, 딕셔너리
# n = [1,2,3,4,5,6,7,'10',5.0]
# print(n)
# print(type(n))
# from random import randint
# L = []
# L.append(10)
# L.pop()
# for i in range(10):
#     L.append(randint(1, 30))
# L.sort()
# print(L)
# n = 1,2,3
# n = (1,2,3)
# print(n)
# print(type(n))
# L = [1,2,3,4]
# L[0] = 10
# print(L)
# s = set([1,1,2,3, "시발", "시발"])
# print(s)
# print(type(s))
# L = list(s)
# print(L)
# D = {"정" : "용훈", "윤" : "현웅"}
# print(D["정"])
# print(D["윤"])
# D["신"] = "원섭"
# D["박"] = "성일"
# D["우"] = "성민"
# print(D)
# 4. 반복문(while, for), 중첩반복문, 함수, 재귀함수
# 4.1. 0 이 입력되기 전까지 무한 반복하면서 
# 입력된 값중 가장 큰 값을 출력해보세요
# m = -1
# while(True):
#     a = int(input())
#     if ( a == 0 ):
#         break
#     elif ( m < a ):
#         m = a
# print(f" 가장 큰 값 :  {m} ")
# for?
# 4.1. for i in range(10):
# for i in range(1, 30, 2):
#     print(i) # 1~29, 2씩 증가
# for i in range(1, 30):
#     print(i) # 1~29
# for i in range(30):
#     print(i) # 0~29
# 4.2. for i in L:
# L = [1,2,3,4,5]
# for i in L:
#     print(i)
# # 4.3. for i in s:
# s = "윤현웅켜잡다"
# for i in s:
#     print(i)
# 4.4 함수
# def f(a,b):
#     y = a+b
#     return y
# y = f(10, 20)
# print(y) 
# 4.5. 재귀함수
# for i in range(1, 10):
#     print(i)
# def test(n):
#     if ( n == 0 ):
#         return
#     print(n)
#     test(n-1)
# test(10)
# 5. 클래스, 상속, 메소드오버라이딩, 접근제어자
# class 붕어빵틀:
#     def __init__(self, 재료):
#         self.재료 = 재료
#         print("붕어빵 완성")

#     def eat(self):
#         print(self.재료, "냠냠")
# class 사람:
#     def __init__(self, 이름):
#         self.이름 = 이름
#         print(self.이름, "탄생!")
#     def eat(self, 붕어빵):
#         print(self.이름, f"가 {붕어빵.재료} 붕어빵 냠냠 합니다.")
# 현웅 = 사람("윤현웅")
# 붕어빵1 = 붕어빵틀("탄내나는")
# 붕어빵2 = 붕어빵틀("팥맛")
# 현웅.eat(붕어빵1)
# 현웅.eat(붕어빵2)
# class 아빠:
#     def __init__(self):
#         self.money = 1000000
#     def 자동차(self):
#         print("람보르기니")
# class 아들(아빠):
#     def 자동차(self):
#         super().자동차()
# father = 아빠()
# son = 아들()
# print(son.money)
# print(son.자동차())
# def f(x):
#     print(10)
# print(f(10))
# 6. 모듈 # pip, conda
# import 파일명
# import helloworld as h
# h.test(10)
# from helloworld import test as t
# t(10)
# import lib.sex as ls
# ls.윤현웅()