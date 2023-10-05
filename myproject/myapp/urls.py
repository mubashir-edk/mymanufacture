from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    
    # Customer
    path('create_customer', views.createCustomer, name='create_customer'),
    path('update_customer/<uuid:customer_id>', views.updateCustomer, name='update_customer'),
    path('view_customers', views.viewCustomers, name='view_customers'),
    
    #quotation
    path('create_quotation', views.createQuotation, name='create_quotation'),
    path('update_quotation/<uuid:quotation_id>', views.updateQuotation, name='update_quotation'),
    path('delete_quotation/<uuid:quotation_id>', views.deleteQuotation, name='delete_quotation'),
    path('view_quotations', views.viewQuotations, name='view_quotations'),
    
    path('view_quotation_jobs', views.viewQuotationJobs, name='view_quotation_jobs'),
    path('each_quotation_job/<uuid:job_id>', views.eachQuotationJob, name='each_quotation_job'),
    path('delete_attachment/<uuid:job_id>', views.deleteAttachment, name='delete_attachment'),
    
    
    # path('view-users/', views.viewUsers, name='view-users'),
    # path('update-user/<int:id>/', views.updateUsers, name='update-user'),
    # path('delete-user/<int:id>/', views.deleteUsers, name='delete-user'),
    
    # path('dashboard/', views.viewDashboard, name='dashboard'),
]