import requests
from .models import Product, Store, Price

def fetch_and_store_data(store):
    """Fetch product data from the store's API and save it in the database."""
    response = requests.get(store.api_url)
    if response.status_code == 200:
        data = response.json()
        for item in data.get('products', []):
            # Get or create the product
            product, created = Product.objects.get_or_create(
                name=item['name'],
                defaults={'category': item.get('category', ''), 'description': item.get('description', '')}
            )

            # Save price information
            Price.objects.create(
                product=product,
                store=store,
                price=item['price'],
                availability_date=item.get('availability_date'),
                location=item.get('location', 'Unknown')
            )
