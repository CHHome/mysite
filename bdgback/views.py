from django.shortcuts import render
from django.shortcuts import HttpResponse
from django.db import connection
from  bdgback import models

def index(request):
    return render(request, "index.html")


# 获取get参数
def login(request):
    if request.method == 'GET':
        username = request.GET.get('username')
        password = request.GET.get('password')
        models.UserInfo.objects.create(username=username, password=password)
        user_list = models.UserInfo.objects.all()
        return HttpResponse(len(user_list))

def show(request):
    if request.method == 'GET':
        user = models.UserInfo.objects.order_by('id')
        return HttpResponse(len(user))
