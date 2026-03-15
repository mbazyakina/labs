from django.shortcuts import render


def home(request):
    return render(request, 'index.html', {})


def static_page(request):
    return render(request, 'static_handler.html', {})