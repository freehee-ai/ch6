# # # # 반대로 파일의 내용을 읽어오기

# # # # 읽기 모드로 파일 열기
# # # # 파일이름, 모드(w,r)
# # # f = open('새파일.txt','r')

# # # line = f.readline()     # 문자열로 읽어온다.
# # # lines = f.readlines()   # 리스트로 읽어온다.
# # # lines2 = f.read()       # 문자열 하나로 반환

# # # print(lines)
# # # # 문자열 안에 있는 알파벳을 하나씩 꺼내기
# # # # 함수의 인자 : 구분자
# # # # 리턴값이 있을 때
# # # lis = lines2.split(' ') # 구분자 : 공백
# # # # 리턴값이 없을 때
# # # lis.sort # 원본 변경하기 때문에 리턴값 받을 필요 없다?
# # # # 알파벳을 하나씩 출력하기
# # # for ch in lis :
# # #     print(ch)

# # # 반대로 파일 읽어오기
# # # 입력장치 : 키보드 -> 파일
# # # 키보드에서 값 입력받기
# # # input()
# # # 파일에서 값 읽어오기
# # # f.read()

# # f = open('file1.txt', 'r')
# # # 내용에 줄바꿈 포함됨 \n
# # lis = f.readlines()
# # for line in lis :
# #     print(line)

# # print(lis)

# # # 사용 후 닫기
# # f.close

# f = open('score.txt', 'r')
# lis = f.read()

# numbers_str = lis.split()
# print(numbers_str)

# sum = 0
# i = 0
# for n in numbers_str :
#     sum += int(n)
# print(sum)

# cnt = len(numbers_str)
# avg = sum / cnt
# print(avg)

f = open('numbers.txt', 'r')

num = f.readlines()
print(num)

# a = f.read()
# print(a)

# b = f.readline()
# print(b)

for n in num :
    if int(n) % 2 == 0 :
         print(n, end='')
    else :
        pass