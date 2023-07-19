from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
# request handler

def alive(request):
    return HttpResponse("Server is ready ....")

def tagh1(request):
    return render(request, "hello.html", {"name":"Yash Khatri"})