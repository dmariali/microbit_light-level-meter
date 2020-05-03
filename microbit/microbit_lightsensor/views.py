
from django.template import Template, Context
from django.shortcuts import render
# Create your views here.

def home(request):
    temp = 20
    context = {'temps': temp}
    return render(request, 'index.html', context)

