from django.shortcuts import render


def main(request):
    context = {'name': 'Мария', 'date':'25 апреля', }
    return render(request, 'mainapp/index.html', context)


def products(request):
    context = {'products':'100'}
    return render(request, 'mainapp/products.html', context)


def contacts (request):
    context = {'phone':"8291912920136362"}
    return render(request, 'mainapp/contacts.html', context)
# Create your views here.

from .models import ProductCategory, Product


def main(request):
    title = 'Главная'

    products = Product.objects.all()[:4]

    content = {'title': title, 'products': products}
    return render(request, 'mainapp/index.html', content)