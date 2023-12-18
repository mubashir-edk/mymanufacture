from django.urls import path
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
    path('view_services/', views.viewAndCreateServices, name='view_services'),
    # path('update_services/<uuid:id>', views.updateService, name='update_services'),
    
    # Product
    path('view_categories/', views.viewCategories, name='views_categories'),
    path('create_category/', views.createCategory, name='create_category'),
    path('view_products/', views.viewProducts, name='view_products'),
    path('create_product/', views.createProduct, name='create_product'),
    
    # Servicer
    path('view_servicers/', views.viewServicers, name='view_servicers'),
    path('create_servicer/', views.createServicer, name='create_servicer'),
    path('fetch_servicer/<uuid:selected_employee>', views.fetchServicer, name='fetch_servicer'),
    
    # Service Work
    path('view_serviceworks/', views.viewServiceWorks, name='view_serviceworks'),
    path('create_servicework/', views.createServiceWork, name='create_servicework'),
    
    # Test
    path('view_tests/', views.viewTests, name='view_tests'),
    path('create_test/', views.createTest, name='create_test'),
    
]
