from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    print(f'request: {request}')

    return HttpResponse('News page')

