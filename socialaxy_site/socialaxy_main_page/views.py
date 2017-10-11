from django.shortcuts import render


def main_page(request):
    return render(request, 'socialaxy_main_page/index.html', {})
