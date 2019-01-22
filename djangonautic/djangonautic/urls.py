from django.contrib import admin
from django.urls import path,include
from django.conf.urls import url,include
from django.contrib.staticfiles.urls import staticfiles_urlpatterns 
from . import views

urlpatterns = [
    url(r'^$',views.homepage),
    url(r'articles/',include('articles.urls')),
    url(r'admin/', admin.site.urls),
    url(r'about/',views.about)
]
