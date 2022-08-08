from django.urls import path

from . import views

app_name = 'controller'
urlpatterns = [
    path('', views.index, name='index'),
    path('<slug:box_slug>/', views.box, name='box'),
    path('<slug:box_slug>/<int:category_id>/', views.box_category, name='box-category'),
    path('<slug:box_slug>/action/<str:cmd>', views.action, name='action'),
    path('<slug:box_slug>/<int:item_id>/play/', views.item, name='item'),
    path('<slug:box_slug>/<int:item_id>/item-play/', views.item_play, name='item-play'),
    path('<slug:box_slug>/<int:item_id>/item-queue/', views.item_queue, name='item-queue'),
]