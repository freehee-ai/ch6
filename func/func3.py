
# # # # # 함수 만들기
# # # # # 두 수의 차를 구하는 함수 정의
# # # # # 매개변수 : 함수에 필요한 입력값. 숫자 두개
# # # # # 반환값 : 두 수의 차를 구해서 결과를 반환
# # # # # 함수의 형태 : 입력값 있고 반환값 있음 -> 함수 내부에서 결과 확인x
# # # # # 함수 호출하는 쪽에서 결과 받고 확인할 것
# # # # def sub(n1, n2) :
# # # #     return n1 - n2

# # # # # 함수 호출
# # # # # 함수이름(함수에 필요한 값 입력)
# # # # result = sub(7,3)
# # # # print(result)

# # # # # 인자를 순서대로 입력 (n1, n2)
# # # # result = sub (7,3)
# # # # print(result)

# # # # # 인자를 순서와 상관없이 입력
# # # # # 매개변수의 이름을 직접 지정
# # # # result = sub(n2 = 3, n1 =7)
# # # # print(result) # ??????????????????????

# # # # # 문자열 두개를 입력받아 연결하는 함수 정의
# # # # def add_text(str1, str2) :
# # # #     print(str1 + ' ' + str2)      
# # # #     print(str1, str2)       # 쉼표는 자동 공백
# # # #     print(f'{str1} {str2}')
# # # # # 함수 호출
# # # # add_text('hello', 'world')

# # # # 두수를 입력 받아, 첫번째 수를 두번째 수로 나누고
# # # # 몫을 출력하는 함수
# # # # def divide(n1, n2) :
# # # #     if n2 == 0 :
# # # #         print('나누는 수는 0이 될 수 없습니다.')
# # # #         return
# # # #     print(n1 // n2)
# # # # # 함수 호출
# # # # divide(10,2)
# # # # divide(10,0)


# # # # 두 수를 더해서 합을 구하는 함수
# # # def add(n1, n2) :
# # #     if type(n1) != int or type(n2) != int :
# # #         return
# # #     else :
# # #         print(f'{n1} + {n2} = {n1 + n2}')

# # # # 함수 호출
# # # add(3, 4) 
# # # add(10, 20)
# # # add('aa','bb')

# # # 나이 입력, 성인여부 출력

# # def func (a) :
# #     if a > 19 :
# #         print('성인 입니다.')
# #     elif a < 0 :
# #         print('잘못된 입력입니다.')
# #         return
# #     else :
# #         print('성인이 아닙니다.')

# # func(20)
# # func(8)
# # func(-1)


# def info(name, age, gender) :
#     print(f'나의 이름은 {name} 입니다.')
#     print(f'나이는 {age} 살 입니다.')
#     if gender == 'm' :
#         print('남자입니다.')
#     else :
#         print('여자입니다.')

# # 함수호출
# info('둘리', 10, 'm')
# info('도우너', 8, 'f')


# 더하기 함수 만들기
def add(a, b) :
    return a + b

# 람다 함수 만들기 (익명함수)
# 변수 = lamda 매개변수 : 반환값
add = lambda a , b : a + b

# 람다 함수 호출
result = add(3,4)
print(result)

# 꼭 써야하는 것은 아님
# 복합 대입, 람다함수는 선택

# sort
# 목록을 순차적으로 정렬하는 함수
# 원본 변경하는 함수 --> 반환x
# 숫자 오름차순 정렬이 기본
# 문자를 정렬할 때는 람다 함수 필요
strings = ['foo', 'card', 'ba', 'aaa']

# 문자의 크기를 비교하는 함수
# 함수의 매개변수가 함수일 때,
# 람다식 함수를 활용
strings.sort(key = lambda s : len(s))
print(strings)
