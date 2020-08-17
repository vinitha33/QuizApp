from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from rest_framework.parsers import JSONParser
from rest_framework.views import csrf_exempt
# Create your views here.
from .models import Users
from .serializer import AddSerializer,LoginSerializer


@csrf_exempt
def Display(request):
    obj=Users.objects.all()
    serial=AddSerializer(obj,many=True)
    return JsonResponse(serial.data,safe=False)

@csrf_exempt
def Display_id(request,pk):
    try:
        use=Users.objects.get(pk=pk)
    except Users.DoesNotExist:
        return HttpResponse(status=404)
    serial=AddSerializer(use)
    return JsonResponse(serial.data)

@csrf_exempt
def Insert(request):
    content = JSONParser().parse(request)
    serial = AddSerializer(data=content)
    if serial.is_valid():
        serial.save()
        return JsonResponse(serial.data, status=201)
    return JsonResponse(serial.errors, status=400)

@csrf_exempt
def Update(request,pk):
    try:
        use=Users.objects.get(pk=pk)
    except Users.DoesNotExist:
        return HttpResponse(status=404)
    content = JSONParser().parse(request)
    serial = AddSerializer(use,data=content)
    if serial.is_valid():
        serial.save()
        return JsonResponse(serial.data)
    return JsonResponse(serial.errors,status=400)


@csrf_exempt
def Delete(request, pk):
    try:
        use = Users.objects.get(pk=pk)
    except Users.DoesNotExist:
        return HttpResponse(status=404)
    use.delete()
    return HttpResponse(status=204)

@csrf_exempt
def login(request):
    log=Users.objects.all()
    serial=LoginSerializer(log,many=True)
    return JsonResponse(serial.data,safe=False)

@csrf_exempt
def Login_id(request,pk):
    try:
        use=Users.objects.get(pk=pk)
    except Users.DoesNotExist:
        return HttpResponse(status=404)
    serial=LoginSerializer(use)
    return JsonResponse(serial.data)


data=[{"userId":1,
     "Answers":[{"qno":"1","selected":"abcd"},
                {"qno":"2","selected":"abcd"},
                {"qno":"3","selected":"abcd"},
                {"qno":"4","selected":"abcd"},
                {"qno":"5","selected":"abcd"},
                {"qno":"6","selected":"abcd"},
                {"qno":"7","selected":"abcd"},
                {"qno":"8","selected":"abcd"},
                {"qno":"9","selected":"abcd"},
                {"qno":"10","selected":"abcd"}]}]
