from django.db import models
import django.utils.timezone as timezone

# Create your models here.
class User(models.Model):
    user_id = models.BigIntegerField()  # 用户注册手机号
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    isSupperuser = models.IntegerField(default=0)        # 0.超级用户    1.普通用户
    # 激活状态
    state = models.IntegerField(default=0)  # 0.已激活  1.未激活
    # 静态余额
    static_balance = models.IntegerField(default=0)
    # 静态冻结
    static_blocked_balance = models.IntegerField(default=0)
    # 动态余额
    dynamic_balance = models.IntegerField(default=0)
    # 家园币余额
    jiayuan_coin = models.IntegerField(default=5)
    # 推荐人手机号
    superior_phone = models.BigIntegerField(default=0)
    # 身份证号
    id_card = models.CharField(max_length=20)
    # 银行卡号
    bank_card = models.IntegerField()
    # 支付宝账户
    alipay_id = models.CharField(max_length=20)
    # 支付密码
    pay_pwd = models.CharField(max_length=20)
    # 是否为首轮
    is_first = models.IntegerField(default=0)

    class Meta:
        db_table = 'User'


#买入模型
class Buyer(models.Model):
    user_id = models.BigIntegerField()  # 用户注册手机号
    username = models.CharField(max_length=20)
    count = models.IntegerField()  # 交易金额
    order_status = models.IntegerField()  # 交易状态
    add_time = models.DateTimeField(default=timezone.now)

    class Meta:
        db_table = 'Buyer'


# 卖出模型
class Order(models.Model):
    user_id = models.BigIntegerField()  # 用户注册手机号
    username = models.CharField(max_length=20)
    count = models.IntegerField()  # 交易金额
    order_status = models.IntegerField()  # 交易状态
    add_time = models.DateTimeField(default=timezone.now)

    class Meta:
        db_table = 'Order'


# 订单模型
class Match_a(models.Model):
    orderNo = models.CharField(max_length=20)
    seller_id = models.BigIntegerField()  # 用户注册手机号
    seller_name = models.CharField(max_length=20)
    buyer_id = models.BigIntegerField()  # 用户注册手机号
    buyer_name = models.CharField(max_length=20)
    money = models.BigIntegerField()
    order_status = models.IntegerField()
    add_time = models.DateTimeField()
    end_time = models.DateTimeField()
    images = models.CharField(max_length=300)  # 匹配截图

    class Meta:
        db_table = 'Match'

# class Static_balance(models.Model):
#     user_id = models.BigIntegerField()  # 用户注册手机号
#
# class Static_blocked(models.Model):
#     user_id = models.BigIntegerField()  # 用户注册手机号
#     capital = models.IntegerField()  # 本金
#     interest = models.IntegerField()  # 利息
#     state = models.IntegerField(default=0)  # 0.冻结中  1.已解冻
#     time = models.FloatField()  # 解冻时间，明细
#     fund = models.IntegerField()  # 金额
#
# class Dynamic_balance(models.Model):
#     user_id = models.BigIntegerField()  # 用户注册手机号
#
# class Jiayuan_coin(models.Model):
#     user_id = models.BigIntegerField()  # 用户注册手机号