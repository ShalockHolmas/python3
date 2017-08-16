# -*- coding: utf-8 -*-
import re
import keyword
import sys

# m = re.search('foo', 'foosea')
# if m is not None: print(m)

print("你好，世界\n\r")
print(keyword.kwlist)

# if True:
# print("this is true")
# print("this is after true")
# else:
#     print("this is false")
#     print("this is after false")
# print("this is end")
#
# print("this is \"\"")
# print('this is \'\'')
# print('''this
# is
# \'\'\'''')
#
# input("\n\n按下enter后退出")

print("下面是import教学：")
print("输出脚本参数:")
for i in sys.argv:
    print("参数:", i)
# print("\n python路径:", sys.path)

print()
print("下面是数据类型教学：")
a = b = c = 1
print(a)
print(a, b, c)
a, b, c = 1, 2, "asd"
print(a, b, c)
print('a is int? ', isinstance(a, int))
print('b is int? ', isinstance(b, int))
print('c is int? ', isinstance(c, int))
print('c is :', type(c))

print()
print("下面是instance和type的区别：")


class A:
    pass


class B(A):
    pass


print("instance A()=A? ", isinstance(A(), A))
print("type A()=A? ", type(A()) == A)

print("instance B()=A? ", isinstance(B(), A))
print("type B()=A? ", type(B()) == A)

print()
print("下面是bool类型加减和del：")
x = False
y = True
z = 1
print("false + 1 = ", x + z)
print("true + 1 = ", z + y)

print()
print("下面是计算：")
print("1 + 1 =", 1 + 1)
print("1 - 1 =", 1 - 1)
print("2 * 21 =", 2 * 21)
print("7 / 3 =", 7 / 3)
print("7 // 3 =", 7 // 3)
print("17 % 3 =", 17 % 3)
print("2 ** 10 =", 2 ** 10)

print()
print("下面是字符串：")
str = "123456789"
print(str)
print(str[0:-1])
print(str[0])
print(str[2:5])
print(str[2:])
print(str * 2)
print(str[0:1])


print()
print("下面是转义：")
print("aaa\nbbb")
print(r'aaa\nbbb')
print(R'aaa\nbbb')

print()
print("下面是list,tuple：")
list = [1, 2, 3, 4, 5, 6]
list2 = [7, 8, 9]

print(list)
print(list[1:2])
print(list[0])
# print(list[1, -1])
print(list[2:])
print(list * 2)
print(list + list2)

tup = (1, 2, 3, 4, 5)
print(tup)

print()
print("下面是set：")
sets = {'a', 'b', 'c', 'd'}
print('sets:', sets)
print('sets:', sets)
print('sets:', sets)

if 'a' in sets:
    print("a 在sets内")
else:
    print("a 不再set内")

sets2 = {'d', 'e'}
print('sets2：', b)

print("1 - 2 =", sets - sets2)
print("1 | 2 =", sets | sets2)
print("1 & 2 =", sets & sets2)
print("1 ^ 2 =", sets ^ sets2)


print()
print("下面是字典：")
dick = {'a':'1-first', 'b':'2-second'}
print(dick)
print(dick.keys())
print(dick.values())
print(dick['a'])

print("")
print("下面是函数：")


def example(aa, bb):
    return aa, bb
print("多返回值函数：", type(example(1, 2)))


def multreturn(*args):
    for i in args:
        print(i)
    return args
print(multreturn(1, 2, 3, 4))

xxx = 1
if xxx:
    print("1 is True")
else:
    print("1 not True")

yyy = 0
if yyy:
    print("0 not False")
else:
    print("0 is False")

aaa = 10
while aaa <= 10:
    if aaa == 6:
        break
    print(aaa)
    aaa -= 1
