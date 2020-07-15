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
'''


'''
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
'''


'''
# 리스트와 내장함수(1)
import random as r
b=list()
print(b)

a=[1,2,3,4,5]
b=list(range(1,11)) #1~10까지 초기화시킬 수 있음

c=a+b #리스트 합치기
print(c)

a.append(6) #추가
a.insert(3,7) #특정 인덱스에 추가함
a.pop() #맨 뒤의 자료를 제거함
a.pop(3) #특정 인덱스에 있는 값을 제거함
a.remove(4) #4라는 값을 가져와서 제거
a.index(5) #5라는 값의 인덱스를 알려줌

a=list(range(1,11))
print(a)
print(sum(a)) #a라는 리스트의 값을 모두 합해줌
print(max(a)) #a 리스트에서 가장 큰 값을 찾아줌
print(min(a)) #최솟값
print(min(7,5)) #인자값들 사이에서 최솟값을 찾아줌
r.shuffle(a) #셔플, 게임만들때 많이 사용함
print(a)

a.sort() #오름차순
a.sort(reverse=True) #내림차순
a.clear() #리스트가 비워짐
print(a)

# 리스트와 내장함수(2)
a=[23,12,36,53,19]
print(a[:3]) #0번부터 2번까지
print(a[1:4])
print(len(a)) #리스트의 길이

for i in range(len(a)):
    print(a[i], end=' ')
print()

for x in a:
    print(x, end=' ')
print()

for x in enumerate(a): #인덱스 번호, 값이 소괄호안에서 출력됨
    print(x)
    
#리스트값은 변경가능하지만 투플값은 변경불가하다.
b=(1,2,3,4,5) #b[0]=7은 에러가 발생한다.

for x in enumerate(a): #x[0]은 인덱스번호,  x[1]은 원소값
    print(x[0], x[1])
print()

for index, value in enumerate(a): #많이 사용하는 방법, 위와 똑같이 출력됨
    print(index, value)
print()

if all(50>x for x in a): #하나라도 거짓이면 거짓을 return, 모두가 참이여야 true
    print("YES")
else:
    print("NO")

if any(15>x for x in a): #한번이라도 참이면 true return, 모두 거짓이면 false
    print("YES")
else:
    print("NO")
'''


'''
# 2차원 리스트 생성과 접근
a=[0]*3 #0으로 초기회되고 0~2까지
print(a)

a=[[0]*3 for _ in range(3)] #_는 변수없이 반복문
print(a)
a[0][1]=1
print(a)

for x in a: #2차원 리스트를 표처럼 확인하는 것
    print(x)

for x in a: #2차원 리스트의 하나하나의 값을 출력
    for y in x:
        print(y, end=' ')
    print()
'''


'''
# 함수 만들기
def add(a, b):
    c = a+b
    print(c)

add(3,2)

def add(a,b):
    c=a+b
    return c

def add(a,b): #두개의 값을 반환할 수 있음, 튜플로 반환됨
    c=a+b
    d=a-b
    return c,d

def isPrime(x):
    for i in range(2, x):
        if x%i==0:
            return False
    return True

a=[12, 13, 7, 9, 19]
for y in a:
    if isPrime(y):
        print(y, end=' ')
'''


'''
# 람다 함수 = 익명의 함수
def plus_one(x):
    return x+1

print(plus_one(1))

plus_two = lambda x: x+2 #람다함수는 변수에 할당해줘야 한다.
print(plus_two(1))

a = [1, 2, 3]
print(list(map(plus_one, a))) #map은 인자 두개(함수명, 자료들)로 이루어져 있다. list(): 리스트로 반환됨

print(list(map(lambda x: x+1, a))) 
'''
