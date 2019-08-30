from django.db import models

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
    id_card = models.BigIntegerField()
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