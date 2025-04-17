from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, JsonResponse
from .models import EducationItem, ProjectItem, ExperienceItem

# Create your views here.
def index(request):
    experience = ExperienceItem.objects.all()
    projects = ProjectItem.objects.all()
    education = EducationItem.objects.all()
    return render(request, 'index.html',{
        'experience' : experience
    })