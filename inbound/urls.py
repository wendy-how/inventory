from django.urls import path
from . import views

urlpatterns = [
    path('', views.inbound_list, name='inbound_list'),
    path('add/', views.add_inbound_item, name='add_inbound_item'),
    path('<int:pk>/', views.inbound_detail, name='inbound_list'),
    path('inbound/update/<int:pk>/', views.update_inbound, name='update_inbound'),
     path('inbound/delete/<int:pk>/', views.delete_inbound, name='delete_inbound'),
]
