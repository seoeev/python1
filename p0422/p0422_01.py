# 구구단 출력하기

# for y in range(2, 10):
#   for x in range(2, 10):
#     print("%d * %d = %d" %(y, x, (y*x)))   


# dan = int(input("단을 입력하세요. : "))

# for y in range(2, 10):
#   for x in range(2, dan+1):
#     print("%d * %d = %d" %(y, x, (y*x)), end=", ")   
#   print()

# ====================================================== #

for i in range (1, 11) :
  if(i % 2 == 0):
    print("%d%%2 = %d" %(i, (i%2)))
  else :
    print("%d%%2 = %d" %(i, (i%2)))

  