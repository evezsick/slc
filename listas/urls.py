from django.contrib import admin
from django.urls import path, include
from . import views
from .views import list_products, create_product, update_product, delete_product

urlpatterns=[    
    path("", views.index, name="index"),
    path('new', create_product, name='create_products'),
    path('update/<int:id>/', update_product, name='update_product'),
    path('delete/<int:id>/', delete_product, name='delete_product'),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
]