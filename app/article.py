from django.shortcuts import render
from django.http import HttpResponseRedirect
from app import models

def add(request):
    if request.method == 'POST':
        title = request.POST.get("title")
        body = request.POST.get("body")
        models.Article.objects.create(title=title, body=body)
    article_list = models.Article.objects.all()
    return render(request, 'index.html', {'articles': article_list})


def delete(request):
    id = request.GET.get('id')
    models.Article.objects.filter(id=id).delete()
    return HttpResponseRedirect('/')


def update(request):
    if request.method == 'POST':
        id = request.POST.get('id')
        title = request.POST.get("title")
        body = request.POST.get("body")
        models.Article.objects.filter(id=id).update(title=title, body=body)
        return HttpResponseRedirect('/')
    else:
        id = request.GET.get('id')
        value = {}
        value['id'] = models.Article.objects.get(id=id).id
        value['title'] = models.Article.objects.get(id=id).title
        value['body'] = models.Article.objects.get(id=id).body
    return render(request, 'update.html', value)
