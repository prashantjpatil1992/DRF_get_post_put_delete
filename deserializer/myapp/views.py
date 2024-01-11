from django.shortcuts import render
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
import io
from .models import Table
from .serializers import Desrializer
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
# Create your views here.

@csrf_exempt
def create(request):
    if request.method == "POST":
        json_data = request.body
        stream = io.BytesIO(json_data)
        data = JSONParser().parse(stream)
        des = Desrializer(data = data)
        if des.is_valid():
            des.save()
            r = {"data":"Data Created Successfully"}
            return JsonResponse(r,content_type='application/json')
    return JsonResponse(des.error, content_type='application/json')
