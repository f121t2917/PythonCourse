# -*- coding: utf-8 -*-

# 點精度和計算機表示內存中數字的能力有關
# https://docs.python.org/2/tutorial/floatingpoint.html
print(0.1 + 0.2 - 0.3)

mystring = '1234567890'
# index 從 0 開始 step 為 2
print(mystring[::2])

# 反過來
print(mystring[::-1])

name = "Sam"
# 字符串不可變！不能使用索引來更改字符串的單個元素
# name[0] = 'P' 無法使用這方法修改第一個字元 

print('P' + name[1:])

letter = 'z'
print(letter * 10)

x = "hello world"
print(x.split()) # 預設用空白分割
print(x.split('l'))

# string format
print('This is a string {}'.format('INSERTED'))
print('The {0} {0} {0}'.format('fox', 'brown', 'quick'))
print('The {q} {b} {f}'.format(f='fox', b='brown', q='quick'))

result = 100 / 777.
print(result)
print("The result was {}".format(result))
print("The result was {r}".format(r=result))

# 格式 {value:width.precision f}
print("The result was {r:10.3f}".format(r=result))

name = "Jose"
age = 3
print('Hello, his name is {}'.format(name))
# python 3.6 以上版本 可改成以下
print(f'Hello, his name is {name}')
print(f'{name} is {age} years old.')

print('=== List ===')
my_list = ['STRING', 100, 23.2]
print(len(my_list))
print(my_list[0])
print(my_list[1:])

# List 相加
another_list = ['four', 'five']
new_list = my_list + another_list
print(new_list)

# 新增元素
new_list.append('seven')
print(new_list)

popped_item = new_list.pop()
print(popped_item)
print(new_list)

# pop 第一個元素
print(new_list.pop(0))
print(new_list)

new_list = ['a', 'e', 'x', 'c', 'b']
my_sorted_list = new_list.sort() # sort 返回 NoneType，sort 直接改 list 
print(type(my_sorted_list))
print(new_list)

new_list.reverse()
print(new_list)

print('=== Dict ===')
my_dict = {'key1': 'value1', 'key2': 'value2'}
print(my_dict['key1'])

d = {'k1': 123, 'k2': [0, 1, 2], 'k3': {'insideKey': 100}}
print(d['k2'])
print(d['k3']['insideKey'])

d['k1'] = 'NEW VALUE'
print(d)

# dict keys
print(d.keys())
# dict values
print(d.values())

print('=== tuple ===')
t = (1, 2, 3)
print(type(t), len(t), t[0], t[-1])

t = ('a', 'a', 'b')
print(t.count('a'))
print(t.index('a'), t.index('b'))
# t[0] = 'NEW' tuple 無法修改，具不變性

# 值是唯一
print('=== Set ===')
myset = set()
myset.add(1)
myset.add(2)
myset.add(2)
print(myset)
mylist = [1, 1, 1, 2, 2, 2, 3, 3, 3,3]
print(set(mylist))

print('=== Boolean ===')
print(type(False))


print('=== Files I/O ===')
# %%writefile myfile.txt
# Hello this is a text file
# this is the second line
# this is the third line
myfile = open('test.txt')
print(myfile.read())
print(myfile.read()) # 第二次再讀就需要重設 seek
myfile.seek(0)
print(myfile.read())

# readlines
myfile.seek(0)
print(myfile.readlines())

# Windows
# open("C:\\Users\\UserName\\Folder\\test.txt")
# Linux
# open("/Users/UserName/Folder/myfile.txt")
myfile.close()

with open('test.txt') as my_new_file:
    contents = my_new_file.read()
print(contents)

with open('test.txt', mode='r') as myfile:
    contents = myfile.read()
print(contents)

# write mode 無法 read
# with open('test.txt', mode='w') as myfile:
    # contents = myfile.read()

# with open('test.txt', mode='a') as f:
#     f.write('\nFOUR ON FOURTH')

# with open('test.txt', mode='r') as myfile:
#     print(myfile.read())


