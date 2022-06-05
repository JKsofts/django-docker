from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

# Create your views here.

def hello(request):
    print("request body:", request)
    return HttpResponse("hello guys")

def hi(request):
    return JsonResponse({"work": "rESPONSE dONE", "done": [1,2,3,4]})

