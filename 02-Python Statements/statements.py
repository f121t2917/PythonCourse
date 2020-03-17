# -*- coding: utf-8 -*-
from random import shuffle
from random import randint

mylist = [(1, 2), (3, 4), (5, 6)]
print(len(mylist))

# for (a, b) in mylist:
for a, b in mylist:
    print(a)
    print(b)

d = {'k1': 1, 'k2': 2, 'k3': 3}
for item in d.items():
    print(type(item))

# tuple 可以使用以下方式
for key, value in d.items():
    print(value)

for value in d.values():
    print(value)

for _ in 'Hello World':
    print('Cool!')

for num in range(10):
    print(num)

print(list(range(0, 11, 2)))

word = 'abcde'
for item in enumerate(word): # 轉成 tuple
    print(type(item))
    print(item)

for index, letter in enumerate(word): # 轉成 tuple
    print(index)
    print(letter)

mylist1 = [1, 2, 3, 4, 5, 6]
mylist2 = ['a', 'b', 'c']
mylist3 = [100, 200, 300]
for item in zip(mylist1, mylist2, mylist3): # 組成 tuple，以最小長度為主
    print(item)

print(list(zip(mylist1, mylist2)))

print('x' in ['x', 'y', 'z'])
print('a' in 'a world ') # 可以是字串

print('mykey' in {'mykey': 345}) # 預設是判斷 key
d = {'mykey': 345}
print(345 in d.values())
print(345 in d.keys())

print(min(mylist1))
print(max(mylist1))

mylist = [1, 2, 3, 4, 5, 6, 7, 8, 9 ,10]
# 亂數排序 
shuffle(mylist)
random_list = shuffle(mylist)
type(random_list) # NoneType 直接改變 mylist
print(mylist)

# 亂數
print(randint(0, 100))

result = input('Enter a number here: ')
print(result)
print(type(result)) # 輸入的數值為字串

mystring = 'hello'
mylist = []
for letter in mystring:
    mylist.append(letter)

# 可改為以下
mylist = [letter for letter in mystring]
print(mylist)

mylist = [x for x in 'word']
print(mylist)


mylist = [num**2 for num in range(0, 11)]
print(mylist)

# 加入判斷
mylist = [x for x in range(0, 11) if x%2 == 0]
print(mylist)

mylist = [x if x%2 == 0 else 'ODD' for x in range(0, 11)]

celcius = [0, 10, 20, 34.5]
fahrenheit = [( (9/5) * temp + 32) for temp in celcius]
print(fahrenheit)
# 上面式子等於下面
fahrenheit = []
for temp in celcius:
    fahrenheit.append(( (9/5) * temp + 32))
print(fahrenheit)


for x in [2, 4, 6]:
    for y in [1, 100, 1000]:
        mylist.append(x * y)

mylist = [x*y for x in [2, 4, 6] for y in [1, 10, 1000]]
print(mylist)
