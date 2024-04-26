# items() 정렬

data = {"d":8, "c":5, "a":9, "b":2}

# 키 기준
data1 = sorted(data.items(), reverse=False)
print(data1)

data2 = sorted(data.items(), key=lambda x: x[0])
data3 = sorted(data.items(), key=lambda x: x[0], reverse=True)
print(data2)
print(data3)

# 값 기준
data2 = sorted(data.items(), key=lambda x: x[1])
data3 = sorted(data.items(), key=lambda x: x[1], reverse=True)
print(data2)
print(data3)

# lambda 예약어
# 함수_이름 = lambda 매개변수, 매개변수2, ... : 표현식 부분
# def 함수_이름(매개변수1, 매개변수2, ...):
#   return 값

def add(a, b):
    return a+b

result = add(3, 4)
print(result)

add = lambda a, b: a+b
result = add(3, 4)
print(result)


# JOIN #
str = "abc123가나다"
strlist = ['abc', '123', '가나다']

print("-".join(str))
print(", ".join(strlist))

# 리스트를 문자열 형태로 합칠때는 join()
# 문자열을 리스트로 쪼갤때는 split()

# 공백 제거
t = "  re er "
print(t)
print(t.lstrip())
print(t.rstrip())
print(t.strip())

# ** 딕셔너리,  * 매개변수 여러개 받게(튜플)
def print_kwargs(**kwargs):
    print(kwargs)

print_kwargs(a=1)   # {'a': 1}

def say_nick(nick):
    if nick=='바보':
        return
    print("나의 별명은 %s 입니다" %nick)

say_nick('아이들')
say_nick('바보')



# 파일 읽기 open()

f = open('c:\\Temp\\test.txt', 'w')
f.write('python\n')
f.write('java\n')
f.close()
print("저장완료")



# 파이썬 자바 스프링 html Django를 한줄씩 파일에 저장 후 내용을 읽어 한줄씩 출력


with open('c:\\Temp\\test4.txt', 'w') as f:
    str = ['자바', '스프링', 'html', 'Django']
    str = '\n'.join(str)
    f.write(str)
    print('저장완료')


# 표준 출력
with open('c:\\Temp\\test4.txt', 'r') as f:
    content = f.read()
    print(content)


import pickle
f = open('c:\\Temp\\test.txt', 'wb')
data = {1: 'python', 2:'you need'}
pickle.dump(data, f)
f.close()
print("완")

f = open('c:\\Temp\\test.txt', 'rb')
data=pickle.load(f)
print(data)



# 퀴즈
blist = ['A', 'B', 'AB', 'O', 'AB', 'O', 'B', 'AB']
dict_blood = {}
for x in blist:
    dict_blood[x] = blist.count(x)
print(dict_blood)

f = open('c:\\Temp\\blood.txt', 'wb')
pickle.dump(dict_blood, f)
f.close()
print("저장완완")

f = open('c:\\Temp\\blood.txt', 'rb')
data=pickle.load(f)
print(data)


import os
# 디렉토리 검색
# listdir
f1 = os.listdir()
# f2 = os.listdir('test')
f3 = os.listdir(r'C:\Temp')
print(f1, f3, sep = '\n')
print(os.getcwd())

file_list = os.scandir()
print(file_list)

for filename in file_list:
    print(filename, filename.name)


# iterator
a = [1,2,3]
ia = iter(a) # 이터레이터 생성
# next(ia)

for i in ia:
    print(i)

# generator
