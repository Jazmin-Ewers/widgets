from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('widget/create/', views.WidgetCreate.as_view(), name='widgets_create'),
]