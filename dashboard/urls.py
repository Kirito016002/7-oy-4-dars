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
    path('product_create', views.product_create, name='product_create'),
    # auth
    path('sign_in', views.sign_in, name='sign_in'),
    path('sign_up', views.sign_up, name='sign_up'),
    path('sign_out', views.sign_out, name='sign_out'),
    path('user_update', views.user_update, name='user_update'),
    # enter product
    path('product_list', views.product_list, name='product_list'),
    path('prodect_update/<int:id>', views.prodect_update, name='prodect_update'),
    path('product_detail/<int:id>', views.product_detail, name='product_detail'),
    
    path('add_card_excel/<int:id>', views.add_card_excel, name='add_card_excel'),
    path('add_all_excel', views.add_all_excel, name='add_all_excel'),
]
