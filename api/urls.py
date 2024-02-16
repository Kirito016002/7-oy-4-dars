from . import views
from django.urls import path

app_name = 'main'

urlpatterns = [
    path('api_category', views.api_category, name='api_category'),
    path('api_product', views.api_product, name='api_product'),
    path('api_enter_product', views.api_enter_product, name='api_enter_product'),
    path('api_product_image', views.api_product_image, name='api_product_image'),
    path('api_wishlist', views.api_wishlist, name='api_wishlist'),
    path('api_product_review', views.api_product_review, name='api_product_review'),
    path('api_cart', views.api_cart, name='api_cart'),
    path('api_cart_product', views.api_cart_product, name='api_cart_product'),
]