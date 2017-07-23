from django.shortcuts import render

from demo.forms import VideoForm

def index(request):
    print('boo')
    return render(request, 'demo/index.html')
