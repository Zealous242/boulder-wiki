from django.shortcuts import render

from .models import Article, Category


def home(request):
    categories = Category.objects.all()
    latest_articles = Article.objects.order_by('-created_at')[:3]
    return render(request, 'articles/home.html', {
        'categories': categories,
        'latest_articles': latest_articles,
    })


def article_list(request):
    articles = Article.objects.select_related('category').order_by('-created_at')
    return render(request, 'articles/article_list.html', {
        'articles': articles,
    })


def categories(request):
    return render(request, 'articles/categories.html')


def search(request):
    return render(request, 'articles/search.html')
