import json
import time

from django.http import HttpResponse
from django.middleware.csrf import get_token
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt

from utils.Camera import Camera
from utils.Gate import gate


# Create your views here.


class Token(View):

    def get(self, request):
        token = get_token(request)
        return HttpResponse(json.dumps({'token': token}), content_type="application/json,charset=utf-8")


class OpenGate(View):
    def get(self, request):
        pass
    def post(self, request):
        ID = request.POST.get("ID")
        FromUrl = request.POST.get("FromUrl")
        if FromUrl == "https://louisyoung.work":
            ID = str(time.time())[:10]

            # TODO 此处业务处理
            camera = Camera(ID)
            camera.shoot()
            camera.save()

            # 开门
            gate.open()

            return HttpResponse(200)
        else:
            return HttpResponse(404)
