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
            'Address': forms.Textarea(attrs={
                'class': 'form-control', 
                'id': 'formCustomerAddress', 
                'rows': '4',
            }),
            'whatsapp_number': forms.TextInput(attrs={
                'class': 'form-control', 
                'id': 'formcustomerWhatsappNumber', 
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