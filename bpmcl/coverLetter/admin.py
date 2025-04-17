from django.contrib import admin
from .models import ProjectItem, EducationItem, ExperienceItem

# Register your models here.
admin.site.register(ProjectItem)
admin.site.register(ExperienceItem)
admin.site.register(EducationItem)