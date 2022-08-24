from django.shortcuts import render
#render在服务器端渲染一个html文件
def index(request):
    return render(requese,"multiends/web.html") #从templates文件夹开始下写

