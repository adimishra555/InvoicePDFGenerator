
from django.db import models

class UserDB(models.Model):
    user_roles = (("Seller", "Seller"), ("Buyer", "Buyer"), ("Admin", "Admin"))
    gender_choices = (("Male", "Male"), ("Female", "Female"))
    
    user_id = models.CharField(max_length=100, unique=True, blank=True, null=True)
    username = models.CharField(max_length=100, unique=True, blank=True, null=True)
    first_name = models.CharField(max_length=100, blank=True, null=True)
    last_name = models.CharField(max_length=100, blank=True, null=True)
    gender = models.CharField(max_length=50, choices=gender_choices, blank=True, null=True)
    profile_picture = models.ImageField(upload_to="profile_images", default="profile_images/sunder.jpg", blank=True, null=True)
    phone = models.CharField(max_length=100, unique=True, blank=True, null=True)
    role = models.CharField(max_length=50, choices=user_roles, default="Buyer")
    email = models.CharField(max_length=100, unique=True, blank=True, null=True)
    company = models.CharField(max_length=1000, blank=True, null=True)
    address_line1 = models.CharField(max_length=1000, blank=True, null=True)
    city = models.CharField(max_length=100, blank=True, null=True)
    state = models.CharField(max_length=100, blank=True, null=True)
    postal_code = models.CharField(max_length=50, blank=True, null=True)
    country = models.CharField(max_length=100, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.username} ({self.role})"


class ProductDB(models.Model):
    seller = models.ForeignKey(UserDB, on_delete=models.CASCADE)
    product_title = models.CharField(max_length=1000)
    brand = models.CharField(max_length=500, blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    gst = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.product_title} - {self.price}"


class OrderDB(models.Model):
    order_id = models.CharField(max_length=100, unique=True)
    user = models.ForeignKey(UserDB, on_delete=models.CASCADE)
    product = models.ForeignKey(ProductDB, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order {self.order_id} - {self.user.username}"
