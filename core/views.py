from django.shortcuts import render
from .forms import UniversityForm

def index(request):
    return render(request, 'index.html', {'form':UniversityForm()})
