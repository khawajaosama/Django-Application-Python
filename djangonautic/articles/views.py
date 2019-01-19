from django.shortcuts import render
from .models import Article
from django.http import HttpResponse


def article_list(request):
    #return HttpResponse('about')
    return render(request,'articles/article_list.html')

# def homepage(request):
#     #return HttpResponse('This is Homepage')
#     return render(request,'homepage.html')