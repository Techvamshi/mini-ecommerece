from django.db import migrations

PRODUCTS = [
    ("Fresh Fruits", "Fresh", "120.00", "fresh_fruits.jpg"),
    ("Green Smoothie", "Fresh", "150.00", "green_smoothie.jpg"),
    ("Mixed Nuts", "Snacks", "250.00", "mixed_nuts.jpg"),
    ("Oats Bowl", "Breakfast", "180.00", "oats_bowl.jpg"),
    ("Quinoa Salad", "Meals", "220.00", "quinoa_salad.jpg"),
    ("Wheat Bread", "Breakfast", "60.00", "wheat_bread.jpg"),
]


def seed(apps, schema_editor):
    Product = apps.get_model("shop", "Product")
    for name, category, price, image in PRODUCTS:
        Product.objects.get_or_create(name=name, defaults={"category": category, "price": price, "image": image})


class Migration(migrations.Migration):
    dependencies = [("shop", "0001_initial")]
    operations = [migrations.RunPython(seed, migrations.RunPython.noop)]
