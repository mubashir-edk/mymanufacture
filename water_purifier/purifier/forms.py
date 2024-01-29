from django import forms
from .models import *

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = '__all__'
        
        widgets = {
            'profile': forms.FileInput(attrs={
                'class': 'form-control',
                'id': 'formEmployeeProfile',
            }),
            'name': forms.TextInput(attrs={
                'class': 'form-control', 
                'id': 'formEmployeeName', 
            }),
            'mobile': forms.TextInput(attrs={
                'class': 'form-control', 
                'id': 'formEmployeeMobile',
            }),
            'state': forms.Select(attrs={
                'class': 'form-select', 
                'id': 'formEmployeeState', 
            }),
            'district': forms.TextInput(attrs={
                'class': 'form-control', 
                'id': 'formEmployeeDistrict', 
            }),
            'address': forms.Textarea(attrs={
                'class': 'form-control', 
                'id': 'formEmployeeAddress',
                'rows': '4',
            }),
        }
        
class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = '__all__'
        
        widgets = {
            'profile': forms.FileInput(attrs={
                'class': 'form-control',
                'id': 'formCustomerProfile',
            }),
            'name': forms.TextInput(attrs={
                'class': 'form-control', 
                'id': 'formCustomerName', 
            }),
            'mobile': forms.TextInput(attrs={
                'class': 'form-control', 
                'id': 'formCustomerMobile',
            }),
            'address': forms.Textarea(attrs={
                'class': 'form-control', 
                'id': 'formCustomerAddress', 
                'rows': '4',
            }),
            'whatsapp_number': forms.TextInput(attrs={
                'class': 'form-control', 
                'id': 'formCustomerWhatsappNumber', 
            }),
            'installed_product': forms.CheckboxSelectMultiple(attrs={
                'class': 'form-checkbox', 
                'id': 'formCustomerInstalledProduct', 
            }),
        }
        
class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = '__all__'
        
        widgets = {
            'image': forms.FileInput(attrs={
                'class': 'form-control',
                'id': 'formCategoryImage',
            }),
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'id': 'formCategoryName',
            }),
        }
        
class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'
        
        widgets = {
            'product_serial': forms.TextInput(attrs={
                'class': 'form-control',
                'id': 'formProductSerial',
            }),
            'category': forms.Select(attrs={
                'class': 'form-select',
                'id': 'formProductCategory',
            }),
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'id': 'formProductName',
            }),
            'image': forms.FileInput(attrs={
                'class': 'form-control',
                'id': 'formProductImage',
            }),
            'services': forms.CheckboxSelectMultiple(attrs={
                'class': 'form-checkbox',
                'id': 'formProductServices',
            }),
        }
        
class ServiceForm(forms.ModelForm):
    class Meta:
        model = Service
        fields = '__all__'
        
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'id': 'formServiceName',
            }),
        }
        
class ServicerForm(forms.ModelForm):
    class Meta:
        model = Servicer
        fields = '__all__'
        
        widgets = {
            'name': forms.Select(attrs={
                'class': 'form-select',
                'id': 'formServicerName',
            }),
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Customize queryset of 'name' field
        self.fields['name'].queryset = self.fields['name'].queryset.exclude(servicer__isnull=False)
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].queryset = Employee.objects.all()
        self.fields['name'].label_from_instance = lambda obj: f"{obj.name}"
        
class ServiceWorkForm(forms.ModelForm):
    class Meta:
        model = ServiceWork
        # fields = '__all__'
        exclude = ('status',)
        
        
        widgets = {
            'customer_code': forms.Select(attrs={
                'class': 'form-select',    
                'id': 'formServiceWorkCustomer',    
            }),
            'product': forms.Select(attrs={
                'class': 'form-select',    
                'id': 'formServiceWorkProduct',    
            }),
            'service_name': forms.Select(attrs={
                'class': 'form-select',    
                'id': 'formServiceWorkService',    
            }),
            'comment_section': forms.Textarea(attrs={
                'class': 'form-control',    
                'id': 'formServiceWorkComment',
                'rows': '3',  
            }),
            'service_date': forms.DateInput(attrs={
                'type': 'date',
                'class': 'form-control',     
                'id': 'formServiceWorkDate',    
            }),
            'remark_section': forms.Textarea(attrs={
                'class': 'form-control',    
                'id': 'formServiceWorkRemark',
                'rows': '3',    
            }),
        }
        
class TestForm(forms.ModelForm):
    class Meta:
        model = Test
        fields = '__all__'
        
        
        widgets = {
            'test_name': forms.TextInput(attrs={
                'class': 'form-control',    
                'id': 'formTestName',    
            }),
            'customer_code': forms.Select(attrs={
                'class': 'form-select',    
                'id': 'formTestCustomerCode',     
            }),
            'ph_value': forms.TextInput(attrs={
                'class': 'form-control',    
                'id': 'formPhValue',    
            }),
            'tds_value': forms.TextInput(attrs={
                'class': 'form-control',    
                'id': 'formTdsValue',
            }),
            'iron_value': forms.TextInput(attrs={
                'class': 'form-control',     
                'id': 'formIronValue',    
            }),
            'hardness_value': forms.TextInput(attrs={
                'class': 'form-control',    
                'id': 'formHardnessValue',    
            }),
            'turbuet_value': forms.TextInput(attrs={
                'class': 'form-control',    
                'id': 'formTurbuetValue', 
            }),
        }
        
class ServiceWorkAssignForm(forms.ModelForm):
    class Meta:
        model = ServiceAssign
        fields = '__all__'
        
        widgets = {
            'service': forms.Select(attrs={
                'class': 'form-select',    
                'id': 'formAssignService',    
            }),
            'servicer': forms.Select(attrs={
                'class': 'form-select',    
                'id': 'formAssignServicer',     
            }),
            'notification': forms.TextInput(attrs={
                'class': 'form-control',    
                'id': 'formAssignNotification',    
            }),
        }