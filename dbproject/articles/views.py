from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def testView (request):
  
    return HttpResponse("Hello TestView working")
