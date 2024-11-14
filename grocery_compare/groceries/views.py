from django.shortcuts import render
from django.db.models import Q
from .models import Product, Price, UserPreference

# groceries/views.py
from django.shortcuts import render

def home(request):
    return render(request, "groceries/home.html")


def product_search(request):
    query = request.GET.get('query', '')
    max_price = request.GET.get('max_price')
    location = request.GET.get('location')
    time_filter = request.GET.get('time_filter')

    # Base query to filter products
    products = Product.objects.filter(name__icontains=query)

    # Filter prices based on max price, location, and time
    prices = Price.objects.filter(product__in=products)

    if max_price:
        prices = prices.filter(price__lte=max_price)
    if location:
        prices = prices.filter(location=location)
    if time_filter:
        # Apply time-based filtering logic, assuming time_filter is a datetime
        prices = prices.filter(availability_date__gte=time_filter)

    return render(request, 'groceries/product_search.html', {
        'query': query,
        'prices': prices,
    })

