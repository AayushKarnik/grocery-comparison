from django.shortcuts import render
from django.db.models import Q
from .models import Product, Price, UserPreference

# groceries/views.py
from django.shortcuts import render
from django.shortcuts import get_object_or_404, redirect
from .models import Product, Review

def submit_review(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    if request.method == 'POST':
        rating = request.POST['rating']
        comment = request.POST['comment']
        Review.objects.create(product=product, rating=rating, comment=comment)
    return redirect('product_detail', product_id=product.id)

from django.core.paginator import Paginator


def product_search(request):
    query = request.GET.get('query', '')
    max_price = request.GET.get('max_price')
    location = request.GET.get('location')
    time_filter = request.GET.get('time_filter')

    products = Product.objects.filter(name__icontains=query)
    prices = Price.objects.filter(product__in=products)

    if max_price:
        prices = prices.filter(price__lte=max_price)
    if location:
        prices = prices.filter(location=location)
    if time_filter:
        prices = prices.filter(availability_date__gte=time_filter)

    paginator = Paginator(prices, 10)  # Show 10 items per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'groceries/product_search.html', {'page_obj': page_obj, 'query': query})


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

