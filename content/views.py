from django.shortcuts import render
from .models import Project

# Add the project 

# List the projects
def projects_list_view(request):

    # Request the objects (Projects) of the DB
    project_list = Project.objects.all()

    # Pass the object list as the context
    return render(request, "content/projects_list.html", {"project_list": project_list})


def experience_list_view(request):
    return render(request, "content/experiences_list.html")

# Add an experience

# List the experience
