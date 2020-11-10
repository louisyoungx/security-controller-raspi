import json
from django.http import HttpResponse
from django.shortcuts import render
from django.middleware.csrf import get_token
from django.utils.decorators import method_decorator
from django.views import View

# Create your views here.
from django.views.decorators.csrf import csrf_exempt


class Token(View):

    def get(self, request):
        token = get_token(request)
        return HttpResponse(json.dumps({'token': token}), content_type="application/json,charset=utf-8")


@method_decorator(csrf_exempt, name='dispatch')

class OpenGate(View):
    def get(self, request):
        pass
    def post(self, request):
        ID = request.POST.get("ID")
        FromUrl = request.POST.get("FromUrl")
        if FromUrl == "https://louisyoung.work":

            # TODO 此处业务处理

            return HttpResponse(200)
        else:
            return HttpResponse(404)
