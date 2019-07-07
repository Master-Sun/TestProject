import os
from django.shortcuts import render, HttpResponse


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

