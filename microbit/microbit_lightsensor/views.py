
from django.template import Template, Context
from django.shortcuts import render
from . import readserial

# Create your views here.

def home(request):
    temp = 20
    context = readserial.updateContext()
    return render(request, 'index.html', context)

