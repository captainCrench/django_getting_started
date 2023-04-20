from django.shortcuts import render
from django.http import HttpResponse

from meetings.models import Meeting

def welcome(request):
    return render(request,"website/welcome.html",
                  {"num_meetings": Meeting.objects.count()})

def aboutme(request):
    return HttpResponse("Brandon Crenshaw")