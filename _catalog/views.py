from django.shortcuts import render
from .models import Country


def countries(request):
    countries_list = Country.objects.all()
    context = {'countries': countries_list, }
    return render(request, 'catalog/countries.html', context)


def index(request):
    return render(request, 'catalog/index.html')


def contact(request):
    return render(request, 'catalog/contact.html')


def blog(request):
    return render(request, 'catalog/blog.html')


def about(request):
    return render(request, 'catalog/about.html')