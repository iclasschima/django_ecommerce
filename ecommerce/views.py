from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.template import loader
from django.http import Http404

# Create your views here.
from .models import Product


def index(request):
    products = Product.objects.all()
    template = loader.get_template('index.html')

    context = {
        "products": products
    }
    return HttpResponse(template.render(context, request))


def detail(request, product_id):
    product = get_object_or_404(Product, pk=product_id)

    return render(request, 'detail.html', {'product': product})



    