from typing import Any
from django.forms.models import BaseModelForm
from django.shortcuts import render, redirect
from .models import UsersUrls
from .forms import UrlsAddForm
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib import messages
from django.contrib.auth.decorators import login_required

def home(request):
    return render(request, 'main/home.html')

def contacts(request):
    return render(request, 'main/contacts.html')

class UrlsAdd(LoginRequiredMixin, CreateView):
    model = UsersUrls
    form_class = UrlsAddForm
    template_name = 'main/urls-add.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        url_small = self.request.POST['url_small']

        if UsersUrls.objects.filter(user=self.request.user, url_small=url_small).exists():
            form.add_error('url_small', 'Ссылка с таким сокращением уже существует')
            return super(UrlsAdd, self).form_invalid(form)
        else:
            return super(UrlsAdd, self).form_valid(form)

    def get_context_data(self, **kwards):
        ctx = super(UrlsAdd, self).get_context_data(**kwards)

        ctx['links'] = self.model.objects.filter(user=self.request.user)
        ctx['title'] = 'Создание ссылок'
        ctx['btn_text'] = 'Создать ссылку'
        return ctx
