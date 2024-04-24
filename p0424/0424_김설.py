import datetime as dt

# 수업 퀴즈. 리스트를 아래와 같이 dict_bleed{}로 변환하는 코드 작성
blist = ['A', 'O','B','AB','B','A','AB','AB','A','A' ]
# >> {'A':4, 'B':2, 'AB':3, 'O':1}
dict_bleed = {}
for x in blist:
    dict_bleed[x] = blist.count(x)
print(dict_bleed)



# == Quiz 2. 입력한 시간의 형식을 변경하시오. == #
while True:
    h,m,s = map(int, input("시간을 입력(시:분:초) : ").split(":"))

    if (0 <= int(h) < 24) and (0 <= int(m) < 60) and 0 <= int(s) < 60:
        ampm_dict = {
            'AM': '오전',
            'PM': '오후'
        }
        t = dt.time(h, m, s)
        formatted_time = ampm_dict[t.strftime("%p")] + ' ' + t.strftime('%I시 %M분 %S초')
        print(formatted_time)
        break
    else:
        print("올바른 시간대가 아닙니다.")
        continue


# == Quiz 4. N명의 심사위원의 점수의 합계를 출력하시오.
# 단 가장 높은 점수와 낮은 점수를 제외한 점수를 제외함.
# 높은 점수가 중복일 경우 하나만 삭제

print("심사위원의 점수의 합계를 구합니다.")
score = list(map(int, input("띄어쓰기 단위로 점수 입력 : ").split()))

# 정렬 및 삭제
score.sort()
del score[0]
score.pop()

# 점수 계산
total = 0
for i in score:
    total += i

print(total)


# ============= #

# Quiz 5. 연속 정답 배점 달라지는 시험
result = input("답 입력(OXOX): ")

score = 0
bonus = 1
for i in result:
    if(i == 'O'):
        score += bonus
        bonus += 1
    else:
        bonus = 1

print(f"{score}점")


# Quiz 6. 입력한 문장에서 사용하지 않은 알파벳 글자를 출력.
print("입력한 문장에서 사용하지 않은 알파벳 글자를 출력 합니다.")
alphabet = "abcdefghijklmnopqrstuvwxyz"
str = input("영소문자 문장 입력 : ")
for i in str:
    alphabet = alphabet.replace(i, "")

print(alphabet)


# Quiz 7. 정수를 입력하면 각 자릿수의 숫자의 합을 출력
str = input("정수를 입력 : ")
result = 0
for i in str:
    result += int(i)
print(result)


# Quiz 8. 입력한 n개의 단어를 출현 빈도수가 높은 단어 3개 출력
# 입 : 단어를 한 칸 단위로 n개 입력
# 출 : 가장 많이 등장한 단어부터 단어와 출현 빈도수를 3개 출력
wordlist = list(input("단어를 띄어쓰기 단위로 입력 : ").split())
w_dict = {}
for x in wordlist:
    w_dict[x] = wordlist.count(x)

w_dict = sorted(w_dict.items(), key = lambda item: item[1], reverse = True)
w_dict = dict(w_dict)

index = 0
for key, value in w_dict.items():
    print(f"{key}: {value}")
    index += 1
    if index == 3:
        break