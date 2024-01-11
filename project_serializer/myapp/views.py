from django.shortcuts import render,HttpResponse
from rest_framework.renderers import JSONRenderer
from .serializers import TableSerializer
from .models import Table
from django.http import JsonResponse

# Create your views here.
def Fetching_data(request):
    data = Table.objects.all()
    ser = TableSerializer(data,many=True)   
    return JsonResponse(ser.data,safe=False)

