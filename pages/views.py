from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("Hello, Django Web Framework")


def about(request):
    return HttpResponse('about Page')

def contact(request):
    return HttpResponse('Contact Page')

def persons(request):
    return HttpResponse('Persons Page')