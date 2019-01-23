from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from . import views

app_name = 'articles'  # we are name spacing this file

urlpatterns = [
    url(r'^articles_list/',views.article_list,name='list'),
    url(r'^slug:(?P<slug>[\w-]+)/$',views.article_detail,name='detail'),
    url(r'^find:(?P<slug>[\w-]+)/$',views.article_full_detail,name='detail')
    # path(r'^admin/', admin.site.urls),
    # path(r'about/',views.about),
    #path('^$',views.about)
]
