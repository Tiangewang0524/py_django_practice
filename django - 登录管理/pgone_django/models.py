from django.db import models


class User(models.Model):
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    isSupperuser = models.IntegerField()        # 0.超级用户    1.普通用户
    role = models.IntegerField()         # 0.java        1.UI          2.Web
    remark = models.CharField(max_length=255)

    class Meta:
        db_table = 'User'


class Problem(models.Model):
    context = models.CharField(max_length=255)
    # 问题类型
    type = models.IntegerField()
    raise_user = models.IntegerField()
    raise_time = models.FloatField()
    state = models.IntegerField()
    solve_user = models.IntegerField()
    solve_time = models.FloatField()
    remark = models.CharField(max_length=255)

    class Meta:
        db_table = 'Problem'
