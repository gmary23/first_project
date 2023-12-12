from django.shortcuts import render
from .models import Topic
from .forms import TopicForm
from django.http import HttpResponseRedirect
from django.urls import reverse


def index(request,):
    return render(request, 'myapp/index.html')

def topics(request):
    topics = Topic.objects.order_by('date_added')
    context = {'topics': topics}
    return render(request, 'myapp/topics.html', context)

def topic(request, topic_id):
    topic = Topic.objects.get(id=topic_id)
    entries = topic.entry_set.order_by('id')
    context = {'topic': topic, 'entries': entries}
    return render(request, 'myapp/topic.html', context)


def new_topic(request):
    if request.method != 'POST':
        form = TopicForm() # Nenhum dado submetido cria um formulário em branco
    else:
        form = TopicForm(request.POST) # Dados POST submetidos - processa os dados
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse(topics)) # essa função reverse -> direciona para o name

    return render(request, 'myapp/new_topic.html', context={'form': form})


