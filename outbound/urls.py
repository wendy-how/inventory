from django.urls import path
from . import views

urlpatterns = [
    path('', views.outbound_list, name='outbound_list'),
    path('add/', views.add_outbound_item, name='add_outbound_item'),
    path('<int:pk>/', views.outbound_list, name='outbound_list'),
]
