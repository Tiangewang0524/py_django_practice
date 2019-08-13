from django.shortcuts import render
from django.views import View
from .models import *
from django.http import HttpResponse
from django.forms import model_to_dict
import json, time


def index(request):
    # return HttpResponse("Hello, world. You're at the polls index.")
    return render(request, 'pgone_django/index.html', {'aaa': 'bbb'})


class Login(View):

    def post(self, request):
        result = {'code': '0000', 'message': '登陆成功', 'data': 'id'}
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = User.objects.filter(username=username).first()
        if user:
            if user.password == password:
                result['data'] = user.id
            else:
                result['code'] = '0001'
                result['message'] = '密码错误'
        else:
            result['code'] = '0002'
            result['message'] = '用户不存在'
        return HttpResponse(content=json.dumps(result), content_type='application/json')


class view_register(View):

    def post(self, request):
        result = {'code': '0000', 'message': 'success'}
        username = request.POST.get('username')
        password = request.POST.get('password')
        is_user = User.objects.filter(username=username)
        if not is_user:
            User.objects.get_or_create(username=username, password=password, isSupperuser=0, role=2)
        else:
            result['code'] = '0001'
            result['message'] = '用户已存在'
        # user_db = User(username = username)
        # user_db.username = username
        # user_db.password = password
        # user_db.isSupperuser = 0
        # user_db.role = 2
        # user_db.remark = 5
        # user_db.save()
        # User.objects.all()
        return HttpResponse(content=json.dumps(result), content_type='application/json')


class UserMsg(View):

    def get(self, request):
        result = {'code': '0000', 'message': 'success'}
        user_id = request.GET.get('user_id')
        user = User.objects.get(id=user_id)
        # problem 的type 跟 user 的 role 相对应
        problems = Problem.objects.filter(type=user.role)
        data = []
        for item in problems:
            raise_name = User.objects.filter(id=item.raise_user).first().username
            item.raise_user = raise_name
            solve_user = User.objects.filter(id=item.solve_user).first()
            if solve_user:
                item.solve_user = solve_user.username
            data.append(model_to_dict(item))
        result['data'] = data
        return HttpResponse(json.dumps(result), content_type='application/json')


class Modify_state(View):

    def post(self, request):
        result = {'code': '0000', 'message': 'success'}
        user_id = request.POST.get('user_id')
        pro_id = request.POST.get('pro_id')
        try:
            Problem.objects.filter(id=pro_id).update(state=1, solve_user=user_id, solve_time=int(time.time()))
        except:
            result['code'] = '0001'
            result['message'] = '修改失败'
        return HttpResponse(json.dumps(result), content_type='application/json')
