from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import StudInfo
from .serilizer import StudSerializer
from rest_framework import viewsets
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def index(request):
    res = [{"msg": "Hello, world. You're at the polls index."}]
    if request.method == 'POST':
        print(request.POST.get('uname'))
        print(request.POST.get('pass'))
        print("hi")
    return JsonResponse(res,safe=False)

class StudData(viewsets.ModelViewSet):
    queryset = StudInfo.objects.all()
    serializer_class = StudSerializer



