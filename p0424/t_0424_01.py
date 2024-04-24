a = {'홍콩', '한국'}
a.update(['한국', '미국'])

print(a)
b = [2,]    # 한개 일 때는 , 해주기

data = [1, 4, 2, 5]
data2 = []

data2 = [a for a in data]
print(data2)

print(dir(data))
print(type(data))

