# # # # # # # def mul(a,b) :
# # # # # # #     return a * b

# # # # # # # mul_num = mul(2,5)
# # # # # # # print(mul_num)

# # # # # # # # 함수의 여러가지 형태
# # # # # # # # 함수의 형태에 따라 호출하는 방법

# # # # # # # # 입력값, 반환값이 없는 함수
# # # # # # # # 인사를 출력하는 함수 만들기
# # # # # # # def hello() :
# # # # # # #     print('안녕하세요')
# # # # # # # # 함수 호출
# # # # # # # hello()

# # # # # # # # 입력값, 반환값이 있는 함수
# # # # # # # def add (a, b) :
# # # # # # #     return a + b
# # # # # # # result = add (3, 4)

# # # # # # # # 입력값 없고, 리턴값만 있는 함수
# # # # # # # # 인사를 반환하는 함수
# # # # # # # def say() :
# # # # # # #     return 'hi'
# # # # # # # # 리턴값이 있으면 결과를 받아야함
# # # # # # # string = say()
# # # # # # # print(string)

# # # # # # # # 입력값은 있고, 반환값은 없는 함수
# # # # # # # # 두 수를 더하고 결과를 바로 출력하는 함수
# # # # # # # def add(a,b) :
# # # # # # #     print(a + b)
# # # # # # # add(3,4)

# # # # # # # # 매개변수, 입력값, 인자
# # # # # # # # 함수 정의할 때 -- > 매개변수
# # # # # # # # 함수 호출할 때 -- > 인자
# # # # # # # # 프린트 콤마로 연결하면 공백생김
# # # # # # # # 포멧팅 연결 가능
# # # # # # # def welcome (str) :
# # # # # # #     return str
# # # # # # # name = welcome('둘리')
# # # # # # # print(f'{name} 님, 안녕하세요!')

# # # # # # # # def sayhi (str_hi) :
# # # # # # # #     return str_hi
# # # # # # # # say = sayhi("환영합니다.")

# # # # # # # # print(f'{name} 님 {say}')


# # # # # # # # 함수 응용하기
# # # # # # # # 입력한 숫자만큼 '안녕하세요' 출력하기
# # # # # # # # 입력값 : 반복횟수
# # # # # # # def hello(cnt) :
# # # # # # #     # cnt 번 출력하기
# # # # # # #     for _ in range(cnt) :
# # # # # # #         print('안녕하세요')
# # # # # # # # 매개변수가 있으면 입력값을 넣어서 함수 호출
# # # # # # # hello(5)


# # # # # # def func(a, b) :
# # # # # #     total = sum(range(a, b+1))
# # # # # #     return total

# # # # # # def sub(a, b) :
# # # # # #     sub_result = a - b
# # # # # #     if sub_result < 0 :
# # # # # #         return -999
# # # # # #     else :
# # # # # #         return sub_result
    
# # # # # # result1 = func(1, 3)
# # # # # # print(result1)

# # # # # # result2 = sub(10, 1)
# # # # # # print(result2)

# # # # # # # 함수 내부에서 결과 처리 : return x
# # # # # # # 함수를 사용하는 쪽에서 결과 처리 : retrun o
# # # # # # # # --> ex)여러 함수의 리턴값을 이용해 처리할 경우...
# # # # # # # # 함수 내부에 return 키워드 여러번 사용 가능
# # # # # # # # 단, 조건문과 함께 사용할 때만!


# # # # # # def func(a) :
# # # # # #     if a % 2 == 0 :
# # # # # #         print('짝수입니다.')
# # # # # #     else :
# # # # # #         print('홀수입니다.')

# # # # # # n = func(4)

# # # # # # # 블록을 가지는 것 : 함수, if, for
# # # # # # # 블록은 들여쓰기로 구분 : space x, tab o
# # # # # # # 블록은 변수의 scope(유효범위)

# # # # # # a = 10              # 전역 변수

# # # # # # if a % 2 == 0 :
# # # # # #     b = 5           # 지역 변수
# # # # # #     print(a, b)

# # # # # # print(a, b)

# # # # # # for n in range(10) :
# # # # # #     print(n)        # 지역 변수

# # # # # # def fun (x, y) :
# # # # # #     print(x, y)     # 지역 변수


# # # # # # fun(2,3)
# # # # # # print(x,y)
# # # # # # # 함수 블록 안에서 선언된 x, y는 지역변수로
# # # # # # # 함수 밖에서는 사용할 수 없다.


# # # # # def type_test (a) :
# # # # #     if type(a) == str :
# # # # #         print("문자입니다")
# # # # #     else :
# # # # #         pass

# # # # # n = type_test('메롱')
# # # # # m = type_test(1)
# # # # # b = type_test(True)

# # # # # print('\n')
# # # # # # ----------------------------------

# # # # # def func(a) :
# # # # #     if a > 0 :
# # # # #         print('양수입니다')
# # # # #     else :
# # # # #         pass

# # # # # num = func(8)
# # # # # num = func(-5)

# # # # # print('\n')
# # # # # # ----------------------------------

# # # # # def lis_func(lis) :
# # # # #     return lis[0]

# # # # # my_list = [1,2,3]
# # # # # result = lis_func(my_list)
# # # # # print(result)

# # # # # print('\n')
# # # # # # ----------------------------------

# # # # def func(a) :
# # # #     return len(a)

# # # # sentence = '파이썬'
# # # # result = func(sentence)
# # # # print(result)


# # # # def func(lis) :
# # # # # lis : 함수의 매개변수로 함수 내부에 선언됨
# # # #     return lis[0]
# # # # # my_lis : 함수에 전달하기 위한 리스트로, 메인에 선언됨
# # # # my_lis = [10,20,30]
# # # # # result : 함수의 결과를 저장하기 위한 변수로, 메인에 선언됨
# # # # result =  func(my_lis)
# # # # print(result)


# # # # # msg : 함수의 매개변수
# # # # def func(msg) :
# # # #     return len(msg)

# # # # # my_str1 : 함수를 호출할 때 입력할 문자열(생략가능)
# # # # my_str1 = 'abc' 
# # # # my_str2 = 'hello'

# # # # # result1 : 함수결과저장변수, abc 길이 저장
# # # # result1 = func(my_str1)
# # # # result2 = func(my_str2)

# # # def func (a) :
# # #     if a > 0 :
# # #         print('양수')
# # #     elif a < 0 :
# # #         print('음수')
# # #     else :
# # #         print('0 입니다')

# # # func(5)
# # # func(-6)
# # # func(0)

# # # # 에러가 나지 않는 형태로 구조를 만든 다음,
# # # # 그 후에 내용을 채워 넣는다.
# # # # 그래야 어디서 잘못되었는지 찾기 쉽다!


# # # def func(lis) :
# # #     sum_list = sum(lis)
# # #     print(sum_list)
# # # nums = [10,20,30]
# # # result = func(nums)

# # #

# # def func(lis) :
# #     hap = 0 # 합계(결과)를 저장할 변수
# #     for n in lis :
# #         hap = hap + n
# #     return hap
# # nums = [10,20,30]
# # result = func(nums)
# # print(result)



# def func(lis) :
#     for n1 in lis :
#         for n2 in range(1, 10) :
#             mul = n1 * n2
#             print(f"{n1} * {n2} = {mul}")
#         print()

# nums = [2,3,4,5,6,7,8,9]
# func(nums)


def func(lis) :
    cnt = 0
    for i in lis :
        if type(i) == str :
            cnt += 1
    print(cnt)

nums = [1, 'a', True, 'b']
func(nums)




