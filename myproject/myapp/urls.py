from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    
    # Employee
    path('create_employee', views.createEmployee, name='create_employee'),
    path('update_employee/<uuid:employee_id>', views.updateEmployee, name='update_employee'),
    path('view_employees', views.viewEmployees, name='view_employees'),
    
    # HRM
    path('create_company_position', views.createCompanyPosition, name='create_company_position'),
    path('view_company_positions', views.viewCompanyPositions, name='view_company_positions'),
    
    # Customer
    path('create_customer', views.createCustomer, name='create_customer'),
    path('update_customer/<uuid:customer_id>', views.updateCustomer, name='update_customer'),
    path('view_customers', views.viewCustomers, name='view_customers'),
    
    # Quotation
    path('create_quotation', views.createQuotation, name='create_quotation'),
    path('update_quotation/<uuid:quotation_id>', views.updateQuotation, name='update_quotation'),
    path('delete_quotation/<uuid:quotation_id>', views.deleteQuotation, name='delete_quotation'),
    path('view_quotations', views.viewQuotations, name='view_quotations'),
    
    path('view_quotation_jobs', views.viewQuotationJobs, name='view_quotation_jobs'),
    path('each_quotation_job/<uuid:job_id>', views.eachQuotationJob, name='each_quotation_job'),
    path('delete_attachment/<uuid:job_id>', views.deleteAttachment, name='delete_attachment'),
    
    # JobAssign
    path('job_assigning', views.jobAssigning, name='job_assigning'),
    path('job_unassign/<uuid:job_task_id>', views.unAssignJob, name='job_unassign'),
    
    # SequentialCode
    path('sequential_code', views.sequentialCode, name='sequential_code'),
    
    # Task
    path('view_tasks', views.viewTasks, name='view_tasks'),
    
    # Machine
    path('machines', views.machineSettings, name='machines'),
    
]