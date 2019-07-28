from django.shortcuts import render
from django.http import JsonResponse

from celerytask.tasks import TestTask    # 导入需要执行的任务

# Create your views here.
def do(request):
    print("接受到请求...")
    # 执行异步任务
    # TestTask.delay()
    # 第二种启动方式，可以传参和指定队列
    TestTask.apply_async(args=("这是args",), queue='work_queue')
    print("结束请求...")
    return JsonResponse({"result": "ok"})