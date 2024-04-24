# Quiz4. 윤년이면 1 아니면 0을 출력
print("윤년이면 1 아니면 0을 출력합니다.")
year = int(input("년도를 입력해주십시오 : "))
if((year % 4 == 0 and year % 100 != 0) or year % 400 == 0):
    print(year, 1)
else :
    print(year, 0)

# Quiz5. 나이를 입력 해서 17,18,19세이면 "출입 허용",그렇지 않은 경우 "출입 금지"를 출력 하는 프로그램
print("출입가능 나이를 판단합니다.")
age = int(input("나이를 입력해 주십시오. : "))
if(17 >= age <= 19) :
    print("출입 가능")
else:
    print("출입 금지")

# Quiz6.평면상의 좌표를 입력 해서 어느 사분면에 속하는지 출력하는 프로그램을작성하시오.
# 단,x와 y는 0이 아닌 정수임.
print("평면상의 좌표를 입력해 주십시오.")
x, y = map(int, input("띄어쓰기 단위로 좌표를 입력(x y) : ").split())

if x > 0 and y > 0:
    print(x, y, "제 1사 분면")
elif x < 0 and y > 0:
    print(x, y, "제 2사 분면")
elif x < 0 and y < 0:
    print(x, y, "제 3사 분면")
elif x > 0 and y < 0:
    print(x, y, "제 4사 분면")

# Quiz7.삼각형 세변의 길이를 입력하여 직각삼각형이면 1,아니면 0을 출력하는 프로그램을.
# 단,세변의 길이는 변의 길이에 상관없이 입력한다.
# a^2 + b^2 = c^2
print("직사각형이면 1, 아니면 0을 출력합니다.")
a, b, c = map(int, input("삼격형 세변의 길이를 띄어쓰기 단위로 입력 : ").split())

if a**2 + b**2 == c**2:
    print("1")
else:
    print("0")
