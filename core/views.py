from django.shortcuts import render
from .forms import UniversityForm
from django.http import HttpResponse

def index(request):
    form = UniversityForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            user = form.save()
            return HttpResponse('hi')            
    return render(request, 'index.html', {'form':form})
