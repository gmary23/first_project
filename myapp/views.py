from django.shortcuts import render
from .models import Topic, Entry
from .forms import TopicForm, EntryForm
from django.http import HttpResponseRedirect, Http404
from django.urls import reverse
# esse módulo dar permissão ao usuário apenas o que foi ele é dono
from django.contrib.auth.decorators import login_required


def index(request,):
    return render(request, 'myapp/index.html')

@login_required # noqa
def topics(request):
    #  tá pegando todos os objetos que tem como owner o usuário e só depois faz uma ordenação pela data # noqa: E501
    topics = Topic.objects.filter(owner=request.user).order_by('date_added') # noqa
    context = {'topics': topics}
    return render(request, 'myapp/topics.html', context)


@login_required
def topic(request, topic_id):
    topic = Topic.objects.get(id=topic_id)
   # noqa
    # Garante que o assunto pertence ao usuário atual
    if topic.owner!= request.user:  # noqa: E225
        raise Http404

    entries = topic.entry_set.order_by('-date_added')
    context = {'topic': topic, 'entries': entries}
    return render(request, 'myapp/topic.html', context)


@login_required
def new_topic(request):
    if request.method != 'POST':
        form = TopicForm() # Nenhum dado submetido cria um formulário em branco # noqa

    else:
        form = TopicForm(request.POST) # Dados POST submetidos - processa os dados # noqa: E501, E261
        if form.is_valid():
            new_topic = form.save(commit=False)
            new_topic.owner = request.user
            new_topic.save()
            return HttpResponseRedirect(reverse('topics')) # essa função reverse -> direciona para o name # noqa: E501, E261

    return render(request, 'myapp/new_topic.html', context={'form': form})

@login_required # noqa
def new_entry(request, topic_id):
    """Insere uma nova entrada para o assunto do topico"""
    topic = Topic.objects.get(id=topic_id)

    # Garante que o assunto pertence ao usuário atual
    if topic.owner!= request.user: # noqa
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
        # noqa

    return render(request, 'myapp/new_entry.html', context={'topic':topic, 'form':form}) # noqa

@login_required # noqa
def edit_entry(request, entry_id):
    entry = Entry.objects.get(id=entry_id)  # tá buscando na class Entry em models.py o id # noqa
    topic = entry.topic  #topic do model topic que está ligado por uma chave estrangeira # noqa

    if topic.owner!= request.user: # noqa
        raise Http404

    if request.method != 'POST': # noqa
        form = EntryForm(instance=entry) # busca o formulário já preenchido - a instance faz isso - a variável entry traz isso na linha 53 # noqa

    else:
        form = EntryForm(instance=entry, data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('topic', args=[topic.id]))
                                                           # noqa
    context={'entry': entry, 'topic': topic, 'form': form} # noqa
    return render(request, 'myapp/edit_entry.html', context)
  # noqa
