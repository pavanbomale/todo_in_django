from django.urls import path
from . import views
from django.urls import re_path as url
urlpatterns = [
    path('', views.index, name='index'),
    path('mytodos', views.mytodos, name='mytodos'),
    path('mytodos/delete/<int:id>', views.delete, name='delete'),
    path('mytodos/edit/<int:id>', views.edit, name='edit'),
]