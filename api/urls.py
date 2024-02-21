from . import views
from django.urls import path

app_name = 'main'

urlpatterns = [
    path('category_list', views.category_list),
    path('category_detail', views.category_detail),
    path('product_list', views.product_list),
    path('product_detail/<int:id>', views.product_detail),
    path('wishlist', views.wishlist),
]