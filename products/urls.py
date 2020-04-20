from django.urls import path

from . import views

app_name = 'products'
urlpatterns = [
    path('', views.index, name='index'),
    path('products/new', views.create, name="new"),
    path('products/<slug:slug>/update', views.update, name="update"),
    path('products/<slug:slug>/delete', views.delete, name="delete")
]
