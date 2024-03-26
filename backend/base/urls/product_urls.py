from django.urls import path
from base.views import product_views as views

urlpatterns = [
    path('s/', views.get_products, name='products'),
    path('/', views.get_product, name='product'),
]