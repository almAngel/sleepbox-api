from django.http import HttpResponse
from django.views import API

def home(request):
    return HttpResponse('Hello, Django!')