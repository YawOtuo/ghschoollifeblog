from django.urls import path
from django.views.generic.edit import CreateView

from . import views

app_name = 'ghblog'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('holychild/', views.HolyChild.as_view(), name='holychild'),
    path('wesley/', views.Wesley.as_view(), name='wesley'),
    path('motown/', views.Motown.as_view(), name='motown'),
    path('more/', views.More.as_view(), name='more'),

]
