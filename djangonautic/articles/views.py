from django.shortcuts import render
from .models import Article
from django.http import HttpResponse
from .models import Article


def article_list(request):
    articles = Article.objects.all().order_by('date')
    #return HttpResponse('about')
    return render(request,'articles/article_list.html',{'articles':articles})

# def homepage(request):
#     #return HttpResponse('This is Homepage')
#     return render(request,'homepage.html')
def article_detail(request,slug):
    return render(request,'articles/url_params.html',{'params':slug})