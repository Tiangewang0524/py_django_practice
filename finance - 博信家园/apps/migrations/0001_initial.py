# Generated by Django 2.2.4 on 2019-09-05 11:17

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Buyer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.BigIntegerField()),
                ('username', models.CharField(max_length=20)),
                ('count', models.IntegerField()),
                ('order_status', models.IntegerField()),
                ('add_time', models.DateTimeField(default=django.utils.timezone.now)),
            ],
            options={
                'db_table': 'Buyer',
            },
        ),
        migrations.CreateModel(
            name='Match',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('orderNo', models.CharField(max_length=20)),
                ('seller_id', models.BigIntegerField()),
                ('seller_name', models.CharField(max_length=20)),
                ('buyer_id', models.BigIntegerField()),
                ('buyer_name', models.CharField(max_length=20)),
                ('money', models.BigIntegerField()),
                ('order_status', models.IntegerField()),
                ('add_time', models.DateTimeField()),
                ('end_time', models.DateTimeField()),
                ('images', models.CharField(max_length=300)),
            ],
            options={
                'db_table': 'Match',
            },
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.BigIntegerField()),
                ('username', models.CharField(max_length=20)),
                ('count', models.IntegerField()),
                ('order_status', models.IntegerField()),
                ('add_time', models.DateTimeField(default=django.utils.timezone.now)),
            ],
            options={
                'db_table': 'Order',
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.BigIntegerField()),
                ('username', models.CharField(max_length=20)),
                ('password', models.CharField(max_length=20)),
                ('isSupperuser', models.IntegerField(default=0)),
                ('state', models.IntegerField(default=0)),
                ('static_balance', models.IntegerField(default=0)),
                ('static_blocked_balance', models.IntegerField(default=0)),
                ('dynamic_balance', models.IntegerField(default=0)),
                ('jiayuan_coin', models.IntegerField(default=5)),
                ('superior_phone', models.BigIntegerField(default=0)),
                ('id_card', models.CharField(max_length=20)),
                ('bank_card', models.IntegerField()),
                ('alipay_id', models.CharField(max_length=20)),
                ('pay_pwd', models.CharField(max_length=20)),
                ('is_first', models.IntegerField(default=0)),
            ],
            options={
                'db_table': 'User',
            },
        ),
    ]
