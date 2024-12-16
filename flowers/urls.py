from django.urls import path
from . import views

urlpatterns = [
    path('', views.flower_list, name='flower_list'),
    path('type/<int:type_id>/', views.flower_by_type, name='flower_by_type'),
    path('<int:flower_id>/', views.flower_detail, name='flower_detail'),
    path('types/', views.flower_type_list, name='flower_type_list'),
]
