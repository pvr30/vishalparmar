from django.shortcuts import render
from .models import *
# Create your views here.
def home(request):
    profile = Profile.objects.get(id=1)
    return render(request, 'main/home.html', {'profile': profile})

def skills(request):
    skills = Skill.objects.all()
    return render(request, 'main/skills.html', {'skills': skills})

def projects(request):
    projects = Project.objects.all()
    return render(request, 'main/projects.html', {'projects': projects})