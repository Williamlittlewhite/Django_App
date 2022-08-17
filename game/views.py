from django.http import HttpResponse


def index(request):
    line1 = '<h1 style="text-align: center">一果可爱捏</h1>'
    line3 = '<a href="/play/">进入第二个网页</a>'
    line4 = '<hr>'
    line2 = '<img src="http://tiebapic.baidu.com/forum/w%3D580/sign=c09364e35cd8bc3ec60806c2b28aa6c8/689f9efb513d2697f5fcd98410fbb2fb4216d8b6.jpg?tbpicau=2022-08-19-05_7767172ff6c1c030a7b9a803b7ac44b5" width=800>'
    return HttpResponse(line1+line3+line4+line2)

def play(request):
    line1 = '<h1 style="text-align: center">一果相当可爱捏</h1>'
    line3 = '<a href="/">返回上级页面</a>'
    line2 = '<img src="http://tiebapic.baidu.com/forum/w%3D580/sign=f4355c70ec014c08193b28ad3a7a025b/81279f22dd54564e8f4935e0f6de9c82d0584fb4.jpg?tbpicau=2022-08-19-05_28ddd77644d677d2e7776c5db24b4d28" width=800>'

    return HttpResponse(line1+line3+line2)
