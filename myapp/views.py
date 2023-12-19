from django.shortcuts import render
from .models import Topic, Entry
from .forms import TopicForm, EntryForm
from django.http import HttpResponseRedirect, Http404
from django.urls import reverse
# esse módulo dar permissão ao usuário apenas o que foi ele é dono
from django.contrib.auth.decorators import login_required


def index(request,):
    return render(request, 'myapp/index.html')

@login_required
def topics(request):
    topics = Topic.objects.filter(owner=request.user).order_by('date_added') # tá pegando todos os objetos que tem como owner o usuário e só depois faz uma ordenação pela data
    context = {'topics': topics}
    return render(request, 'myapp/topics.html', context)


@login_required
def topic(request, topic_id):
    topic = Topic.objects.get(id=topic_id)
   
    # Garante que o assunto pertence ao usuário atual
    if topic.owner!= request.user:
        raise Http404

    entries = topic.entry_set.order_by('-id')
    context = {'topic': topic, 'entries': entries}
    return render(request, 'myapp/topic.html', context)

@login_required
def new_topic(request):
    if request.method != 'POST':
        form = TopicForm() # Nenhum dado submetido cria um formulário em branco
    else:
        form = TopicForm(request.POST) # Dados POST submetidos - processa os dados
        if form.is_valid():
            new_topic = form.save(commit=False)
            new_topic.owner = request.user
            new_topic.save()
            return HttpResponseRedirect(reverse('topics')) # essa função reverse -> direciona para o name

    return render(request, 'myapp/new_topic.html', context={'form': form})

@login_required
def new_entry(request, topic_id):
    """Insere uma nova entrada para o assunto do topico"""
    topic = Topic.objects.get(id=topic_id)

    # Garante que o assunto pertence ao usuário atual
    if topic.owner!= request.user:
        raise Http404

    if request.method != 'POST':
        form = EntryForm()

    else:
        form = EntryForm(data=request.POST)
        if form.is_valid():
            new_entry = form.save(commit=False)
            new_entry.topic = topic
            new_entry.save()
            return HttpResponseRedirect(reverse('topic', args=[topic_id]))
        

    return render(request, 'myapp/new_entry.html', context={'topic':topic, 'form':form})

@login_required
def edit_entry(request, entry_id):
    entry = Entry.objects.get(id=entry_id)  # tá buscando na class Entry em models.py o id 
    topic = entry.topic  #topic do model topic que está ligado por uma chave estrangeira

    if topic.owner!= request.user:
        raise Http404

    if request.method != 'POST': 
        form = EntryForm(instance=entry) # busca o formulário já preenchido - a instance faz isso - a variável entry traz isso na linha 53

    else:
        form = EntryForm(instance=entry, data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('topic', args=[topic.id]))
      
    context={'entry': entry, 'topic': topic, 'form': form}
    return render(request, 'myapp/edit_entry.html', context)

