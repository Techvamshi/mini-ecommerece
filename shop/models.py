from django.db import models
from django.templatetags.static import static


class Product(models.Model):
    name = models.CharField(max_length=150)
    category = models.CharField(max_length=80)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    # File name inside shop/static/shop/images/, e.g. "fresh_fruits.jpg"
    image = models.CharField(max_length=200, blank=True)

    class Meta:
        ordering = ["id"]

    def __str__(self):
        return self.name

    @property
    def image_url(self):
        return static(f"shop/images/{self.image}") if self.image else ""
