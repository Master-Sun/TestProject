import os
from django.shortcuts import render, HttpResponse
from django.core.mail import send_mail
from django.conf import settings


UPLOAD_PATH = 'D:\\test1\\'
# Create your views here.
def files_upload(request):
    if request.method == 'GET':
        return render(request, 'filesupload.html')
    elif request.is_ajax():
        # 根据input框的name属性值取到文件对象
        files = request.FILES.getlist('files')
        for file in files:
            # 获取文件名，文件对象的__str__属性返回的是文件名
            file_name = str(file)
            with open(os.path.join(UPLOAD_PATH, file_name), 'wb') as f:
                # 分块写入，防止大文件卡死
                for chunk in file.chunks(chunk_size=2014):
                    f.write(chunk)
        return HttpResponse('ajaxOK')
    elif request.method == 'POST':
        # 获取上传文件对象的列表
        files = request.FILES.getlist('files')
        for file in files:
            file_name = str(file)
            with open(os.path.join(UPLOAD_PATH, file_name), 'wb') as f:
                for chunk in file.chunks(chunk_size=2014):
                    f.write(chunk)
        return HttpResponse('OK')


def send_email(request):
    subject = "主题：注册验证码"
    message = "内容：123456"
    sender = settings.EMAIL_FROM
    reciever = ['779625568@qq.com']    # 邮箱地址瞎写的也能发送成功，之后邮箱会收到一个退信的通知
    # fail_silently：邮件未正常发送则抛出异常，设置为True则不会抛出异常
    # 返回值为1则发送成功，0为发送失败
    result= send_mail(subject, message, sender, reciever, fail_silently=True)
    print(result)
    return HttpResponse("OK")


