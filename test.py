#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os

L=[x for x in os.listdir('.') if os.path.isdir(x)]
print(L)

if os.fork()==0:
	print('child')
else:
	print('parent')

'''
L = ['adam', 'LISA', 'barT']

def normalize(name):
	return name.capitalize()

print(list(map(normalize, L)))
'''

'''
L1 = ['Hello', 'World', 18, 'Apple', None]
L2 = [ x.lower() for x in L1 if isinstance(x, str)]
print(L2)
'''

'''
d={'a':1,'b':2,'c':3}
for key, value in d.items():
    print(key)
    print(value)
'''

'''
L = ['Alen', 'Bob', 'Linken', 'Gelon', 'Mage','Mike']

print(L[1:4])
print('=')
print(L[-5:-1])
print('=')
print(L[1:6:3])
'''

'''
def mi(x, n):
	if n == 0:
		return 1
	return x * mi(x, n-1)

print(mi(2,5))
'''


'''

def move(n, a, b, c):
	if n == 0:
		return
	move(n-1, a, c, b)
	print(a, '-->', c)
	move(n-1, b, a, c)
	return

move(3, 'A', 'B', 'C')
'''
'''
import math

def quadratic(a, b, c):
    if not isinstance(a,(int,float)):
        raise TypeError('bad operand type')
    else:
        v =  b ** 2 - 4* a * c
        if v >= 0:
            x1 = (math.sqrt(v) / 2 * a - b ) / 2 * a
            x2 = (- math.sqrt(v) / 2 * a - b ) / 2 * a
            print('value:', x1, x2)
            return x1, x2
        elif v < 0:
            print('no root')
            return

quadratic(1,4,2)
'''

'''
s = (1, 2, 3)
d = {s}
print(d)
s = (1, [2 , 3])
d = {s}
print(d)
'''


'''
L = ['Bart', 'Lisa', 'Adam']

for x in L:
	print('hello, %s !' % x)

n = len(L)
m = 0
while m < n:
	print('hello, %s !' % L[m])
	m = m + 1
'''


'''
import urllib.request

request = urllib.request.Request("http://www.baidu.com")

response = urllib.request.urlopen(request)

print(response.read())

n = 123
f = 456.789
s1 = 'Hello, world'
s2 = 'Hello, \'Adam\''
s3 = r'Hello, "Bart"'

print(n)
print(f)
print(s1)
print(s2)
print(s3)

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

p1 = 72
p2 = 85

r = (p2 - p1)  / p1 * 100
print('grow rate : %.1f %%' % r)

''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

L = [
        ['Apple', 'Google', 'Microsoft'],
        ['Java', 'Python', 'Ruby', 'PHP'],
	['Adam', 'Bart', 'Lisa']
    ]

print(L[0][0])
print(L[1][1])
print(L[-1][-1])
'''

''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
'''
heightStr = input('your heighti(m):')
weightStr = input('your weight(kg):')

heightInt = float(heightStr)
weightInt = float(weightStr)

bmi = weightInt / (heightInt ** 2)

if bmi < 18.5:
	print('太轻了')
elif 18.5 <= bmi <=25:
	print('正常')
elif 25 < bmi < 28:
	print('太重了')
elif 28 <= bmi <= 32:
	print('肥胖')
else:
	print('严重肥胖')
'''
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
