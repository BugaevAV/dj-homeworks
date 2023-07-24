from django.shortcuts import render, redirect
from phones.models import Phone


def index(request):
    return redirect('catalog')


def show_catalog(request):
    sort = request.GET.get('sort')
    if sort == 'name':
        phones_obj = Phone.objects.order_by('name')
    elif sort == 'min_price':
        phones_obj = Phone.objects.order_by('price')
    elif sort == 'max_price':
        phones_obj = Phone.objects.order_by('price').reverse()
    else:
        phones_obj = Phone.objects.all()
    template = 'catalog.html'
    context = {'phones': phones_obj}
    return render(request, template, context)


def show_product(request, slug):
    phone_obj = Phone.objects.filter(slug=slug).first()
    template = 'product.html'
    context = {'phone': phone_obj}
    return render(request, template, context)
