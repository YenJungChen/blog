# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, get_object_or_404, redirect
from article.models import Article
from django.http import HttpResponse
from django import forms
from article.forms import PostForm
from django.utils import timezone


def home(request):
    article = Article.objects.all()
    return render(request, "home.html", {'article': article})

def detail(request, pk):
	article = get_object_or_404(Article, pk=int(pk))
	return render(request, "detail.html", {'article': article})

def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'post_edit.html', {'form': form})