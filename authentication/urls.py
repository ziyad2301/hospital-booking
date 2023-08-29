from django.urls import path
from . import views

urlpatterns = [
    path('register',views.registration,name='register'),
    path('login',views.user_login,name='login'),
    path('logout',views.user_logout,name='logout'),
    path('profile/<int:user_id>/', views.user_profile, name='user_profile'),
    path('profile',views.update_profile,name='profile'),

]