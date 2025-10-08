from django.shortcuts import render 
from .models import Project

# Create your views here.
def projects(request):
    projects = Project.objects.all()
    return render(request, 'Projects/projects.html', {'projects': projects})

def project_detail(request, project_id):
    project = Project.objects.get(id=project_id)
    return render(request, 'Projects/project_detail.html', {'project': project})

