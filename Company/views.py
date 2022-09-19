from django.shortcuts import render
from .company import get_service

def index(request):
    context = {
        'services': get_service(),
    }
    return render(request, 'index.html', context)
