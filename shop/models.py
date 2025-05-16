
from django.db import models
from django.utils.text import slugify
from django.conf import settings
from django.core.validators import MinValueValidator, MaxValueValidator


User = settings.AUTH_USER_MODEL

class Category(models.Model):

    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(unique=True)
    display_order = models.IntegerField(default=0)
    parent_id = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True)
    image = models.JSONField(blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)
    domain_user_id = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, related_name='domain_user')
    added_by_user_id = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, related_name='added_by')



    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.headline)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class Prod(models.Model):
    class Status(models.TextChoices):  # Define Status as a subclass of TextChoices
        ACTIVE = 'ACTIVE', 'Active'
        INACTIVE = 'INACTIVE', 'Inactive'
        PENDING = 'PENDING', 'Pending'
    id = models.AutoField(primary_key=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='prods')
    name = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    description = models.TextField()
    specifications = models.JSONField()
    sku = models.CharField(max_length=255, unique=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField()
    is_available = models.BooleanField(default= True)
    image = models.JSONField()
    initial_buying_price = models.FloatField()
    initial_selling_price = models.FloatField()
    weight = models.FloatField()
    dimensions = models.CharField(default='0x0x0', max_length=255)
    uom = models.CharField(max_length=255)
    color = models.CharField(max_length=255)
    tax_percentage = models.FloatField()
    brand = models.CharField(max_length=255)
    brand_model = models.CharField(max_length=255)

    seo_title = models.CharField(max_length=255)
    seo_description = models.TextField()
    seo_keywords = models.JSONField()
    addition_details = models.JSONField()
    domain_user_id = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True,
                                       related_name='domain_user_id_products')
    added_by_user_id = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True,
                                         related_name='added_by_user_id_products')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if not self.slug and self.name:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)


    def __str__(self):
        return self.name


class ProductQuestions(models.Model):
    question = models.TextField()
    answer = models.TextField(blank=True, null=True)
    status = models.CharField(max_length=10, choices=Prod.Status.choices, default=Prod.Status.ACTIVE)

    product = models.ForeignKey(Prod, on_delete=models.CASCADE, related_name='questions')
    domain_user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True,
                                    related_name='question_domains')
    question_user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True,
                                      related_name='questions_asked')
    answer_user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True,
                                    related_name='questions_answered')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Q: {self.question[:30]}"


class ProductReviews(models.Model):
    review_images = models.JSONField(blank=True, null=True)  # Consider image model
    rating = models.FloatField(validators=[MinValueValidator(1.0), MaxValueValidator(5.0)])
    reviews = models.TextField()
    status = models.CharField(max_length=10, choices=Prod.Status.choices, default=Prod.Status.ACTIVE)

    product = models.ForeignKey(Prod, on_delete=models.CASCADE, related_name='reviews')
    domain_user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True,
                                    related_name='review_domains')
    review_user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, related_name='user_reviews')

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Review {self.pk} for {self.product}"


class Cart(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True)
    session_key = models.CharField(max_length=255, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)


class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey(Prod, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def subtotal(self):
        return self.product.price * self.quantity


class Order(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('processing', 'Processing'),
        ('shipped', 'Shipped'),
        ('completed', 'Completed'),
        ('cancelled', 'Cancelled'),
    ]

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True)
    order_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    total = models.DecimalField(max_digits=10, decimal_places=2)
    shipping_address = models.TextField()
    payment_method = models.CharField(max_length=50)
    payment_status = models.CharField(max_length=50, default='unpaid')

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey(Prod, on_delete=models.SET_NULL, null=True)
    quantity = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)


class Address(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=100)
    address_line1 = models.CharField(max_length=255)
    address_line2 = models.CharField(max_length=255, blank=True)
    city = models.CharField(max_length=100)
    postal_code = models.CharField(max_length=20)
    country = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.full_name}, {self.address_line1}"

class Wishlist(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    products = models.ManyToManyField(Prod, related_name='wishlists')



class Coupon(models.Model):
    code = models.CharField(max_length=20, unique=True)
    discount_percent = models.PositiveIntegerField()
    active = models.BooleanField(default=True)
    valid_from = models.DateTimeField()
    valid_to = models.DateTimeField()
