# 효율적인 루핑을 위한 이터레이터
import itertools
import threading

print(list(itertools.permutations(['1', '2', '3'], 2)))

# it = itertools.combinations(range(1, 46), 6)
# for num in it:
#     print(num)


def positive(l):
    result = [1, -3, 2, 0, -5, 6]
    for i in l:
        if i > 0:
            result.append(i)
        return result

print(positive([1, -3, 2, 0, -5, 6]))

def positive2(x):
    return x>0

print(list(filter(positive2, [1, -3, 2, 0, -5, 6])))

def two_times(list):
    result = [num*2 for num in list]
    return [num*2 for num in list]

result = two_times([1,2,3,4])
print(result)

def two_times2(x): return x*2
# 함수 이름만 참조
print(list(map(two_times2, [1,2,3,4])))
print(list(map(lambda x:x*2, [1,2,3,4])))


# itertools.zip_longest
# zip()
students = ['a', 'b', 'c', 'd', 'e']
snacks = ['새우깡', '젤리', '초코']
print(list(zip(students, snacks)))
print(list(itertools.zip_longest(students, snacks, fillvalue='새우깡')))

def add(data):
    result = 0
    for i in data:
        result += i
    return result

data = [1,2,3,4,5]
print(add(data))

import functools
# 왼쪽에서 오른쪽으로 하나씩 요소를 가져와서 연산하는 함수
print(functools.reduce(lambda x,y:x+y, data))

from operator import itemgetter

# print(sorted(students, key=itemgetter(2)))


students = [
    {'name': 'java', "age": 22, "grade": "A"},
    {'name': 'dave', "age": 32, "grade": "B"},
    {'name': 'sally', "age": 17, "grade": "B"},
]


students2 = [
    {'name': 'java', "age": 2+2, "grade": "A"},
    {'name': 'dave', "age": 3+2, "grade": "B"},
    {'name': 'sally', "age": 1+7, "grade": "B"},
]


print(sorted(students, key=itemgetter('age')))
print(sorted(students2, key=itemgetter('age')))

import glob
print(glob.glob("c:/temp/a*"))

# 환경변수 확인
import os
print(os.environ)

# 파일 실행, os.popen(명령)
f = os.popen('dir')
print(f.read())

# import zipfile
#
# with zipfile.ZipFile('C:\\Temp\\', 'w') as myzip:
#     myzip.write('a.txt')
#     myzip.write('b.txt')
#     myzip.write('c.txt')
#
# with zipfile.ZipFile('C:\\Temp\\mytext.zip') as myzip:
#     myzip.extractall()
#

import  time
def long_task():
    for i in range(5):
        time.sleep(1)
        print("w%s\n" %i)

print('Start')

threads = []
for i in range(5):
    t = threading.Thread(target=long_task())
    threads.append(t)

for t in threads:
    t.start()

for t in threads:
    t.join() # thread 종료시까지 기다림


print("End")


