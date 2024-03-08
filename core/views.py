from django.shortcuts import render
from .forms import UniversityForm
from django.http import HttpResponse
from django.template.context_processors import csrf
from crispy_forms.utils import render_crispy_form
from django.contrib.auth import login
from crispy_forms.templatetags.crispy_forms_filters import as_crispy_field

def index(request):
    form = UniversityForm(request.POST or None)
    #if request.method == 'GET':
    #    return render(request, 'index.html', {'form':form})

    if request.method == 'POST':
        if form.is_valid():
            user = form.save()
            login(request, user)
            template = render(request, 'profile.html')
            template['hx-Push'] = '/Profile/'
            return template
        ctx = {}
        ctx.update(csrf(request))
        form_html = render_crispy_form(form, context=ctx) 
        return HttpResponse(form_html)  
    return render(request, 'index.html', {'form':form})    

def check_username(request):
    form = UniversityForm(request.GET)
    context={
        'field':as_crispy_field(form['username']),
        'valid':not form['username'].errors,
    }
    return render(request, 'partials/field.html', context)

def check_subject(request):
    form = UniversityForm(request.GET)
    context={
        'field':as_crispy_field(form['subject']),
        'valid':not form['subject'].errors,
    }
    return render(request, 'partials/field.html', context)

def check_dob(request):
    form = UniversityForm(request.GET)
    context={
        'field':as_crispy_field(form['dob']),
        'valid':not form['dob'].errors,
    }
    return render(request, 'partials/field.html', context)
