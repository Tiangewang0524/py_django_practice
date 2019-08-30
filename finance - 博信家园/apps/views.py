from django.shortcuts import render
from django.views import View
from .models import *
from django.http import HttpResponse
from django.forms import model_to_dict
import json, time


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