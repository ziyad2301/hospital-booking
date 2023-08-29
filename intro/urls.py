from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('doctor', views.doctor, name='doctor'),
    path('department', views.department, name='department'),
    path('contact', views.contact, name='contact'),
    path('booking', views.booking, name='booking'),
    path('about', views.about, name='about'),
    # path('register', views.register, name='register'),
    # path('login', views.login, name='login')

]