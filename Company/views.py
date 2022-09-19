from django.shortcuts import render
from .company import get_service, get_quote, get_faq, get_fact

def index(request):
    context = {
        'services': get_service(),
        'quote': get_quote(),
        'fact': get_fact(),
        'faq': get_faq(),
    }
    return render(request, 'index.html', context)
