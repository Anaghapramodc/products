
from django.contrib import admin
from django.urls import path, include

from . import views

urlpatterns = [
    path('api_overview/',views.api_overview,name='overviews'),
    path('product-list/', views.showall, name='product_list'),
    path('product-create/', views.createproduct, name='product_create'),
    path('product-detailview/<int:pk>/', views.detailview, name='product_detailview'),
    path('product-updateview/<int:pk>/', views.Updateview, name='product_updateview'),
    path('product-deleteview/<int:pk>/', views.deleteview, name='product_deleteview'),

]

