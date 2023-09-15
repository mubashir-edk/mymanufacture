from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    
    # Customer
    path('create_customer', views.createCustomer, name='create_customer'),
    path('view_customers', views.viewCustomers, name='view_customers'),
    
    #quotation
    path('create_quotation', views.createQuotation, name='create_quotation'),
    path('update_quotation/<uuid:quotation_id>', views.updateQuotation, name='update_quotation'),
    path('view_quotations', views.viewQuotations, name='view_quotations'),
    
    path('view_quotation_jobs', views.viewQuotationJobs, name='view_quotation_jobs'),
    
    
    # path('view-users/', views.viewUsers, name='view-users'),
    # path('update-user/<int:id>/', views.updateUsers, name='update-user'),
    # path('delete-user/<int:id>/', views.deleteUsers, name='delete-user'),
    
    # path('dashboard/', views.viewDashboard, name='dashboard'),
]