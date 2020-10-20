from django.shortcuts import render
from django.shortcuts import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from jsapp.service import KgService
import json
# Create your action here.


#图谱控制器
@csrf_exempt
def entitykg(request):#实体图谱
    if request.method == 'GET':    #判断请求方式
        return render(request, 'kgviews/entitykg.html')

@csrf_exempt
def orderkg(request):#指令推理
    if request.method == 'GET':    #判断请求方式
        return render(request, 'kgviews/orderkg.html')
    elif request.method=='POST':
        reason=KgService.MainKgCheck()
        if len(reason)>0:
            res=json.dumps(reason)
            return HttpResponse(res)
        else:
            return HttpResponse(0)
