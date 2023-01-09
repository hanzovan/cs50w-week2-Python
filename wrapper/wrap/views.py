from django.shortcuts import render
from django.http import HttpResponse
from functools import wraps


# Create your views here.
def announce(f):
    def wrapper(request, *args, **kwargs):
        print("prepare to run...")
        return f(request, *args, **kwargs)
    return wrapper


@announce
def index(request):
    return HttpResponse('Hello, this is wrapper 2')