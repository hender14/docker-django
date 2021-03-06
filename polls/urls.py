from django.urls import path
from . import views

urlpatterns = [
    # path('templetes/', views.index_templete, name='index_templete'),
    path('', views.index, name='index'),
]