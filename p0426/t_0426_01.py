import os

# 폴더 생성, 삭제, 이름 변경

print(os.getcwd())
print("디렉토리 존재" if os.path.exists('test') else '디렉토리 미존재')
res = 'ok' if True else 'not ok'
print(res)
# 특정 절대경로로 디렉토리 생성
#os.mkdir('c:\\temp\\myfolder')
# os.makedirs('c:\\temp\\aa\\bb')

# isdir() == exists()
if not os.path.isdir('aa'): os.mkdir('aa')

mypath = r'c:\temp\hello.py'
print(os.path.dirname(mypath))  # 전체 경로에서 디렉토리만 출력
print(os.path.basename(mypath)) # 전체 경로 파일명만 출력


filename = 'python-3.9.7-amd64.exe'
file1 = filename.split('.')
print(file1, file1[:-1], file1[-1])
print(''.join(file1[:-1]))