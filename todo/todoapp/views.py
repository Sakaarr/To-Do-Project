from django.shortcuts import render
from .forms import Form
# Create your views here.
def addanddisplay(request):
    if request.method=="POST":
        fm=Form(request.POST)
        if fm.is_valid():
            fm.save()
            fm=Form()
    else:
        fm=Form()        
    return render(request , 'todoapp/addanddisplay.html' , {'forms':fm})