from django.shortcuts import render
from app.forms import *
# Create your views here.

def user_def_vali(request):
    nfo=NameForm()
    d={'form':nfo}
    return render(request,'user_def_vali.html',d)