from django.shortcuts import render
from django.shortcuts import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from jsapp.service import LoginService
import json
# Create your action here.

#登录控制器
USER_LIST = {}
@csrf_exempt
def login(request):
    if request.method == 'GET':    #判断请求方式
        return render(request, 'loginviews/login.html')
    elif request.method == 'POST':
        user = request.POST.get('user')   #post请求，输入框获取值
        pwd = request.POST.get('pwd')
        reason=LoginService.loginCheck(user,pwd)
        if len(reason)>0:
            res=json.dumps(reason)
            return HttpResponse(res)
        else:
            return HttpResponse(0)
    else:
        return HttpResponse(0)   #HttpResponse("字符串")
