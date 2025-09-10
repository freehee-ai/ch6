# 파일을 쓰기 모드로 열기
# f = open('new.txt', 'w')
# f.write('hello world')
# f.close()

# 간단하게 쓰기
with open('new.txt', 'w') as f :
    f.write('hello world')
    # close 생략