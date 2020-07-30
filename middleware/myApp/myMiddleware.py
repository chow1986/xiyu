#自定义中间件
#如果想使用中间件，在setting.py文件中配置， 在MIDDLEWARE下配置‘middleware.myApp.myMiddle.MyMiddle’
from django.utils.deprecation import MiddlewareMixin
class MyMiddle(MiddlewareMixin):
    def process_request(self,request):
        print("get参数为： ",request.GET.get('a'))