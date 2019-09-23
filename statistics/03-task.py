from math import *


# 列联表相关系数
# coefficient of contingency
def coc(n):
    # n 为二维数组
    n11 = n[1][1]
    n01 = n[0][1]
    n10 = n[1][0]
    n00 = n[0][0]
    n1o = n11 + n10
    no1 = n11 + n01
    no0 = n10 + n00
    n0o = n01 + n00

    phi = (n11 * n00 - n10 * n01) / sqrt(n1o * n0o * no0 * no1)

    return phi


# 斯皮尔曼等级相关系数
# Spearman’s correlation coefficient for ranked data
# key:Xi, value:Yi
def spearman(dict_a):
    # 对键排序
    list_key = sorted(dict_a.keys())
    # xi 排名列表
    list_xi = [i for i in range(len(1, list_key+1))]
    temp = list(zip(list_key, list_xi))
    # 拼接后转成列表，保存排名
    list_Xi = []
    for xi in list_key:
        for i, j in temp:
            if xi == i:
                list_Xi.append(j)


    # 对值排序
    list_val = sorted(dict_a.values())
    # yi 排名列表
    list_yi = [i for i in range(len(1, list_val + 1))]
    temp = list(zip(list_val, list_yi))
    # 拼接后转成列表，保存排名
    list_Yi = []
    for yi in list_val:
        for i, j in temp:
            if yi == i:
                list_Yi.append(j)

    Xi_Yi = [[key, value] for key, value in dict_a.items()]
    n = len(Xi_Yi)
    for i in range(n):
        Xi_Yi[i].append(list_Xi[i])
        Xi_Yi[i].append(list_Yi[i])
    # Xi_Yi 中的每一个子列表格式为：[xi, yi, xi排名, yi排名]

    sum = 0
    for each in Xi_Yi:
        d = each[2] - each[3]
        d2 = d ** 2
        sum += d2

    p = 1 - (6 * sum) / (n * (n ** 2 - 1))

    return p


# 皮尔逊积差系数
# Pearson correlation coefficient
def pearson(dict_a):
    # 平均数
    def mean_num(num):
        sum = 0
        for i in range(len(num)):
            sum += num[i]
        return sum / len(num)

    # 方差
    def variance_num(num):
        mean = mean_num(num)
        sum = 0
        for i in range(len(num)):
            sub = num[i] - mean
            sub = sub ** 2
            sum += sub
        return sum / len(num)

    # 标准差
    def standard_deviation(num):
        var = variance_num(num)
        return var ** 0.5

    # 以 SD 表示x, y, 并求积
    def sd(x, y, avg_x, avg_y, sd_x, sd_y):
        x_sd = (x - avg_x) / sd_x
        y_sd = (y - avg_y) / sd_y

        return x_sd * y_sd

    list_x = dict_a.keys()
    list_y = dict_a.values()
    avg_x = mean_num(list_x)
    avg_y = mean_num(list_y)
    sd_x = standard_deviation(list_x)
    sd_y = standard_deviation(list_y)
    sum = 0
    for x, y in zip(list_x, list_y):
        sum += sd(x, y, avg_x, avg_y, sd_x, sd_y)
    r = sum / len(list_x)

    return r


# 最小二乘法
# Least squares
def ls(dict_a):
    # 平均数
    def mean_num(num):
        sum = 0
        for i in range(len(num)):
            sum += num[i]
        return sum / len(num)

    list_x = dict_a.keys()
    list_y = dict_a.values()
    avg_x = mean_num(list_x)
    avg_y = mean_num(list_y)

    # 分子，分母
    numerator, denominator = 0, 0
    for i in range(len(list_x)):
        numerator += (list_x[i] - avg_x) * (list_y[i] - avg_y)
        denominator += (list_x[i] - avg_x) ** 2
    b = numerator / denominator
    a = avg_y - b * avg_x

    return a
