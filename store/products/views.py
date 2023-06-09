from django.shortcuts import render

def index(request):
    context = {'title': 'Store'}
    return render(request, 'products/index.html', context)

def products(request):
    return render(request, template_name='products/products.html')
