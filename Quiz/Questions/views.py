from .models import Question
from django.http import HttpResponse,JsonResponse
from rest_framework.parsers import parse, JSONParser
from django.shortcuts import render
from .serializer import QuesSerializers,FewSerializer
from rest_framework.views import csrf_exempt
from random import randint

# Create your views here.
@csrf_exempt
def Display(request):
    ques=Question.objects.all()
    serial=QuesSerializers(ques,many=True)
    return JsonResponse(serial.data,safe=False)

@csrf_exempt
def Display_id(request,pk):
    try:
        ques=Question.objects.get(pk=pk)
    except Question.DoesNotExist:
        return HttpResponse(status=404)
    serial=QuesSerializers(ques)
    return JsonResponse(serial.data)

@csrf_exempt
def Insert(request):
        content=JSONParser().parse(request)
        serial=QuesSerializers(data=content)
        if serial.is_valid():
            serial.save()
            return JsonResponse(serial.data,status=201)
        return JsonResponse(serial.errors,status=400)

@csrf_exempt
def Update(request,pk):
    try:
        ques=Question.objects.get(pk=pk)
    except Question.DoesNotExist:
        return HttpResponse(status=404)
    content = JSONParser().parse(request)
    serial = QuesSerializers(ques,data=content)
    if serial.is_valid():
        serial.save()
        return JsonResponse(serial.data)
    return JsonResponse(serial.errors,status=400)


@csrf_exempt
def Delete(request, pk):
    try:
        ques = Question.objects.get(pk=pk)
    except Question.DoesNotExist:
        return HttpResponse(status=404)
    ques.delete()
    return HttpResponse(status=204)

@csrf_exempt
def random(request):
    #fields=('Question','Option_A','Option_B',
            #'Option_C','Option_D')
    random_object = Question.objects.all().distinct().order_by('?')[:10]
    serial = FewSerializer(random_object, many=True)
    return JsonResponse(serial.data, safe=False)

