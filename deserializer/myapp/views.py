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
        
    if request.method == "DELETE":
        json_data = request.body
        stream = io.BytesIO(json_data)
        data = JSONParser().parse(stream)
        id = data.get('id')
        Table.objects.filter(id=id).delete()
        r = {"data":"Data Deleted Successfully...."}
        return JsonResponse(r,content_type='application/json')
    
    if request.method == "PUT":
        json = request.body
        # print(type(json))
        s = io.BytesIO(json)
        # print(type(s))
        data = JSONParser().parse(s)
        print(type(data))
        id = data.get('id')
        instance = Table.objects.get(pk=id)
        des = Desrializer(instance, data = data, partial=True)
        if des.is_valid():
            des.save()
            r = {'data':'Data Created'}
            return JsonResponse(r,content_type='application/json')
        
    if request.method == "GET":
        data1 = Table.objects.all()
        a = Desrializer(data1,many=True)
        return JsonResponse(a.data,safe=False)
    return JsonResponse('abc', content_type='application/json')
