from django.shortcuts import render, redirect
from django.contrib import messages
from models import *
# Create your views here.
def index(request):
    context = {'courses': Course.objects.all()}
    return render(request, 'courses/index.html', context)

def create(request):
    if request.method == "POST":
        errors = Course.objects.basic_validator(request.POST)
        if len(errors):
            for tag, error in errors.iteritems():
                messages.error(request, error, extra_tags=tag)
        else:
            name = request.POST['name']
            desc = request.POST['desc']
            Course.objects.create(name=name, desc=desc)
        return redirect("/") 

def destroy(request, id):
    context = {'course': Course.objects.get(id=id)}
    return render(request, 'courses/destroy.html', context)

def delete(request):
    id = request.POST['id']
    u = Course.objects.get(id=id)
    u.delete()
    return redirect('/')
