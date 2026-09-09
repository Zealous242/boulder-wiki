from django.shortcuts import render


def suggestion_list(request):
    return render(request, 'suggestions/suggestion_list.html')
