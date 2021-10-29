from django.urls import path
from . import views

app_name = 'superheroes'
urlpatterns = [
    path('', views.index, name = 'index'),
    path('<int:hero_id>/', views.detail, name = 'detail' ),
    path('new/', views.create, name='create'),
    path('<int:hero_id>/edit', views.edit, name='edit'),
    path('<int:hero_id>/delete/', views.delete, name = 'delete'),
]