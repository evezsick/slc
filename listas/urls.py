from django.contrib import admin
from django.urls import path, include
from . import views
from .views import list_products, create_product, update_product, delete_product, update_list, create_list, delete_list, lista

urlpatterns=[    
    path("", views.index, name="index"),
    path('new', create_product, name='create_products'),
    path('new_list', create_list, name='create_list'),
    path('product', list_products, name='list_products'),
    path('update/<int:id>/', update_product, name='update_product'),
    path('delete/<int:id>/', delete_product, name='delete_product'),
    path('delete/<int:id>/', delete_list, name='delete_list'),
    path('update/<int:id>/', update_list, name='update_list'),
    path("login", views.login_view, name="login_view"),
    path("logout", views.logout_view, name="logout"),
]