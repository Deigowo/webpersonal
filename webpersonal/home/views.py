from django.shortcuts import render
from django.http import HttpResponse

from .models import Project

# Create your views here.
def home (request):
    name = 'Diego Nicolás'
    career = 'Backend Developer'
    context = {
        "name": name,
        "career": career
    }
    return render(request, 'home/index.html', context)

def contact(request):
    return render(request, 'home/contact.html')

def projects(request):
    projects = Project.objects.all().order_by('id') [:5]
    context = {
        "projects": projects
    }
    return render(request, 'home/projects.html', context)

def about(request):
    name = 'Diego Nicolás'
    description = 'Lorem ipsum dolor sit, amet consectetur adipisicing elit. Deserunt impedit ea iure reiciendis beatae, vitae est dignissimos accusamus iste tempora laboriosam cupiditate eos perspiciatis? Veritatis deserunt quaerat veniam quae nesciunt?'
    context = {
        "name": name,
        "description": description
    }
    return render(request, 'home/about.html', context)
