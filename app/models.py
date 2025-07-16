from django.db import models

class Brand(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

class Product(models.Model):
    CATEGORY_CHOICES = [
        ('pen', 'Pens'),
        ('notebook', 'Notebooks'),
        ('game', 'Games'),
        ('cool_Items', 'Cool Items'),
        ('color', 'Colors'),
    ]

    name = models.CharField(max_length=255)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    description = models.TextField()
    mrp = models.DecimalField(max_digits=10, decimal_places=2)
    selling_price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='product_images/')
    image2 = models.ImageField(upload_to='product_images/', null=True, blank=True)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES, blank=True, null=True)

    def __str__(self):
        return self.name

    def discount_percentage(self):
        if self.mrp > self.selling_price:
            return int((self.mrp - self.selling_price) / self.mrp * 100)
        return 0
