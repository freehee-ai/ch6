
# # file
# # 이전 입출력 장치 : 키보드와 모니터

# # 파일 열기
# # open(파일이름, 모드)
# # 파일이 있으면 연결, 없으면 새로 생성됨
# f = open('새파일.txt', 'w')
# f = open('file1.txt', 'w')
# # 파일에 내용 쓰기
# #
# f.write('a b c d e')
# for n in range(1, 11) :
#     # write 함수의 매개변수는 int
#     # int - > str
#     f.write(str(n))

# # 파일 닫기
# # 닫지 않아도 문제는 없지만, 닫지 않으면 메모리 낭비
# f.close()

# 한글 입력시 인코딩 설정
f = open('file2.txt', 'w', encoding='utf-8')
for i in range(1, 11) :
    f.write(f'{i} 번째 줄입니다.\n')
f.close()

f = open('test.txt', 'w')
f.write('hello\n')
f.write('hi')
f.close

f = open('score.txt', 'w')
f.write('80 90 70 100 60')
f.close

f = open('numbers.txt', 'w')
for i in range(10, 21) :
    f.write(f'{i}\n')
f.close