from django.shortcuts import render
from django.http import HttpResponse
from myapp.models import *
from django.forms.models import model_to_dict
from myapp.models import *

def show_history_temperature(request):
    resultList = temperature_db.objects.all().order_by("-datetime")
    for d in resultList:
        print(model_to_dict(d))
    print("hello1")
    return HttpResponse("hello")
    # return render(request,"show_history_temperature.html",locals())
