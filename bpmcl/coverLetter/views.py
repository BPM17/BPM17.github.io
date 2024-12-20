from django.shortcuts import render
from django.http import HttpResponse
# from .models import item

# Create your views here.
def index(request):
    # dbitems = item.objects.all()
    # context = {'dbitems':dbitems}
    return render(request, 'index.html')