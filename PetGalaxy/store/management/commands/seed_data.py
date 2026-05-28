from django.core.management.base import BaseCommand
from store.models import Category, Product
from django.utils.text import slugify

class Command(BaseCommand):
    help = 'Seeds the database with 5 categories and 35 products with real images.'

    def handle(self, *args, **kwargs):
        self.stdout.write('Seeding database...')

        categories_data = ['Dogs', 'Cats', 'Rabbits', 'Birds', 'Fish']
        category_objects = {}

        for cat_name in categories_data:
            cat, created = Category.objects.get_or_create(
                name=cat_name,
                defaults={'slug': slugify(cat_name)}
            )
            category_objects[cat_name] = cat
            if created:
                self.stdout.write(f'Created category: {cat_name}')

        products_data = {
            'Dogs': [
                {
                    'name': 'Premium Dog Food (5 kg)',
                    'price': '1299.00',
                    'desc': 'High-quality dog food for adult dogs with balanced nutrition.',
                    'img': 'https://images.unsplash.com/photo-1568640347023-a616a30bc3bd?w=600&q=80',
                },
                {
                    'name': 'Adjustable Dog Leash',
                    'price': '399.00',
                    'desc': 'Durable and adjustable dog leash for comfortable walks.',
                    'img': 'https://images.unsplash.com/photo-1601758124510-52d02ddb7cbd?w=600&q=80',
                },
                {
                    'name': 'Leather Dog Collar',
                    'price': '499.00',
                    'desc': 'Stylish and sturdy leather collar with a soft inner lining.',
                    'img': 'https://images.unsplash.com/photo-1583337130417-3346a1be7dee?w=600&q=80',
                },
                {
                    'name': 'Orthopedic Dog Bed',
                    'price': '2499.00',
                    'desc': 'Comfortable orthopedic bed for ultimate rest and joint support.',
                    'img': 'https://images.unsplash.com/photo-1587300003388-59208cc962cb?w=600&q=80',
                },
                {
                    'name': 'Rubber Chew Toy',
                    'price': '249.00',
                    'desc': 'Tough rubber chew toy for active dogs.',
                    'img': 'https://images.unsplash.com/photo-1546975490-e8b92a360b24?w=600&q=80',
                },
                {
                    'name': 'Dog Grooming Shampoo',
                    'price': '349.00',
                    'desc': 'Gentle shampoo for a shiny and clean coat.',
                    'img': 'https://images.unsplash.com/photo-1583511655826-05700d52f4d9?w=600&q=80',
                },
                {
                    'name': 'Stainless Steel Food Bowl',
                    'price': '299.00',
                    'desc': 'Rust-resistant stainless steel bowl for food or water.',
                    'img': 'https://images.unsplash.com/photo-1625316708582-7c38734be31d?w=600&q=80',
                },
            ],
            'Cats': [
                {
                    'name': 'Premium Cat Food (3 kg)',
                    'price': '999.00',
                    'desc': 'Nutritious cat food specially formulated for adult cats.',
                    'img': 'https://images.unsplash.com/photo-1589924691995-400dc9ecc119?w=600&q=80',
                },
                {
                    'name': 'Clumping Cat Litter (10 kg)',
                    'price': '699.00',
                    'desc': 'High-absorbency clumping cat litter with odor control.',
                    'img': 'https://images.unsplash.com/photo-1535268647677-300dbf3d78d1?w=600&q=80',
                },
                {
                    'name': 'Cat Scratching Post',
                    'price': '1499.00',
                    'desc': 'Durable scratching post to keep claws healthy.',
                    'img': 'https://images.unsplash.com/photo-1514888286974-6c03e2ca1dba?w=600&q=80',
                },
                {
                    'name': 'Interactive Cat Toy Set',
                    'price': '499.00',
                    'desc': 'Fun interactive toy set including feathers and balls.',
                    'img': 'https://images.unsplash.com/photo-1574144611937-0df059b5ef3e?w=600&q=80',
                },
                {
                    'name': 'Cozy Cat Bed',
                    'price': '1199.00',
                    'desc': 'Warm and soft bed for your cat to curl up in.',
                    'img': 'https://images.unsplash.com/photo-1608848461950-0fe51dfc41cb?w=600&q=80',
                },
                {
                    'name': 'Litter Box with Scoop',
                    'price': '899.00',
                    'desc': 'Spacious litter box with an included scoop.',
                    'img': 'https://images.unsplash.com/photo-1561948955-570b270e7c36?w=600&q=80',
                },
                {
                    'name': 'Cat Grooming Brush',
                    'price': '199.00',
                    'desc': 'Gentle brush to remove loose hair and tangles.',
                    'img': 'https://images.unsplash.com/photo-1526336024174-e58f5cdd8e13?w=600&q=80',
                },
            ],
            'Rabbits': [
                {
                    'name': 'Rabbit Pellet Food',
                    'price': '450.00',
                    'desc': 'Nutritionally balanced pellet food for rabbits.',
                    'img': 'https://images.unsplash.com/photo-1585110396000-c9ffd4e4b308?w=600&q=80',
                },
                {
                    'name': 'Timothy Hay Bundle',
                    'price': '350.00',
                    'desc': 'Fresh Timothy hay for digestion and dental health.',
                    'img': 'https://images.unsplash.com/photo-1535241749838-299277b6305f?w=600&q=80',
                },
                {
                    'name': 'Rabbit Hutch',
                    'price': '3500.00',
                    'desc': 'Spacious wooden hutch for indoor or outdoor use.',
                    'img': 'https://images.unsplash.com/photo-1552053831-71594a27632d?w=600&q=80',
                },
                {
                    'name': 'Water Bottle Feeder',
                    'price': '150.00',
                    'desc': 'Drip-proof water bottle for cages.',
                    'img': 'https://images.unsplash.com/photo-1617077644557-63efe13cb64c?w=600&q=80',
                },
                {
                    'name': 'Chew Sticks',
                    'price': '120.00',
                    'desc': 'Apple wood chew sticks to keep teeth trim.',
                    'img': 'https://images.unsplash.com/photo-1533929736458-ca588d08c8be?w=600&q=80',
                },
                {
                    'name': 'Rabbit Bedding',
                    'price': '250.00',
                    'desc': 'Absorbent and odor-controlling paper bedding.',
                    'img': 'https://images.unsplash.com/photo-1518020382113-a7e8fc38eac9?w=600&q=80',
                },
                {
                    'name': 'Rabbit Grooming Brush',
                    'price': '180.00',
                    'desc': 'Soft brush suitable for rabbit coats.',
                    'img': 'https://images.unsplash.com/photo-1504006833117-8886a355efbf?w=600&q=80',
                },
            ],
            'Birds': [
                {
                    'name': 'Bird Seed Mix',
                    'price': '250.00',
                    'desc': 'Nutritious seed mix for small to medium birds.',
                    'img': 'https://images.unsplash.com/photo-1444464666168-49d633b86797?w=600&q=80',
                },
                {
                    'name': 'Bird Cage with Perches',
                    'price': '2100.00',
                    'desc': 'Sturdy bird cage featuring multiple perches.',
                    'img': 'https://images.unsplash.com/photo-1520038410233-7141be7e6f97?w=600&q=80',
                },
                {
                    'name': 'Cuttlefish Bone',
                    'price': '80.00',
                    'desc': 'Natural cuttlebone for calcium and beak health.',
                    'img': 'https://images.unsplash.com/photo-1552728089-57bdde30beb3?w=600&q=80',
                },
                {
                    'name': 'Bird Swing Toy',
                    'price': '150.00',
                    'desc': 'Colorful wooden swing toy for entertainment.',
                    'img': 'https://images.unsplash.com/photo-1508921912186-1d1a45ebb3c1?w=600&q=80',
                },
                {
                    'name': 'Water Dispenser',
                    'price': '120.00',
                    'desc': 'Easy-to-fill water dispenser for cages.',
                    'img': 'https://images.unsplash.com/photo-1522926193341-e9ffd686c60f?w=600&q=80',
                },
                {
                    'name': 'Millet Spray Treat',
                    'price': '180.00',
                    'desc': 'Healthy and tasty millet spray treat.',
                    'img': 'https://images.unsplash.com/photo-1597058712635-3182d1eabc17?w=600&q=80',
                },
                {
                    'name': 'Cage Cleaning Spray',
                    'price': '299.00',
                    'desc': 'Pet-safe spray for easy cage cleaning.',
                    'img': 'https://images.unsplash.com/photo-1553284965-83fd3e82fa5a?w=600&q=80',
                },
            ],
            'Fish': [
                {
                    'name': 'Tropical Fish Food',
                    'price': '220.00',
                    'desc': 'Flake food formulated for tropical aquarium fish.',
                    'img': 'https://images.unsplash.com/photo-1522069169874-c58ec4b76be5?w=600&q=80',
                },
                {
                    'name': 'Aquarium Tank (20 L)',
                    'price': '1800.00',
                    'desc': 'Clear glass aquarium suitable for small fish.',
                    'img': 'https://images.unsplash.com/photo-1534043464124-3be32fe000c9?w=600&q=80',
                },
                {
                    'name': 'Aquarium Water Filter',
                    'price': '650.00',
                    'desc': 'Efficient internal filter for clean water.',
                    'img': 'https://images.unsplash.com/photo-1544551763-46a013bb70d5?w=600&q=80',
                },
                {
                    'name': 'Air Pump',
                    'price': '450.00',
                    'desc': 'Quiet air pump to oxygenate the water.',
                    'img': 'https://images.unsplash.com/photo-1524704654690-b56c05c78a00?w=600&q=80',
                },
                {
                    'name': 'Decorative Gravel',
                    'price': '200.00',
                    'desc': 'Colorful non-toxic gravel for the tank bottom.',
                    'img': 'https://images.unsplash.com/photo-1535591273668-578e31182c4f?w=600&q=80',
                },
                {
                    'name': 'LED Aquarium Light',
                    'price': '750.00',
                    'desc': 'Bright LED light to enhance fish colors.',
                    'img': 'https://images.unsplash.com/photo-1583212292454-1fe6229603b7?w=600&q=80',
                },
                {
                    'name': 'Water Conditioner',
                    'price': '150.00',
                    'desc': 'Makes tap water safe for fish instantly.',
                    'img': 'https://images.unsplash.com/photo-1565039190189-92a1cd65e99e?w=600&q=80',
                },
            ],
        }

        for cat_name, products in products_data.items():
            category = category_objects[cat_name]
            for prod in products:
                product, created = Product.objects.get_or_create(
                    name=prod['name'],
                    category=category,
                    defaults={
                        'description': prod['desc'],
                        'price': prod['price'],
                        'stock': 50,
                        'image_url': prod['img'],
                    }
                )
                if not created:
                    # Update image_url even for existing products
                    product.image_url = prod['img']
                    product.description = prod['desc']
                    product.price = prod['price']
                    product.save()
                    self.stdout.write(f"Updated product: {prod['name']}")
                else:
                    self.stdout.write(f"Created product: {prod['name']}")

        self.stdout.write(self.style.SUCCESS('Successfully seeded database with images!'))
