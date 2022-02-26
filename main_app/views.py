from django.shortcuts import render
from .models import Widget
from django.views.generic import CreateView, UpdateView, DeleteView
from django.http import HttpResponseRedirect
from django.contrib.auth.mixins import LoginRequiredMixin


def home(request):
  return render(request, 'index.html')

def widget_index(request):
  widget = Widget.objects.all()
  return render(request, 'widget/index.html', { 'widget': widget })


class PostCreate(CreateView):
    model = Widget
    fields = '__all__'
    success_url = '/posts/'

class PostUpdate(LoginRequiredMixin,UpdateView):
    model = Widget
    fields = ['text']
    success_url = '/'

class PostDelete(LoginRequiredMixin,DeleteView):
    model = Widget
    success_url = '/'


def widget_index(request):
  widget = Widget.objects.all()
  return render(request, 'widget/index.html', { 'widget': widget })