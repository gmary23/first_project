from django.shortcuts import render
from . models import Topic


def index(request,):
    return render(request, 'myapp/index.html')

def topics(request):
    topics = Topic.objects.order_by('date_added')
    context = {'topics': topics}
    return render(request, 'myapp/topics.html', context)