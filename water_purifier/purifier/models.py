from django.db import models
from django.db.models import Subquery
import uuid
# from location_field.models.spatial import LocationField
# from location_field.widgets import GoogleMapsWidget
# from geoposition.fields import GeopositionField

# Create your models here.
class Employee(models.Model):
    
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, unique=True, editable=False)
    profile = models.ImageField(null=True, blank=True, upload_to="employee_profiles/")
    name = models.CharField(max_length=50)
    mobile = models.CharField(max_length=20)
    address = models.TextField()
    employee_code = models.CharField(max_length=50, blank=True, unique=True)
    
    def __str__(self) -> str:
        return self.employee_code
    
class Category(models.Model):
    
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, unique=True, editable=False)
    image = models.ImageField(null=True, blank=True, upload_to="category_images/")
    name = models.CharField(max_length=50)
    
    def __str__(self) -> str:
        return self.name
    
class Service(models.Model):
    
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, unique=True, editable=False)
    name = models.CharField(max_length=180)
    
    def __str__(self) -> str:
        return self.name
    
class Product(models.Model):
    
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, unique=True, editable=False)
    product_serial = models.CharField(max_length=100, blank=True, unique=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, blank=True, null=True)
    name = models.CharField(max_length=100)
    image = models.ImageField(null=True, blank=True, upload_to="product_images/")
    services = models.ManyToManyField(Service, null=True, blank=True)
    
    def __str__(self) -> str:
        return self.name

class Customer(models.Model):
    
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, unique=True, editable=False)
    profile = models.ImageField(null=True, blank=True, upload_to="customer_profiles/")
    name = models.CharField(max_length=50)
    address = models.TextField()
    mobile = models.CharField(max_length=20)
    whatsapp_number = models.CharField(max_length=20)
    installed_product = models.ManyToManyField(Product, null=True, blank=True)
    customer_code = models.CharField(max_length=50, blank=True, unique=True)
    # location = LocationField(based_fields=[name], zoom=7, blank=True)
    
    def __str__(self) -> str:
        return self.customer_code
    
class Servicer(models.Model):
    
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, unique=True, editable=False)
    name= models.ForeignKey(Employee, on_delete=models.CASCADE)
    
    def __str__(self) -> str:
        return self.name.employee_code
    
    queryset = Employee.objects.exclude(id=name.name)
    print(queryset)

class Test(models.Model):
    
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, unique=True, editable=False)
    customer_code = models.ForeignKey(Customer, on_delete=models.CASCADE)
    test_name = models.CharField(max_length=150)
    ph_value = models.CharField(max_length=30)
    tds_value = models.CharField(max_length=30)
    iron_value = models.CharField(max_length=30)
    hardness_value = models.CharField(max_length=30)
    turbuet_value = models.CharField(max_length=30)
    
    def __str__(self) -> str:
        return self.test_name

class ServiceWork(models.Model):
    
    STATUS_CHOICES = (
        ('pending', 'Pending'),
        ('working', 'Working'),
        ('completed', 'Completed'),
    )
    
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, unique=True, editable=False)
    service_work_code = models.CharField(max_length=50, blank=True, unique=True)
    customer_code = models.ForeignKey(Customer, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    service_name = models.ManyToManyField(Service)
    comment_section = models.TextField(null=True, blank=True)
    service_date = models.DateField()
    remark_section = models.TextField(null=True, blank=True)
    status = models.CharField(max_length=30, choices=STATUS_CHOICES, default='pending')
    
    def __str__(self) -> str:
        return self.service_work_code
    
class ServiceAssign(models.Model):
    
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, unique=True, editable=False)
    service = models.ForeignKey(ServiceWork, on_delete=models.CASCADE, blank=True)
    servicer = models.ForeignKey(Servicer, on_delete=models.SET_NULL, null=True, blank=True)
    notification = models.CharField(max_length=500, blank=True)
    
    def __str__(self):
        return str(self.service)
    
    