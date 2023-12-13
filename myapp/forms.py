from django import forms
from .models import Topic, Entry

class TopicForm(forms.ModelForm):
    class Meta:
        model = Topic
        fields = ['text']
        labels = {'text': ''}

class EntryForm(forms.ModelForm):
    class Meta:
        model = Entry
        fields = ['text'] # esse é campo que aparece pra preencher
        labels = {'text': ''}
        widgets = {'text': forms.Textarea(attrs={'cols':80})} # espaço para adicionar as anotações