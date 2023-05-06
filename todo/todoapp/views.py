from django.shortcuts import render
from .forms import Form
from .models import User
from django.http import HttpResponseRedirect
# Create your views here.
def addanddisplay(request):
    if request.method=="POST":
        fm=Form(request.POST)
        if fm.is_valid():
            fm.save()
            fm=Form()
    else:
        fm=Form()   
    info = User.objects.all()     
    return render(request , 'todoapp/addanddisplay.html' , {'forms':fm,'info':info})
def delete_data(request , id):
    if request.method=="POST":
        pi = User.objects.get(pk=id)
        pi.delete()
        return HttpResponseRedirect('/')
def update_data(request , id):
    if request.method=="POST":
        pi = User.objects.get(pk=id)
        fm = Form(request.POST , instance= pi)
        if fm.is_valid:
            fm.save()
    else:
        if request.method=="GET":
            pi = User.objects.get(pk=id)
            fm = Form(instance=pi)
    return render(request , 'todoapp/update.html', {'forma':fm})
