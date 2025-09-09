# # # 키보드로 값 입력 받기
# # # a =  input()
# # # print('입력받은 값: ', a)

# # # 숫자 두개 입력 받기
# # n1 = input('첫번째 숫자를 입력하세요 : ')
# # n2 = input('두번째 숫자를 입력하세요 : ')
# # # 두 수의 합 구하기

# # # print('결과 : ', sum)
# # # input 함수로 받은 값은 str
# # # 형변환을 먼저 한다.

# # sum = int(n1) + int(n2)
# # print(sum)

# n1 = input('n1 : ')
# n2 = input('n2 : ')
# mul = int(n1) * int(n2)
# print(mul)

# n = input('이름입력 : ')
# a = input('나이입력 : ')
# print(f'{n}님의 나이는 {a}세 입니다')

# p = input('사과가격 : ')
# c = input('사과개수 : ')
# t = int(p) * int(c)
# print(f'사과 {c}개의 가격은 {t}입니다.')


# grade = input('점수 입력 : ')
# if int(grade) >= 60 :
#     print('합격')
# else :
#     print('불합격')

# age = input('나이입력 : ')
# if int(age) >= 0 and int(age) <= 12 :
#     print("1000원")
# elif int(age) >= 13 and int(age) <= 18 :
#     print("1800원")
# elif int(age) >= 19 :
#     print("2000원")


# # 조건을 잘 모르겠을 때 : 조건식을 True 로 표현
# while True :        # 무한루프 --> 블록에서 if 문 --> break
#     text = input('입력값 : ')
#     if text == '0' :
#         break
#     print(text)

# 키보드로 입력받기
# 모니터에 출력하기
# print : 화면에 숫자, 문자,리스트 등을 출력하는 함수

print('hello' 'world', end =' ')
print('hello', 'world', end =' ') # 쉼표를 쓰면 공백이 들어간다.
print('hello' + 'world', end =' ')
