# # 함수 만들기
# # 값을 하나 입력받고 출력하기
# def func1(a) :
#     print(a)


# # 함수 호출하기
# func1(1)

# # 값을 두개 입력받고 호출하는 함수 만들기
# def func2(a, b) :
#     print(a, b)

# func2(1, 2)

# # 값을 3개 입력받고 호출하는 함수 만들기
# def func3(a, b, c) :
#     print(a, b, c)

# func3(1,2,3)

# # 매개변수의 개수가 달라져도 사용할 수 있는 함수 만들기
# # 나머지 매개변수
# # 나머지 매개변수를 만들때는 ** 별 두개
# def func(**kwargs) :
#     print(kwargs)

# # 함수 호출
# # 나머지 매개변수는 딕셔너리 형태로 저장됨
# func(a = 1)                 # {'a': 1}
# func(a = 1, b = 2)          # {'a': 1, 'b': 2}


# # 나머지 매개변수를 사용하는 함수 만들기
# # 사람의 정보를 입력받아 출력하는 함수 만들기
# def info(**kwargs) :
#     print(kwargs)

# info(name = "둘리", age = 10)       # 주소모름
# info(name = '도우너', age = 8, adress = '서울')

# # 딕셔너리를 초기화할 때와, 함수 내부에서 사용할 때 다르게 표현
# dic = {'name':'둘리', 'age':10}
# # 딕셔너리의 함수들
# print(dic.keys())   # keys 는 순회가능한 이터러블 객체
# print(dic.values())
# # items 객체의 요소는 tuple
# print(dic.items())
      


# def calc(**kwargs) :
#     print(kwargs.keys())
# # 함수호출
# calc(apple=1200, banana = 800, orange = 1500)

# def show_scores(**kwargs):
#     print(kwargs.values())
# show_scores(철수=90, 영희=85, 민수=100)

# def show_population(**kwargs) :
#     print(kwargs.items())
# show_population(seoul=950, busan=340, incheon=300)

# def show_items(**kwargs) :
#     print(kwargs.keys())
# show_items(milk=2500, bread=2000, egg=3000)
