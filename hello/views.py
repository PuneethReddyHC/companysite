"""
Definition of views.
"""
from django.views import generic
from django.shortcuts import render
from django.http import HttpRequest
from django.template import RequestContext
from datetime import datetime
import hello.forms
def home(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'index.html',
        {
            'title':'Home Page',
            'year':datetime.now().year,
        }
    )

def contact(request):
    """Renders the contact page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'contact.html',
        {
            'title':'Contact',
            'message':'Your contact page.',
            'year':datetime.now().year,
        }
    )

def about(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'about.html',
        {
            'title':'About',
            'message':'Your application description page.',
            'year':datetime.now().year,
        }
    )
def services(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'services.html',
        {
            'title':'services',
            'message':'Your application services page.',
            'year':datetime.now().year,
        }
    )

def portfolio(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'portfolio.html',
        {
            'title':'portfolio',
            'message':'Your application portfolio page.',
            'year':datetime.now().year,
        }
    )

    