from django.urls import path , include
from . import views
urlpatterns = [
    path('', views.home, name='home'),
    path('pointer', views.pointer, name='pointer'),
    path('about', views.about, name='about'),
    path('service', views.my_view, name='service'),
    path('service/result/', views.result, name='result'),
]
