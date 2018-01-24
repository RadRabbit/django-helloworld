from django.shortcuts import render
from app import models
# Create your views here.
# def index(request):
#     if request.method =='POST':
#         title = request.POST.get("title")
#         body = request.POST.get("body")
#         models.Article.objects.create(title=title,body=body)
#     article_list= models.Article.objects.all()
#     return render(request, 'index.html',{'articles':article_list})