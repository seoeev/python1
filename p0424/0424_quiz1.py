# 퀴즈 리스트를 아래와 같이 dict_bleed{}로 변환하는 코드 작성
blist = ['A', 'O','B','AB','B','A','AB','AB','A','A' ]

dict_bleed = {}
for x in blist:
    dict_bleed[x] = blist.count(x)
print(dict_bleed)

# {'A':4, 'B':2, 'AB':3, 'O':1}
