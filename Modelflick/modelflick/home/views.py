from django.shortcuts import render
from django.http import HttpResponse
from .forms import serviceform




# Create your views here.
def pointer(request):
    return render(request,'pointer.html')

def home(request):
    return render(request,'home.html')

def about(request):
    return render(request,'about.html')

def service(request):
    form = serviceform()
    dict_form = {
        'form': form
    }
    return render(request,'service.html', dict_form)

from django.shortcuts import render, redirect
from .forms import serviceform
from .models import services

def my_view(request):
    if request.method == 'POST':
        form = serviceform(request.POST)
        if form.is_valid():
            # Save the form data to the database
            form.save()
            return render(request, 'result.html')
    form = serviceform()
    dict_form={
        'form': form
    }
    return render(request, 'service.html',dict_form)

from django.shortcuts import render
from .models import services

def result(request):
    servicess= services.objects.all()
    return render(request,'result.html', {'servicess': servicess})