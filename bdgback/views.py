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
        p = models.UserInfo.objects.create(username=username, password=password)
        p.save()
        user_list = models.UserInfo.objects.all()
        return HttpResponse(len(user_list))
# Create your views here.
