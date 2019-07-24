import time


# d1 = {'aa': 10, 'bb': 20, 'cc': 30}
# d2 = {key: value*value for key, value in d1.items()}
# print(d2)
#
#
# def sum_1 (*args):
#     def _sum():
#         res = 0
#         for x in args:
#             res += x
#         return res
#     return _sum
#
# f = sum_1(1,2,3,4,5)
# print(f())

# 利用装饰器测试一个函数的运行时间
def sum_time(aaa):
    def bbb(a, b):
        t1 = time.time()
        aaa(a, b)
        t2 = time.time()
        return t2 - t1
    return bbb

@sum_time
def print_num():
    for i in range(10000):
        print(i, end=' ')
        if i == 9999:
            print('\n')

# print(print_num())
# print(sum_time(print_num)())

@sum_time
def sum_2(a, b):
    print(a + b)


print(sum_2(1, 3))
