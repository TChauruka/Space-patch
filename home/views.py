from django.shortcuts import render
from django.http import HttpResponseServerError

# Create your views here.

def index(request):
    '''' view to return index page '''
    return render (request, "home/index.html")


def handler404(request, exception):
    return render(request, '404.html', status=404)


def handler500(request):
    return render(request, '500.html', status=500)