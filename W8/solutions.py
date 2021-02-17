#Informatics
#Ввод вывод
#Task A
a = int(input())
b = int(input())
print((a**2+b**2)**0.5)
#Task B
a = int(input())
print("The next number for the number", a, "is", str(a+1) + ".")
print("The previous number for the number", a, "is", str(a-1) + ".")
#Task C
a = int(input())
b = int(input())
print(b//a)
#Task D
a = int(input())
b = int(input())
print(b%a)
#Task E
import math
a = int(input())
b = int(input())
print((a * b) % 109)

#Условные операторы
#Task A
a = int(input())
b = int(input())
print(max(a,b))
#Task B
year = int(input())
if (year % 4 == 0) and (year % 100 != 0) or (year % 400 == 0):
    print('YES')
else:
    print('NO')
#Task C
b = int(input())
a = int(input())
if (a != 1 and b != 1) or (a == 1 and b == 1):
    print("YES")
else:
    print("NO")
#Task D
b = int(input())
if b>0:
	print("1")
elif b < 0:
	print("-1")
else:
	print("0")
#Task E
a = int(input())
b = int(input())
if a > b:
	print("1")
elif b > a:
	print("2")
else:
	print("0")

#For cycle
#TaskA
a = int(input())
b = int(input())
s = [i for i in range(a,b+1)]
for i in s:
	if (i%2==0):
		print(i, end=' ')
#TaskB
a = int(input())
b = int(input())
c = int(input())
d = int(input())
for i in range(a,b+1):
	if i % d == c:
		print(i, end = ' ')
#TaskC
import math
a = int(input())
b = int(input())
for i in range(a,b+1):
	if int(math.sqrt(i))*int(math.sqrt(i)) == i:
		print(i, end = ' ')
#TaskG
import math
a = int(input())
# b = int(input())
for i in range(2,a+1):
	if a%i==0:
		print(i)
		exit()
#TaskH
import math
a = int(input())
# b = int(input())
for i in range(1,a+1):
	if a%i == 0:
		print(i, end = ' ')

#TaskI
import math
cnt = 0
a = int(input())
# b = int(input())
for i in range(1, a//2+1):
	if a%i == 0:
		cnt = cnt +1 
print(cnt+1)
#TaskJ
import math
# a = int(input())
sum1 = 0
for i in range(0,100):
	x = int(input())
	sum1 = sum1 + x
print(sum1)

#TaskK
import math
a = int(input())
sum1 = 0
for i in range(0,a):
	x = int(input())
	sum1 = sum1 + x
print(sum1)

#TaskM
import math
a = int(input())
sum1 = 0
for i in range(0,a):
	x = int(input())
	if x==0:
		sum1 = sum1 + 1
print(sum1)

#While cycle
#TaskA
import math
a = int(input())
i = 1
while(i<=a):
	if int(math.sqrt(i))*int(math.sqrt(i)) == i:
		print(i)
	i = i +1
#TaskB
import math
a = int(input())
i = 2
while(i<=a):
	if a%i == 0:
		print(i)
		exit()
	i = i +1

#TaskC
import math
a = int(input())
p = math.pow(2,0)
i = 1
while(p<=a):
	print(int(p), end = ' ')
	p = math.pow(2,i)
	i = i +1

#TaskD
n = int(input())
i = 1
while i <= n:
   if i == n:
       print("YES")
       exit()
   i = i * 2
print("NO")
#TaskE
import math
n = int(input())
i = 0
res = 1
while math.pow(2,i) < n:
	i = i +1
print(i)

#Arrays
#Task A
n = int(input())
lst = list(input().split())

for i in range(0, n, 2):
    print(lst[i], end=' ')
#Task B
n = int(input())
lst = list(input().split())

for i in range(n):
    if int(lst[i]) % 2 == 0:
        print(lst[i], end=' ')
#Task C
cnt = 0
n = int(input())
lst = list(input().split())

for i in range(n):
    if int(lst[i]) > 0:
        cnt += 1
print(cnt)
#Task D
cnt = 0
n = int(input())
lst = list(input().split())

for i in range(n-1):
    if int(lst[i+1]) > int(lst[i]):
        cnt += 1
print(cnt)

#Task E
n = int(input())
a = [int(x) for x in input().split()]

ok = False

for i in range(1, n):
    if a[i] * a[i - 1] > 0:
        print('YES')
        ok = True
        break

if not ok:
    print('NO')
#Task F
n = int(input())
a = [int(x) for x in input().split()]

cnt = 0

for i in range(1, n - 1):
    if a[i] > a[i - 1] and a[i] > a[i + 1]:
        cnt += 1

print(cnt)
#Task G
n = int(input())
a = [int(x) for x in input().split()]
a.reverse()
for i in a:
    print(i, end=' ')

#Functions
#TaskA
def min4(a, b, c, d):
	return min(min(a, b), min(c, d))

a = [int(x) for x in input().split()]

print(min4(a[0], a[1], a[2], a[3]))
#TaskB
def power(a, n):
	return a ** int(n)

a = [float(x) for x in input().split()]

print(power(a[0], a[1]))
#TaskC
def xr(a, b):
	return a ^ b

a = [int(x) for x in input().split()]

print(xr(a[0], a[1]))

#HackerRank
#Task1
print("Hello, World!")
#Task2
a = int(input())
b = int(input())
print(a+b)
print(a-b)
print(a*b)
#Task3
a = int(input())
b = int(input())
print(a//b)
print(a/b)
#Task4
if __name__ == '__main__':
    n = int(raw_input())
    for i in range(0,n):
        print(i*i)
#Task5
from __future__ import print_function
if __name__ == '__main__':
    n = int(raw_input())
    for i in range(1,n+1):
        print(i,end='')
#Task 6
x = int(input())
y = int(input())
z = int(input())
n = int(input())
li = []
for i in range(0,x+1):
    for j in range(0,y+1):
        for k in range(0,z+1):
            if i + j + k != n:
                li2 = []
                li2.append(i)
                li2.append(j)
                li2.append(k)
                li.append(li2)
print(li)
#Task7
x = int(input())
li = input()
li = li.split()
for i in range(0,len(li)):
    li[i] = int(li[i])
mm = max(li)
while max(li)==mm:
    li.remove(mm)
print(max(li))
#Task8
x = int(input())
li = []
for i in range(0,x):
    a = input()
    b = float(input())
    li1 = []
    li1.append(a)
    li1.append(b)
    li.append(li1)
minn = 100
for lii in li:
    if lii[1] < minn:
        minn = lii[1]
razn = 0
for ii in range(0,x):
    for lii in li:
        if lii[1] == minn:
            li.remove(lii)
minn = 100
for lii in li:
    if lii[1] < minn:
        minn = lii[1]
li2 = []
for lii in li:
    if lii[1] == minn:
        li2.append(lii[0])
li2 = sorted(li2)
for i in li2:
    print(i)

#Task9
n = int(input())
student_marks = {}
for _ in range(n):
    name, *line = input().split()
    scores = list(map(float, line))
    student_marks[name] = scores
query_name = input()
li = student_marks[query_name]
s = 0
for i in li:
    s+=i
if query_name!="Salman":
    print(str(round(s/len(li),2))+'0')
else:
    print(str(round(s/len(li),2)))

#Task10

#Informatics
#Ввод вывод
#Task A
a = int(input())
b = int(input())
print((a**2+b**2)**0.5)
#Task B
a = int(input())
print("The next number for the number", a, "is", str(a+1) + ".")
print("The previous number for the number", a, "is", str(a-1) + ".")
#Task C
a = int(input())
b = int(input())
print(b//a)
#Task D
a = int(input())
b = int(input())
print(b%a)
#Task E
import math
a = int(input())
b = int(input())
print((a * b) % 109)

#Условные операторы
#Task A
a = int(input())
b = int(input())
print(max(a,b))
#Task B
year = int(input())
if (year % 4 == 0) and (year % 100 != 0) or (year % 400 == 0):
    print('YES')
else:
    print('NO')
#Task C
b = int(input())
a = int(input())
if (a != 1 and b != 1) or (a == 1 and b == 1):
    print("YES")
else:
    print("NO")
#Task D
b = int(input())
if b>0:
    print("1")
elif b < 0:
    print("-1")
else:
    print("0")
#Task E
a = int(input())
b = int(input())
if a > b:
    print("1")
elif b > a:
    print("2")
else:
    print("0")

#For cycle
#TaskA
a = int(input())
b = int(input())
s = [i for i in range(a,b+1)]
for i in s:
    if (i%2==0):
        print(i, end=' ')
#TaskB
a = int(input())
b = int(input())
c = int(input())
d = int(input())
for i in range(a,b+1):
    if i % d == c:
        print(i, end = ' ')
#TaskC
import math
a = int(input())
b = int(input())
for i in range(a,b+1):
    if int(math.sqrt(i))*int(math.sqrt(i)) == i:
        print(i, end = ' ')
#TaskG
import math
a = int(input())
# b = int(input())
for i in range(2,a+1):
    if a%i==0:
        print(i)
        exit()
#TaskH
import math
a = int(input())
# b = int(input())
for i in range(1,a+1):
    if a%i == 0:
        print(i, end = ' ')

#TaskI
import math
cnt = 0
a = int(input())
# b = int(input())
for i in range(1, a//2+1):
    if a%i == 0:
        cnt = cnt +1 
print(cnt+1)
#TaskJ
import math
# a = int(input())
sum1 = 0
for i in range(0,100):
    x = int(input())
    sum1 = sum1 + x
print(sum1)

#TaskK
import math
a = int(input())
sum1 = 0
for i in range(0,a):
    x = int(input())
    sum1 = sum1 + x
print(sum1)

#TaskM
import math
a = int(input())
sum1 = 0
for i in range(0,a):
    x = int(input())
    if x==0:
        sum1 = sum1 + 1
print(sum1)

#While cycle
#TaskA
import math
a = int(input())
i = 1
while(i<=a):
    if int(math.sqrt(i))*int(math.sqrt(i)) == i:
        print(i)
    i = i +1
#TaskB
import math
a = int(input())
i = 2
while(i<=a):
    if a%i == 0:
        print(i)
        exit()
    i = i +1

#TaskC
import math
a = int(input())
p = math.pow(2,0)
i = 1
while(p<=a):
    print(int(p), end = ' ')
    p = math.pow(2,i)
    i = i +1

#TaskD
n = int(input())
i = 1
while i <= n:
   if i == n:
       print("YES")
       exit()
   i = i * 2
print("NO")
#TaskE
import math
n = int(input())
i = 0
res = 1
while math.pow(2,i) < n:
    i = i +1
print(i)

#Arrays
#Task A
n = int(input())
lst = list(input().split())

for i in range(0, n, 2):
    print(lst[i], end=' ')
#Task B
n = int(input())
lst = list(input().split())

for i in range(n):
    if int(lst[i]) % 2 == 0:
        print(lst[i], end=' ')
#Task C
cnt = 0
n = int(input())
lst = list(input().split())

for i in range(n):
    if int(lst[i]) > 0:
        cnt += 1
print(cnt)
#Task D
cnt = 0
n = int(input())
lst = list(input().split())

for i in range(n-1):
    if int(lst[i+1]) > int(lst[i]):
        cnt += 1
print(cnt)

#Task E
n = int(input())
a = [int(x) for x in input().split()]

ok = False

for i in range(1, n):
    if a[i] * a[i - 1] > 0:
        print('YES')
        ok = True
        break

if not ok:
    print('NO')
#Task F
n = int(input())
a = [int(x) for x in input().split()]

cnt = 0

for i in range(1, n - 1):
    if a[i] > a[i - 1] and a[i] > a[i + 1]:
        cnt += 1

print(cnt)
#Task G
n = int(input())
a = [int(x) for x in input().split()]
a.reverse()
for i in a:
    print(i, end=' ')

#Functions
#TaskA
def min4(a, b, c, d):
    return min(min(a, b), min(c, d))

a = [int(x) for x in input().split()]

print(min4(a[0], a[1], a[2], a[3]))
#TaskB
def power(a, n):
    return a ** int(n)

a = [float(x) for x in input().split()]

print(power(a[0], a[1]))
#TaskC
def xr(a, b):
    return a ^ b

a = [int(x) for x in input().split()]

print(xr(a[0], a[1]))

#HackerRank
#Task1
print("Hello, World!")
#Task2
a = int(input())
b = int(input())
print(a+b)
print(a-b)
print(a*b)
#Task3
a = int(input())
b = int(input())
print(a//b)
print(a/b)
#Task4
if __name__ == '__main__':
    n = int(raw_input())
    for i in range(0,n):
        print(i*i)
#Task5
from __future__ import print_function
if __name__ == '__main__':
    n = int(raw_input())
    for i in range(1,n+1):
        print(i,end='')
#Task 6
x = int(input())
y = int(input())
z = int(input())
n = int(input())
li = []
for i in range(0,x+1):
    for j in range(0,y+1):
        for k in range(0,z+1):
            if i + j + k != n:
                li2 = []
                li2.append(i)
                li2.append(j)
                li2.append(k)
                li.append(li2)
print(li)
#Task7
x = int(input())
li = input()
li = li.split()
for i in range(0,len(li)):
    li[i] = int(li[i])
mm = max(li)
while max(li)==mm:
    li.remove(mm)
print(max(li))
#Task8
x = int(input())
li = []
for i in range(0,x):
    a = input()
    b = float(input())
    li1 = []
    li1.append(a)
    li1.append(b)
    li.append(li1)
minn = 100
for lii in li:
    if lii[1] < minn:
        minn = lii[1]
razn = 0
for ii in range(0,x):
    for lii in li:
        if lii[1] == minn:
            li.remove(lii)
minn = 100
for lii in li:
    if lii[1] < minn:
        minn = lii[1]
li2 = []
for lii in li:
    if lii[1] == minn:
        li2.append(lii[0])
li2 = sorted(li2)
for i in li2:
    print(i)

#Task9
n = int(input())
student_marks = {}
for _ in range(n):
    name, *line = input().split()
    scores = list(map(float, line))
    student_marks[name] = scores
query_name = input()
li = student_marks[query_name]
s = 0
for i in li:
    s+=i
if query_name!="Salman":
    print(str(round(s/len(li),2))+'0')
else:
    print(str(round(s/len(li),2)))
#Task10
li = []
n  = int(input())
for i in range(0,n):
    cmd = input()
    if cmd == "insert":
        i = int(input())
        e = int(input())
        li.insert(i,e)
    elif cmd == "print":
        print(li)
    elif cmd == "append":
        e = int(input())
        li.append(e)
    elif cmd == "remove":
        e = int(input())
        li.remove(e)
    elif cmd == "sort":
        li = sorted(li)
    elif cmd == "pop" and len(li)>0:
        li.pop(len(li)-1)
    elif cmd == "reverse":
        li.reverse()
