from django.shortcuts import render, get_object_or_404
from .models import Product, Brand
import random

def dashboard(request):
    products = list(Product.objects.select_related('brand').all())
    random.shuffle(products)

    brands = Brand.objects.all()
    selected_brand = request.GET.get('brand')
    selected_category = request.GET.get('category')
    query = request.GET.get('q')

    # Filter by category first (if selected)
    if selected_category:
        products = [p for p in products if p.category == selected_category]

    # Then filter by brand (if selected)
    if selected_brand:
        products = [p for p in products if p.brand.name.lower() == selected_brand.lower()]


    # Then filter by search query (if entered)
    if query:
        products = [p for p in products if query.lower() in p.name.lower()]

    context = {
        'products': products,
        'brands': brands,
        'selected_brand': selected_brand,
        'selected_category': selected_category,
        'query': query,
        'whatsapp_number': '6378381443',  # replace with your number
    }
    return render(request, 'dashboard.html', context)


def product_detail(request, id):
    product = get_object_or_404(Product, id=id)
    return render(request, 'product_detail.html', {'product': product})
