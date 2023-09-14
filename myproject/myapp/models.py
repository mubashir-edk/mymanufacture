from django.db import models
import uuid
from django.utils import timezone

# Create your models here.

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
    
    def __str__(self) -> str:
        return self.customer_id.name
    
class QuotationJob(models.Model):
    
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, unique=True, editable=False)
    quotation_id = models.ForeignKey(Quotation, on_delete=models.CASCADE)
    length = models.IntegerField(null=False, blank=False)
    width = models.IntegerField(null=False, blank=False)
    height = models.IntegerField(null=False, blank=False)
    remarks = models.CharField(max_length=700, null=True, blank=True)
    quantity = models.IntegerField(null=False, blank=False)
    attachment = models.FileField(null=True, blank=True)
    
    def __str__(self) -> str:
        return str(self.quotation_id.chalan_no)
    
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
    
    