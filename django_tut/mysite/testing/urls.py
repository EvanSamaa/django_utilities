from . import views
from django.urls import path

urlpatterns = [
    path('toJulie', views.index, name='index'),
]