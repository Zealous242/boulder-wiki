from django.shortcuts import render


def home(request):
    return render(request, 'articles/home.html')


def categories(request):
    return render(request, 'articles/categories.html')


def search(request):
    return render(request, 'articles/search.html')
