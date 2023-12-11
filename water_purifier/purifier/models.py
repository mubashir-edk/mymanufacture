from django.db import models
import uuid
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.
class Employee(models.Model):
    
    STATE_CHOICES = (
    ('NULL', 'Select State'),
    ('AP', 'Andhra Pradesh'),
    ('AR', 'Arunachal Pradesh'),
    ('AS', 'Assam'),
    ('BR', 'Bihar'),
    ('CG', 'Chhattisgarh'),
    ('GA', 'Goa'),
    ('GJ', 'Gujarat'),
    ('HR', 'Haryana'),
    ('HP', 'Himachal Pradesh'),
    ('JH', 'Jharkhand'),
    ('KA', 'Karnataka'),
    ('KL', 'Kerala'),
    ('MP', 'Madhya Pradesh'),
    ('MH', 'Maharashtra'),
    ('MN', 'Manipur'),
    ('ML', 'Meghalaya'),
    ('MZ', 'Mizoram'),
    ('NL', 'Nagaland'),
    ('OD', 'Odisha'),
    ('PB', 'Punjab'),
    ('RJ', 'Rajasthan'),
    ('SK', 'Sikkim'),
    ('TN', 'Tamil Nadu'),
    ('TS', 'Telangana'),
    ('TR', 'Tripura'),
    ('UK', 'Uttarakhand'),
    ('UP', 'Uttar Pradesh'),
    ('WB', 'West Bengal'),
    ('AN', 'Andaman and Nicobar Islands'),
    ('CH', 'Chandigarh'),
    ('DN', 'Dadra and Nagar Haveli and Daman and Diu'),
    ('DL', 'Delhi'),
    ('JK', 'Jammu and Kashmir'),
    ('LA', 'Ladakh'),
    ('LD', 'Lakshadweep'),
    ('PY', 'Puducherry'),)
    
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, unique=True, editable=False)
    profile = models.ImageField(null=True, blank=True, upload_to="employee_profiles/")
    name = models.CharField(max_length=50)
    mobile = models.CharField(max_length=20)
    state = models.CharField(max_length=50, choices=STATE_CHOICES, default='NULL')
    district = models.CharField(max_length=100)
    address = models.TextField()
    employee_code = models.CharField(max_length=50, null=True, blank=True, unique=True)
    
    def __str__(self) -> str:
        return self.employee_code

class Customer(models.Model):
    
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, unique=True, editable=False)
    profile = models.ImageField(null=True, blank=True, upload_to="customer_profiles/")
    name = models.CharField(max_length=50)
    address = models.TextField()
    mobile = models.CharField(max_length=20)
    whatsapp_number = models.CharField(max_length=20)
    # installed_product
    # location
    customer_code = models.CharField(max_length=50, blank=True, unique=True)
    
    def __str__(self) -> str:
        return self.customer_code
    
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
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=100)
    image = models.ImageField(null=True, blank=True, upload_to="product_images/")
    services = models.ManyToManyField(Service)
    
    def __str__(self) -> str:
        return self.name
    
class Servicer(models.Model):
    
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, unique=True, editable=False)
    name= models.ForeignKey(Employee, on_delete=models.CASCADE)
    
    def __str__(self) -> str:
        return self.name.employee_code

# class Test(models.Model):
    
    

# class ServiceWork(models.Model):