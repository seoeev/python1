print("a", "2")
name = "홍길동"
age = 18
score = 93.642
print("[{:<10}]".format(format(name)))
print("[{:>10}]".format(format(name)))
print("[{:^10}]".format(format(name)))
print("[{:.5f}]".format(score))
print("[{:8.3f}]".format(score))
print("[{:<8.3f}]".format(score))
print("[{:>8.3f}]".format(score))


# > 기호 앞에 문자열을 쓰며 공백을 해당 문자열로 채워 줌
print("[{:*>10}]".format(name))
print("[{:#<10}]".format(name))
print("[{:?^10}]".format(name))


# 분리 후 사용
temp = "이름:{}, 나이:{}, 점수:{}"
temp = temp.format(name, age, score)
print("분리 : ", temp)

print(f"에프 : 이름:{name}, 나이:{age}, 점수:{score}")
print(f"[{name:>10}], [{age:>10}]")
print(f"[{name:<10}], [{age:<10}]")
print(f"[{name:^10}], [{age:^10}]")


# 포맷팅을 url 작성하기
site = "https://api.thingspeak.com/update?api_key="
apikey = "YTRUYF6Y045MOB37"
v1 = 5
v2 = 10
url = f"{site}-{apikey}&field={v1}&filed2={v2}"
print(url)
