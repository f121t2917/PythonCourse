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