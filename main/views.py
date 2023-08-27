from django.shortcuts import render
from .models import Project

def index(request):
    projects = Project.objects.all()
    return render(request, 'index.html', {'projects':projects})

def about(request):
    return render(request, 'about.html')

def projects(request):
    return render(request, 'projects.html')

def contact(request):
    return render(request, 'contact.html')
