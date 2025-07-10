from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login, name='login'),
    path('dash/',views.dashboard,name='home'),
    path('set-password/', views.set_password, name='set_password'),
]
