"""
Definition of views.
"""

from datetime import datetime
from django.shortcuts import render
from django.http import HttpRequest

def inicio(request):
    """INICIO."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/index.html',
        {
            'title':'Inicio',
            'year':datetime.now().year,
        }
    )

def ropa(request):
    """ROPA."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/ropa.html',
        {
            'title':'Ropa',
            'message':'Productos disponibles',
            'year':datetime.now().now
        }
    )

def juguetes(request):
    """JUGUETES."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/juguetes.html',
        {
            'title':'Juguetes',
            'message':'Productos disponibles',
            'year':datetime.now().year,
        }
    )
