from time import timezone
from typing import Iterable
from django.db import models
from django.contrib.auth.models import User
from functools import reduce
from django.core.exceptions import ValidationError
from django.utils.text import slugify
from unidecode import unidecode


class Category(models.Model):
    name = models.CharField(max_length=255, unique=True)
    slug = models.SlugField(blank=True)

    def save(self, *args, **kwargs) -> None:
        self.slug = slugify(unidecode(self.name))
        super(Category, self).save(*args, **kwargs)
        
    def __str__(self):
        return self.name
    

class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    quantity = models.IntegerField()
    price = models.DecimalField(decimal_places=2, max_digits=10)
    currency = models.SmallIntegerField(
        choices=(
            (1,'Dollar'), 
            (2, 'So`m')
            )
    ) 
    discount_price = models.DecimalField(
        decimal_places=2, 
        max_digits=10, 
        blank=True, 
        null=True
        )
    baner_image = models.ImageField(upload_to='baner/')
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    
    slug = models.SlugField(blank=True)

    def save(self, *args, **kwargs) -> None:
        self.slug = slugify(unidecode(self.name))
        super(Product, self).save(*args, **kwargs)


    @property
    def review(self):
        reviews = ProductReview.objects.filter(product_id=self.id)
        result = reduce(lambda result, x: result +x, reviews, 0)
        try:
            result = result / reviews.count()
        except ZeroDivisionError:
            result = 0
        return result
    
    @property 
    def is_discount(self):
        if self.discount_price is None:
            return 0
        return self.discount_price > 0
    
    @property 
    def is_active(self):
        return self.quantity > 0


class EnterProduct(models.Model):
    quantity = models.IntegerField()
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True, blank=True)
    quantity_enter_notation = models.SmallIntegerField(
        choices=(
            (0,'Ayrish'), 
            (1, 'Qo`shish')
            ), null=True, blank=True
    ) 
    date = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    
    slug = models.SlugField(blank=True)

    def save(self, *args, **kwargs) -> None:
        self.slug = slugify(unidecode(self.name))
        super(EnterProduct, self).save(*args, **kwargs)


class ProductImage(models.Model):
    image = models.ImageField(upload_to='products/')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    slug = models.SlugField(blank=True)

    def save(self, *args, **kwargs) -> None:
        self.slug = slugify(unidecode(self.name))
        super(ProductImage, self).save(*args, **kwargs)


class WishList(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    slug = models.SlugField(blank=True)

    def save(self, *args, **kwargs) -> None:
        self.slug = slugify(unidecode(self.name))
        super(WishList, self).save(*args, **kwargs)

def check_duplicate_wishlist(sender, instance, **kwargs):
    if WishList.objects.filter(user=instance.user, product=instance.product).exists():
        raise ValidationError("This product is already in the wishlist.")

models.signals.pre_save.connect(check_duplicate_wishlist, sender=WishList)


class ProductReview(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    mark = models.SmallIntegerField()
    slug = models.SlugField(blank=True)

    def save(self, *args, **kwargs) -> None:
        self.slug = slugify(unidecode(self.name))
        super(ProductReview, self).save(*args, **kwargs)


class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)
    slug = models.SlugField(blank=True)

    def save(self, *args, **kwargs) -> None:
        self.slug = slugify(unidecode(self.name))
        super(Cart, self).save(*args, **kwargs)

    @property
    def quantity(self):
        quantity = 0
        products = CartProduct.objects.filter(product_id = self.id)
        for i in products:
            quantity +=i.quantity
        return quantity

    @property
    def total_price(self):
        result = 0
        for i in CartProduct.objects.filter(card_id=self.id):
            result +=(i.product.price)*i.quantity
        return result


class CartProduct(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    slug = models.SlugField(blank=True)

    def save(self, *args, **kwargs) -> None:
        self.slug = slugify(unidecode(self.name))
        super(CartProduct, self).save(*args, **kwargs)
    
    @property
    def total_price(self):
        if self.product.is_discount:
            result = self.product.discount_price * self.quantity
        else:
            result = self.product.price * self.quantity
        return result