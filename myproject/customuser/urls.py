from django.urls import path
from customuser import views

urlpatterns = [
    path('user-create',views.create_user,name='create_user'),
    path('login',views.login,name='login'),
    path('dashboard',views.dashboard,name='dashboard'),
    path('logout',views.logout,name='logout'),
]
