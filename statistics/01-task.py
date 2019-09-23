#算术平均数
def mean_num(num):
    sum = 0
    for i in range(len(num)):
        sum += num[i]
    return sum / len(num)


#几何平均数
def geo_num(num):
    multi = 1
    for i in range(len(num)):
        multi *= num[i]
    return multi ** (1/len(num))


#中位数
def median_num(num):
    list_a = [num[i] for i in range(len(num))]
    list_a.sort()
    length = len(num)
    if length % 2 == 1:
        i = int((length + 1) / 2)-1
        return list_a[i]
    else:
        i = int(length / 2)-1
        return (list_a[i] + list_a[i + 1]) / 2


#众数
def mode_num(num):
    dict_a = dict()
    for i in range(len(num)):
        if num[i] in dict_a.keys():
            dict_a[num[i]] += 1
        else:
            dict_a[num[i]] = 1
    list_1 = sorted(dict_a.items(), key=lambda x: x[1], reverse=True)
    return list_1[0][0]


#极差
def Range(num):
    max_num = max(num)
    min_num = min(num)
    return max_num - min_num


#百分位数
def percentile_num(num, percent):
    list_a = [num[i] for i in range(len(num))]
    list_a.sort()
    length = len(num)
    if length % 2 == 1:
        i = int((length + 1) * percent) - 1
        return list_a[i]
    else:
        i = int(length * percent) - 1
        return (list_a[i] + list_a[i + 1]) / 2


#第一四分位数
def quartile_num(num):
    list_a = [num[i] for i in range(len(num))]
    list_a.sort()
    length = len(num)
    if length % 2 == 1:
        i = int((length + 1) / 4)-1
        return list_a[i]
    else:
        i = int(length / 4)-1
        return (list_a[i] + list_a[i + 1]) / 2


#方差
def variance_num(num):
    mean = mean_num(num)
    sum = 0
    for i in range(len(num)):
        sub = num[i] - mean
        sub = sub ** 2
        sum += sub
    return sum / len(num)


#标准差
def standard_deviation(num):
    var = variance_num(num)
    return var ** 0.5

