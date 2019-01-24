from django.conf.urls import url
from django.contrib.auth.forms import UserCreationForm
from . import views


app_name = 'accounts'

urlpatterns = [
    url(r'^signup$',views.signup_view, name='signup')
]