# from django.http import HttpResponse
# def homepage(request):
#  return (HttpResponse("Hello World!"))

from django.shortcuts import render
def homepage(request):
 return render(request, 'home.html')