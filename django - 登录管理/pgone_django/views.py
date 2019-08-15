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
        result = {'code': '0000', 'message': '登陆成功'}
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
            userid = item.raise_user
            item.raise_user = raise_name
            solve_user = User.objects.filter(id=item.solve_user).first()
            if solve_user:
                item.solve_user = solve_user.username
            # model_to_dict 返回一个字典文件
            dict_temp = model_to_dict(item)
            # 向字典文件里添加一个提出问题的用户的id，方便查找相关人的提问
            dict_temp['raise_user_id'] = userid
            data.append(dict_temp)
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

class Delete_record(View):

    def post(self, request):
        result = {'code': '0000', 'message': 'success'}
        pro_id = request.POST.get('pro_id')
        try:
            Problem.objects.filter(id=pro_id).delete()
        except:
            result['code'] = '0001'
            result['message'] = '修改失败'
        return HttpResponse(json.dumps(result), content_type='application/json')


class Add_problem(View):

    def post(self, request):
        result = {'code': '0000', 'message': 'success'}
        problem = request.POST.get('problem')
        user_id = request.POST.get('user_id')
        user = User.objects.get(id=user_id)
        try:
            Problem.objects.create(context=problem, type=user.role, raise_user=user_id, raise_time=int(time.time()), state=0)
        except:
            result['code'] = '0001'
            result['message'] = '添加失败'
        return HttpResponse(content=json.dumps(result), content_type='application/json')
