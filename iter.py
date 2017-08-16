# import demo

list = [1, 2, 3, 4]
it = iter(list)
print(next(it))
print(next(it))
print(next(it))
print(next(it))

tupl = (1, 2, 4, 6)
it = iter(tupl)
print(next(it))
print(next(it))
print(next(it))
print(next(it))

sum = lambda a, b: a + b;
print(sum(1, 72))


# print()

# print(__name__)
# print("----")

whoisi = lambda: __name__;

# def whoisi():
#     return __name__
