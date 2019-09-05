from django.shortcuts import render
from django.views import View
from .models import *
from django.http import HttpResponse
from django.forms import model_to_dict
import json, time, datetime


# 使json能序列化datetime
class DateEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime.datetime):
            return obj.strftime('%Y-%m-%d %H:%M:%S')

        elif isinstance(obj, datetime.date):
            return obj.strftime("%Y-%m-%d")

        else:
            return json.JSONEncoder.default(self, obj)


# Create your views here.
class Login(View):

    def post(self, request):
        result = {'code': '0000', 'message': '登陆成功'}
        # user_id 为手机号
        user_id = request.POST.get('user_id')
        password = request.POST.get('password')
        user = User.objects.filter(user_id=user_id).first()
        if user:
            if user.password == password:
                result['data'] = user_id
                result['state'] = user.state
                result['isSupperUser'] = user.isSupperuser
            else:
                result['code'] = '0001'
                result['message'] = '密码错误'
        else:
            result['code'] = '0002'
            result['message'] = '用户不存在'
            # 增加cookie用于注册，省略重复输入手机号
            result['data'] = user_id
        return HttpResponse(content=json.dumps(result), content_type='application/json')


class Register(View):

    def post(self, request):
        result = {'code': '0000', 'message': 'success'}
        user_id = request.POST.get('user_id')
        username = request.POST.get('username')
        password = request.POST.get('password')
        alipay_id = request.POST.get('alipay_id')
        pay_pwd = request.POST.get('pay_pwd')
        superior_phone = request.POST.get('superior_phone')
        bank_card = request.POST.get('bank_card')
        is_user = User.objects.filter(user_id=user_id)
        if not is_user:
            if superior_phone:
                User.objects.get_or_create(user_id=user_id, username=username, password=password, alipay_id=alipay_id,
                                           pay_pwd=pay_pwd, superior_phone=superior_phone, bank_card=bank_card)
            else:
                User.objects.get_or_create(user_id=user_id, username=username, password=password, alipay_id=alipay_id,
                                           pay_pwd=pay_pwd, bank_card=bank_card)
        else:
            result['code'] = '0001'
            result['message'] = '用户已存在'
        return HttpResponse(content=json.dumps(result), content_type='application/json')


class User_main(View):

    def get(self, request):
        result = {'code': '0000', 'message': 'success'}
        user_id = request.GET.get('user_id')
        user = User.objects.get(user_id=user_id)
        result['user'] = model_to_dict(user)
        return HttpResponse(json.dumps(result), content_type='application/json')


class Activate(View):

    def post(self, request):
        result = {'code': '0000', 'message': 'success'}
        user_id = request.POST.get('user_id')
        password = request.POST.get('password')
        id_card = request.POST.get('id_card')
        user = User.objects.get(user_id=user_id)
        coins = user.jiayuan_coin
        if user.password == password:
            User.objects.filter(user_id=user_id).update(id_card=id_card, state=1, jiayuan_coin=coins-3)
        else:
            result['code'] = '0001'
            result['message'] = '密码错误'
        return HttpResponse(json.dumps(result), content_type='application/json')


class Buy(View):

    def post(self, request):
        result = {'code': '0000', 'message': 'success'}
        user_id = request.POST.get('user_id')
        user = User.objects.get(user_id=user_id)
        pay_pwd = request.POST.get('pay_pwd')
        buy_val = int(request.POST.get('buy_val'))
        balance = user.static_blocked_balance
        username = user.username
        coin = user.jiayuan_coin
        if user:
            if user.pay_pwd != pay_pwd:
                result['code'] = '0001'
                result['message'] = '交易密码错误'
            else:
                # 密码正确
                if user.is_first == 0:
                    if buy_val <= 5000:
                        if user.jiayuan_coin >= 1:
                            User.objects.filter(user_id=user_id).update(static_blocked_balance=balance + buy_val,
                                                                        jiayuan_coin=coin - 1, is_first=1)
                            Buyer.objects.create(user_id=user_id, username=username, count=buy_val, order_status=0)
                        else:
                            result['code'] = '0001'
                            result['message'] = '家园币不足，请充值！'
                    else:
                        result['code'] = '0001'
                        result['message'] = '首次购入不能超过5000！'
                else:
                    # 后一次买入金额必须大于前一次
                    last_buy = Buyer.objects.filter(user_id=user_id).order_by('-id').first()
                    if last_buy:
                        if buy_val < last_buy.count:
                            result['code'] = '0001'
                            result['message'] = '买入金额少于前一次！'
                        else:
                            if buy_val <= 5000:
                                if user.jiayuan_coin >= 1:
                                    User.objects.filter(user_id=user_id).update(static_blocked_balance=balance + buy_val,
                                                                                jiayuan_coin=coin - 1, is_first=1)
                                    Buyer.objects.create(user_id=user_id, username=username, count=buy_val, order_status=0)
                                else:
                                    result['code'] = '0001'
                                    result['message'] = '家园币不足，请充值！'
                            # 买入10000数量以上，收取2个家园币
                            if buy_val > 10000:
                                if user.jiayuan_coin >= 2:
                                    User.objects.filter(user_id=user_id).update(static_blocked_balance=balance + buy_val,
                                                                                jiayuan_coin=coin - 2, is_first=1)
                                    Buyer.objects.create(user_id=user_id, username=username, count=buy_val, order_status=0)
                                else:
                                    result['code'] = '0001'
                                    result['message'] = '家园币不足，请充值！'
                    else:
                        result['code'] = '0001'
                        result['message'] = '买入信息读取错误'
        else:
            result['code'] = '0001'
            result['message'] = '用户信息错误'
        return HttpResponse(json.dumps(result), content_type='application/json')


class Admin(View):

    def get(self, request):
        result = {'code': '0000', 'message': 'success'}
        # order = request.GET.get('order_status')
        orders = Order.objects.filter(order_status=0)
        data = []
        for order in orders:
            data.append(model_to_dict(order))
        result['data'] = data
        return HttpResponse(json.dumps(result, cls=DateEncoder), content_type='application/json')

    def post(self, request):
        result = {'code': '0000', 'message': 'success'}
        buy_orders = Buyer.objects.filter(order_status=0)
        data = []
        for order in buy_orders:
            data.append(model_to_dict(order))
        result['data'] = data
        return HttpResponse(json.dumps(result, cls=DateEncoder), content_type='application/json')


class Sell(View):

    def post(self, request):
        result = {'code': '0000', 'message': 'success'}
        user_id = request.POST.get('user_id')
        user = User.objects.get(user_id=user_id)
        pay_pwd = request.POST.get('pay_pwd')
        sell_val = int(request.POST.get('sell_val'))
        balance = user.static_balance
        time_now = datetime.datetime.now()
        username = user.username
        if user:
            if user.pay_pwd != pay_pwd:
                result['code'] = '0001'
                result['message'] = '交易密码错误'
            else:
                # 密码正确
                if sell_val > balance:
                    result['code'] = '0001'
                    result['message'] = '所出售数不能大于余额！'
                else:
                    if sell_val % 100 == 0 and sell_val >= 100:
                        # 24小时只允许卖一次
                        last_sell = Order.objects.filter(user_id=user_id).order_by('-id').first()
                        if last_sell:
                            prove_sell_time = last_sell.add_time + datetime.timedelta(hours=24)
                            if time_now < prove_sell_time:
                                result['code'] = '0001'
                                result['message'] = '24小时内只允许出售一次！'
                            else:
                                User.objects.filter(user_id=user_id).update(static_balance=balance - sell_val)
                                Order.objects.create(user_id=user_id, username=username, count=sell_val, order_status=0)
                        else:
                            # 如果是首单，则直接发布出售消息
                            User.objects.filter(user_id=user_id).update(static_balance=balance - sell_val)
                            Order.objects.create(user_id=user_id, username=username, count=sell_val, order_status=0)
                    else:
                        result['code'] = '0001'
                        result['message'] = '所出售数需为100的整数倍且不能小于100！'
        else:
            result['code'] = '0001'
            result['message'] = '用户信息错误'
        return HttpResponse(json.dumps(result), content_type='application/json')


class Match(View):

    def post(self, request):
        result = {'code': '0000', 'message': 'success'}
        buy_id = request.POST.get('all_buy').split('|')[0:-1]
        sale_id = request.POST.get('all_sale').split('|')[0:-1]
        if buy_id and sale_id:
            buy = []
            sell = []
            for i in buy_id:
                buy_msg = Buyer.objects.filter(id=i, order_status=0).first()
                buy.append(model_to_dict(buy_msg))
            for j in sale_id:
                sale_msg = Order.objects.filter(id=j, order_status=0).first()
                sell.append(model_to_dict(sale_msg))
            for i in range(len(buy)):
                buy_money = buy[i]['count']
                need_delete = []
                for j in range(len(sell)):
                    sell_money = sell[j]['count']
                    t1 = datetime.datetime.now()
                    str_time = t1.strftime("%Y%m%d%H%M%S")
                    if buy_money == sell_money:
                        a = buy[i]['user_id']
                        b = buy[i]['username']
                        Match_a.objects.create(orderNo=str_time, seller_id=buy[i]['user_id'], seller_name=buy[i]['username'],
                                             buyer_id=sell[j]['user_id'], buyer_name=sell[j]['username'],
                                             money=buy_money, order_status=0, add_time=t1)
                        Order.objects.filter(id=sell[j]['id']).update(order_status=1)
                        Buyer.objects.filter(id=buy[i]['id']).update(order_status=1)
                        need_delete.append(j)
                        break
                    if buy_money > sell_money:
                        Match_a.objects.create(orderNo=str_time, seller_id=buy[i]['user_id'], seller_name=buy[i]['username'],
                                             buyer_id=sell[j]['user_id'], buyer_name=sell[j]['username'],
                                             money=sell_money, order_status=0, add_time=t1)
                        buy_money = buy_money - sell_money
                        Order.objects.filter(id=sell[j]['id']).update(order_status=1)
                        need_delete.append(j)
                    else:
                        Match_a.objects.create(orderNo=str_time, seller_id=buy[i]['user_id'], seller_name=buy[i]['username'],
                                             buyer_id=sell[j]['user_id'], buyer_name=sell[j]['username'],
                                             money=buy_money, order_status=0, add_time=t1)
                        sell[j]['count'] = sell_money - buy_money
                        Buyer.objects.filter(id=buy[i]['id']).update(order_status=1)
                        break
                for x in need_delete[::-1]:
                    del sell[x]
            if buy or sell:
                result['code'] = '0001'
                result['message'] = '信息不匹配！'
        else:
            result['code'] = '0001'
            result['message'] = '读取匹配信息错误'
        return HttpResponse(json.dumps(result), content_type='application/json')
