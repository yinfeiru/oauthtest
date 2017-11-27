from django.shortcuts import render as django_render

def index(request):
    return django_render(
        request,
        'implicit.html'
    )
