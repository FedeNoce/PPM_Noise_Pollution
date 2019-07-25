from django.urls import path

from . import views

app_name = 'Noise_Pollution'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:id>/', views.graphic, name='graphic'),
    ]