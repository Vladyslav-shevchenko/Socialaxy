from django.shortcuts import render


def coming_soon_page(request):
    return render(request, 'socialaxy_coming_soon_page/index.html', {})
