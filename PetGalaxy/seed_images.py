import os
import django
import urllib.request
from django.core.files.base import ContentFile

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'petgalaxy.settings')
django.setup()

from store.models import Product

print("Starting to fetch and apply real images...")

products = Product.objects.all()
for p in products:
    if p.image and 'dog_food_bag' in p.image.name:
        continue # Skip the one we already created
    
    cat_name = p.category.name.lower()
    if 'dog' in cat_name:
        keywords = "dog"
    elif 'cat' in cat_name:
        keywords = "cat"
    elif 'rabbit' in cat_name:
        keywords = "rabbit"
    elif 'bird' in cat_name:
        keywords = "bird,parrot"
    elif 'fish' in cat_name:
        keywords = "aquarium,fish"
    else:
        keywords = "pet"
        
    url = f"https://loremflickr.com/600/600/{keywords}"
    try:
        print(f"Fetching image for {p.name} ({keywords})...")
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req, timeout=10) as response:
            if response.status == 200:
                filename = f"prod_{p.id}_{keywords}.jpg"
                p.image.save(filename, ContentFile(response.read()), save=True)
                print(f" -> Successfully saved image for {p.name}")
            else:
                print(f" -> Failed to fetch image for {p.name}")
    except Exception as e:
        print(f" -> Error processing {p.name}: {e}")

print("Done updating all products with real images!")
