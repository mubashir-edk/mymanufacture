from typing import Any
from django.db import models
import uuid
from django.utils import timezone

# Create your models here.

class EmployeeDesignation(models.Model):
    
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, unique=True, editable=False)
    designation = models.CharField(max_length=30)
    
    def __str__(self) -> str:
        return self.designation

class Employee(models.Model):
    
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, unique=True, editable=False)
    name = models.CharField(max_length=30)
    designation = models.ForeignKey(EmployeeDesignation, on_delete=models.CASCADE)
    address = models.CharField(max_length=150)
    contact_one = models.IntegerField()
    contact_two =models.IntegerField()
    email = models.EmailField()
    profile_image = models.ImageField(null=True, blank=True, upload_to="employees_profile/")
    
    def __str__(self) -> str:
        return self.name


class Customer(models.Model):
    
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, unique=True, editable=False)
    name = models.CharField(max_length=30)
    address = models.CharField(max_length=150)
    contact = models.IntegerField()
    email = models.EmailField()
    profile_image = models.ImageField(null=True, blank=True, upload_to="profiles/")
    
    def __str__(self) -> str:
        return self.name
    
class Quotation(models.Model):
    
    status_choices=( ('draft', 'Draft'), ('in_process', 'In Process'), ('ready_to_deliver', 'Ready to Deliver'), ('delivered_successfully', 'Delivered Successfully') )

    
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, unique=True, editable=False)
    customer_id = models.ForeignKey(Customer, on_delete=models.CASCADE)
    chalan_no = models.IntegerField(null=False, blank=True)
    created_on = models.DateTimeField(default=timezone.now ,null=False, blank=False)
    status = models.CharField(max_length=50, choices=status_choices, default='draft')
    
    sequential_code = models.CharField(max_length=30, null=True, blank=True, unique=True)
    
    def __str__(self) -> str:
        return self.sequential_code
    
class SequentialCode(models.Model):
    
    models_choices=( ('quotation', 'Quotation'), ('quotation_job', 'Quotation Job'), ('task', 'Task') )
    
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, unique=True, editable=False)
    code_prefix = models.CharField(max_length=3)
    code_size = models.IntegerField()
    code_suffix = models.CharField(max_length=3, null=True, blank=True)
    code_of = models.CharField(max_length=30, choices=models_choices)
    
    def __str__(self) -> str:
        return self.code_of
    
class QuotationJob(models.Model):
    
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, unique=True, editable=False)
    quotation_id = models.ForeignKey(Quotation, on_delete=models.CASCADE)
    length = models.FloatField(null=False, blank=False)
    width = models.FloatField(null=False, blank=False)
    height = models.FloatField(null=False, blank=False)
    remarks = models.CharField(max_length=700, null=True, blank=True)
    quantity = models.IntegerField(null=False, blank=False)
    attachment = models.FileField(null=True, blank=True)
    
    sequential_code = models.CharField(max_length=30, null=True, blank=True, unique=True)
    
    def __str__(self) -> str:
        return str(self.sequential_code)
    
class Machine(models.Model):
    
    status_choices=( ('ready_to_work', 'Ready to work'), ('running', 'Running'), ('In maintanance', 'In Maintanace') )
    
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, unique=True, editable=False)
    machine_name = models.CharField(max_length=50)
    status = models.CharField(max_length=50, choices=status_choices, default='ready_to_work')
    
    def __str__(self) -> str:
        return self.machine_name
    
class Task(models.Model):
    
    status_choices=( ('pending', 'Pending'), ('in_progress', 'In Progress'), ('completed', 'Completed') )
    
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, unique=True, editable=False)
    job_id = models.ForeignKey(QuotationJob, on_delete=models.CASCADE)
    machine_id = models.ForeignKey(Machine, on_delete=models.CASCADE)
    estimate_duration = models.DurationField(null=True, blank=True)
    completed_in = models.DurationField(null=True, blank=True)
    status = models.CharField(max_length=30, choices=status_choices, default='pending')
    
    def __str__(self) -> str:
        return self.job_id
    
class JobAssign(models.Model):
    
    employee_id = models.ForeignKey(Employee, on_delete=models.CASCADE)
    job_id = models.ForeignKey(QuotationJob, on_delete=models.CASCADE)
    
    def __str__(self) -> str:
        return str(self.employee_id)
    


    