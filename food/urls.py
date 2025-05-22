from django.urls import path
from food import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:item_id>/', views.detail, name = 'detail'),
    path('add/', views.itemForm, name='itemForm'),
]
