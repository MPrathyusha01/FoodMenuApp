from django.urls import path
from food import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:item_id>/', views.detail, name = 'detail'),
    path('add/', views.itemForm, name='itemForm'),
    path('update/<int:item_id>/', views.item_update, name='item_update'),
    path('delete/<int:item_id>/', views.item_delete, name='item_delete')
]
