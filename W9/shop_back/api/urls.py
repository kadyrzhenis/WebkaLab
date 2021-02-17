from django.urls import path

from . import views

urlpatterns = [
	path('', views.home, name = 'home'),
    path('products', views.products, name='products'),
    path('categories', views.categories, name = 'categories'),
    path('products/<int:id>', views.product, name = 'product'),
    path('categories/<int:id>', views.category, name = 'category'),
    path('categories/<int:id>/products', views.prodcat, name = 'productofcategory'),
]
