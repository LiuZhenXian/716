from django.shortcuts import render
from django.shortcuts import HttpResponse
from django.views.decorators.csrf import csrf_exempt
# Create your action here.


#地图控制器
@csrf_exempt
def map(request):
    if request.method == 'GET':    #判断请求方式
        return render(request, 'mapviews/map.html')