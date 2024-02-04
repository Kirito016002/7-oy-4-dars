from . import views
from django.urls import path

app_name = 'main'

urlpatterns = [
    path('', views.index, name='index'),
    path('product/<int:id>', views.product_detail, name='product_detail'),
    path('carts', views.carts, name='carts'),
    path('cart_detail', views.cart_detail, name='cart_detail'),
    path('cart/detail/delete/', views.cart_detail_delete, name='cart_detail_delete'),
    path('cart_sale/<int:id>', views.cart_sale, name='cart_sale'),
    path('cart_create/<int:id>/', views.cart_create, name='cart_create'),
]