from math import *


# 排列
def permutation(n, k):
    # p n k
    return factorial(n) / factorial((n-k))


# 组合
def combination(n, k):
    # c n k
    return factorial(n) / (factorial((n-k)) * (factorial(k)))


# 期望
# 参数：字典 键:随机变量所有可能的取值 值：相对应的概率
def expectation(dict_a):
    sum = 0
    # list_var = dict_a.keys()
    # list_pro = dict_a.values()
    # for i in range(len(list_var)):
    #     sum += list_var[i] * list_pro[i]
    for keys, values in dict_a:
        sum += keys * values
    return sum


# 方差
def variance(dict_a):

    sum = 0

    # 期望的值
    num_expectation = expectation(dict_a)

    # 键:随机变量所有可能的取值 值：相对应的概率
    for keys, values in dict_a:
        sum += (keys - num_expectation)**2 * values
    return sum


# 标准差
def standard_deviation(num):
    var = variance(num)
    return sqrt(var)


# 几何分布
def geometric_distribution(p, r):
    dict_a = dict()
    q = 1 - p

    # 几何分布的概率计算公式为：
    dict_a['pro'] = p * (q ** (r - 1))
    # 需要计算至少要试验r次以上才能取得第一次成功的概率为：
    dict_a['pro_2'] = q ** r
    # 几何分布的期望和方差公式为：
    dict_a['E(x)'] = 1 / p
    dict_a['Var(x)'] = q / (p ** 2)

    return dict_a


# 二项分布
def binomial_distribution(n, p, r):
    dict_a = dict()
    # c n r
    cnr = combination(n, r)
    q = 1 - p

    # 二项分布的概率计算公式为：
    dict_a['pro'] = cnr * (p ** r) * (q ** (n - r))

    # 二项分布的期望和方差公式为：
    dict_a['E(x)'] = n * p
    dict_a['Var(x)'] = n * p * q

    return dict_a


# 泊松分布
def poisson_distribution(lamb, r):
    dict_a = dict()

    # 二项分布的概率计算公式为：
    dict_a['pro'] = (e ** (-lamb)) * (lamb ** r) / factorial(r)

    # 二项分布的期望和方差公式为：
    dict_a['E(x)'] = lamb
    dict_a['Var(x)'] = lamb

    return dict_a
