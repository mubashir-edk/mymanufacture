from django.urls import path, include
from . import views

app_name = 'purifier'

urlpatterns = [
    path('', views.index),
    
    # Employee
    path('view_employees/', views.viewEmployees, name='view_employees'),
    path('create_employee/', views.createEmployee, name='create_employee'),
    path('each_employee/<uuid:id>', views.eachEmployee, name='each_employee'),
    path('update_employee/<uuid:id>', views.updateEmployee, name='update_employee'),
    path('delete_employee/<uuid:id>', views.deleteEmployee, name='delete_employee'),
    
    # Customer
    path('view_customers/', views.viewCustomers, name='view_customers'),
    path('create_customer/', views.createCustomer, name='create_customer'),
    path('each_customer/<uuid:id>', views.eachCustomer, name='each_customer'),
    path('update_customer/<uuid:id>', views.updateCustomer, name='update_customer'),
    path('delete_customer/<uuid:id>', views.deleteCustomer, name='delete_customer'),
    
    # Service
    path('view_services/', views.viewServices, name='view_services'),
    # path('create_services/', views.createService, name='create_service'),
]
