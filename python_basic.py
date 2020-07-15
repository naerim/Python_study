'''
# 출력 방식
print("number")
a,b,c=1,2,3
print(a,b,c)
print(a,b,c, sep='\n')
print(a, end=' ')
print(b, end=' ')
print(c)

# 키보드를 통해 변수 입력
a, b = input("숫자를 입력하세요 : ").split()
print(a+b)

# map 함수
c, d = map(int, input("숫자를 입력하세요 : ").split())
print(c + d)

# 몫 연산, 나머지 연산, 거듭 제곱
print(c//d)
print(c%d)
print(c**d)


# 조건문(분기, 중첩), 들여쓰기 중요함
x=7
if x>0 and x<10:
    print("10보다 작은 자연수")

x=7
if 0<x<10:
    print("10보다 작은 자연수")

x=-3
if x>0:
    print("양수")
else:
    print("음수")

x=93
if x>=90:
    print('A')
elif x>=80:
    print('B')
else:
    print('F')

# 반복문

for i in range(1,11):
    print(i)

for i in range(10,0, -2):
    print(i)

i=1
while i<=10:
    print(i)
    i=i+1

i=1
while True:
    print(i)
    if i==5:
        break
    i+=1

for i in range(1,11):
    if i%2==0:
        continue
    print(i)

for i in range(1,11):
    print(i)
    if i>15:
        break
else:
    print(11)

# 1부터 n까지 홀수출력
n = int(input("N : "))
for i in range(1,n+1):
    if i%2==1:
        print(i)

# 1부터 n까지의 합 구하기
n = int(input("n : "))
sum = 0
for i in range(1, n+1):
    sum += i
print(sum)

# n의 약수 출력하기
n = int(input("n : "))
for i in range(1, n+1):
    if n%i == 0:
        print(i, end=" ")

# 중첩 반복문(2중 for문)
for i in range(5):
    for j in range(5-i):
        print("*", end=' ')
    print()
'''
# 문자열과 내장 함수
msg = "It is Time"
print(msg.upper()) #대문자화
print(msg.lower()) #소문자화
tmp=msg.upper()
print(tmp)
print(tmp.find('T')) #인덱스를 반환(1이 출력됨)
print(tmp.count('T')) #2가 출력됨
print(msg[:2]) #슬라이스 기능, 제일처음부터 2번전까지 출력(0~1까지), It이 출력됨
print(msg[3:5]) #공백도 문자, is가 출력됨
print(len(msg)) #문자열의 길이, 10이 출력됨
for i in range(len(msg)):
    print(msg[i], end='')
print()

for x in msg: #문자열 하나하나를 접근
    print(x, end='')
print()

for x in msg:
    if x.isupper(): #x가 대문자이면 참
        print(x, end=' ')
    elif x.islower(): #x가 소문자이면 참
        print(x, end=' ')
print()

for x in msg:
    if x.isalpha(): #알파벳일때 참, 공백은 거짓
        print(x, end='')
print()

tmp='AZ'
for x in tmp:
    print(ord(x)) #아스키 코드(A=65, Z=90)
tmp='az'
for x in tmp:
    print(ord(x)) #아스키 코드(a=97, z=122)

tmp=65
print(chr(tmp)) #아스키 코드와 대응되는 문자를 출력해줌





















