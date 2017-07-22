from django.shortcuts import render

from demo.forms import VideoForm

def index(request):
    form = VideoForm()
    return render(request, 'demo/index.html', {'form': form})
