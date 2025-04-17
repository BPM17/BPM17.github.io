from django.db import models

# Create your models here.

class Item(models.Model):
    Title = models.CharField( max_length=200)
    Image = models.ImageField()
    Description = models.TextField()
    Link = models.URLField(max_length=200)

    def __str__(self):
        return self.Title + ' - ' + self.Description
    
class EducationItem(models.Model):
    school = models.CharField(max_length=100)
    course = models.CharField(max_length=200, null = True, blank = True)
    image = models.ImageField(null = True, blank = True)
    description = models.TextField(null = True, blank = True)

    def __str__(self):
        return self.school + ' - ' + self.course
    
class ProjectItem(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField( null = True, blank = True)
    image = models.ImageField( null = True, blank = True)
    link = models.URLField(max_length=200, null = True, blank = True)

    def __str__(self):
        return self.title 

class ExperienceItem(models.Model):
    company = models.CharField(max_length=100)
    position = models.CharField(max_length=100, null = True, blank = True)
    timelaps = models.CharField(max_length=100, null = True, blank = True)
    description = models.TextField( null = True, blank = True)
    achivements = models.TextField( null = True, blank = True)

    def __str__(self):
        return self.company + ' - ' + self.position