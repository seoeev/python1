# json 파일
import json

with open('myinfo.json', encoding='utf8') as f:
    data = json.load(f)

print(type(data), data)


# 만들기

d = {'name':'김길동', 'birth':'0325', 'age':18}
json_data = json.dumps(d)
print(json_data)

json_data2 = json.dumps(d, ensure_ascii=False) #unicode 변환 방지
print(json_data2)

# 들여쓰기
json_data3 = json.dumps(d, indent=2, ensure_ascii=False) #unicode 변환 방지
print(json_data3)

import urllib.request

# SSL 인증서 검증 비활성화 처리
import ssl
context = ssl._create_unverified_context()

def get_wikidocs(page):
    resource = 'https//wikidocs.net/{}'.format(page)
    with urllib.request.urlopen(resource, context=context) as s:
        with open('wikidocs_%s.html'%page, 'wb') as f:
            f.write(s.read())

get_wikidocs(12)


import webbrowser
webbrowser.open_new('http://python.org')


