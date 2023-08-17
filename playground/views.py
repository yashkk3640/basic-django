from django.shortcuts import render
from django.http import HttpResponse
from .models import Team
# Create your views here.
# request handler

def alive(request):
    return HttpResponse("Server is ready ....")

def tagh1(request,**arg):
    print(request,arg)
    return render(request, "hello.html", {"name":"Yash Khatri"})


def get_team(request):
    data = Team.objects.all().values() or [('test','test')]
    print(data)
    return HttpResponse(data,"application/json")

def createTeam(request):
    print(request)
    return HttpResponse('Post request')