from django.db import models
# from django.contrib.gis.db import models as point_field
import uuid

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
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, blank=True, null=True)
    name = models.CharField(max_length=100)
    image = models.ImageField(null=True, blank=True, upload_to="product_images/")
    services = models.ManyToManyField(Service)
    
    def __str__(self) -> str:
        return self.name

class Customer(models.Model):
    
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, unique=True, editable=False)
    profile = models.ImageField(null=True, blank=True, upload_to="customer_profiles/")
    name = models.CharField(max_length=50)
    address = models.TextField()
    mobile = models.CharField(max_length=20)
    whatsapp_number = models.CharField(max_length=20)
    installed_product = models.ManyToManyField(Product, blank=True, null=True)
    # location = point_field.PointField()
    customer_code = models.CharField(max_length=50, blank=True, unique=True)
    
    def __str__(self) -> str:
        return self.customer_code
    
class Servicer(models.Model):
    
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, unique=True, editable=False)
    name= models.ForeignKey(Employee, on_delete=models.CASCADE)
    
    def __str__(self) -> str:
        return self.name.employee_code

class Test(models.Model):
    
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, unique=True, editable=False)
    test_name = models.CharField(max_length=150)
    ph_value = models.CharField(max_length=30)
    tds_value = models.CharField(max_length=30)
    iron_value = models.CharField(max_length=30)
    hardness_value = models.CharField(max_length=30)
    turbuet_value = models.CharField(max_length=30)
    
    def __str__(self) -> str:
        return self.test_name

class ServiceWork(models.Model):
    
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, unique=True, editable=False)
    customer_code = models.ForeignKey(Customer, on_delete=models.CASCADE)
    service_name = models.ForeignKey(Service, models.SET_NULL, null=True)
    comment_section = models.TextField()
    service_date = models.DateField()
    remark_section = models.TextField()
    
    def __str__(self) -> str:
        return self.customer_code.customer_code