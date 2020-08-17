from .models import Role
from django.shortcuts import render
from rest_framework.views import csrf_exempt
from .serializer import RoleSerializer
from django.http import JsonResponse,HttpResponse
from rest_framework.parsers import parse, JSONParser

# Create your views here.
@csrf_exempt
def Display(request):
    obj=Role.objects.all()
    serial=RoleSerializer(obj,many=True)
    return JsonResponse(serial.data,safe=False)

@csrf_exempt
def Insert(request):
    content = JSONParser().parse(request)
    serial = RoleSerializer(data=content)
    if serial.is_valid():
        serial.save()
        return JsonResponse(serial.data, status=201)
    return JsonResponse(serial.errors, status=400)

@csrf_exempt
def Update(request,pk):
    try:
        ques=Role.objects.get(pk=pk)
    except Role.DoesNotExist:
        return HttpResponse(status=404)
    content = JSONParser().parse(request)
    serial = RoleSerializer(ques,data=content)
    if serial.is_valid():
        serial.save()
        return JsonResponse(serial.data)
    return JsonResponse(serial.errors,status=400)


@csrf_exempt
def Delete(request, pk):
    try:
        role = Role.objects.get(pk=pk)
    except Role.DoesNotExist:
        return HttpResponse(status=404)
    role.delete()
    return HttpResponse(status=204)
