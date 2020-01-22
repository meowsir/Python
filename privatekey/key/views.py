from django.shortcuts import render

# Create your views here.

from . import models
# 引入模块
from django.utils.timezone import now
 
 
# Create your views here.
 
 
def lists(req):
    data = {}
    listdata = models.UserInfo.objects.all()
    data['list'] = listdata
    return render(req, 'lists.html', data)
 
 
# 路由中指定要调用的函数,传入一个用户请求参数
def index(request):
    # 返回HTML页面时,使用render来渲染和打包
    return render(request, 'index.html')
 
 
def insert(request):
    if request.method == 'GET':
        return render(request, 'register.html')
    elif request.method == "POST":
        name = request.POST.get("name", None)
        account = request.POST.get("account", None)
        password = request.POST.get("password", None)
        models.UserInfo.objects.create(name=name, account=account, password=password,create_date=now())
        return redirect('student:lists')