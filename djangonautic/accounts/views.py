from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm

# Create your views here.

def signup_view(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('article:list')
            # we can also use 'http://127.0.0.1:8000/articles/articles_list/ but no efficient
            # redirect take *url*
    else:
        form = UserCreationForm()
    return render(request,'accounts/signup.html',{'form':form})