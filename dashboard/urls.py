from . import views
from django.urls import path

app_name = 'dashboard'

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    # Category
    path('list_category', views.list_category, name='list_category'),
    path('create_category', views.create_category, name='create_category'),
    path('detail_category/<int:id>', views.detail_category, name='detail_category'),
    path('delete_category/<int:id>', views.delete_category, name='delete_category'),
    # Product
    path('product_create', views.product_create, name='product_create')
]