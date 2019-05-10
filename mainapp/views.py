from django.shortcuts import render


def main(request):
    context = {'name': 'Мария', 'date':'25 апреля', }
    return render(request, 'mainapp/index.html', context)


def products(request):
    products = Product.objects.all()
    content = {'products': products}
    return render(request, 'mainapp/products.html', content)


def contacts (request):
    context = {'phone':"8291912920136362"}
    return render(request, 'mainapp/contacts.html', context)
# Create your views here.




