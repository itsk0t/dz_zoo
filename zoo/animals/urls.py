from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.animals, name='animals'),
    path('create', views.create, name='create'),
    path('<int:pk>', views.AnimalsDetailView.as_view(), name='animal_detail')
]
