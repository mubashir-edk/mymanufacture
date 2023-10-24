from django import forms
from django.forms import modelformset_factory
from .models import *

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = '__all__'
        
        widgets = {
            'profile_image': forms.FileInput(attrs={
                'class': 'form-control',
                'id': 'formEmployee_Profile',
            }),
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Employee Name',
                'id': 'formEmployee_Name',
            }),
            'designation': forms.Select(attrs={
                'class': 'form-select',
                'placeholder': 'Employee Designation',
                'id': 'formEmployee_Designation',
            }),
            'address': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Employee Address',
                'id': 'formEmployee_Address',
            }),
            'contact_one': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Employee Contact 1',
                'id': 'formEmployee_ContactOne',
            }),
            'contact_two': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Employee Contact 2',
                'id': 'formEmployee_ContactTwo',
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'Employee Email',
                'id': 'formEmployee_Email',
            }),
        }
        

class DesignationForm(forms.ModelForm):
    class Meta:
        model = EmployeeDesignation
        fields = '__all__'
        
        widgets = {
            'designation': forms.TextInput(attrs={
                'class': 'form-control',
                'id': 'formDesignation',    
            }),
        }


class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = '__all__'
        
        widgets = {
            'profile_image': forms.FileInput(attrs={
                'class': 'form-control',  
                'id': 'formImage', 
            }),
            'name': forms.TextInput(attrs={
                'class': 'form-control', 
                'placeholder': 'Enter Name', 
                'id': 'formName', 
            }),
            'address': forms.TextInput(attrs={
                'class': 'form-control', 
                'placeholder': 'Enter Address',  
                'id': 'formAddress', 
            }),
            'contact': forms.NumberInput(attrs={
                'class': 'form-control', 
                'placeholder': 'Enter Contact Number',  
                'id': 'formContact', 
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control', 
                'placeholder': 'Enter Email',
                'id': 'formEmail', 
            }),
        }
        
        
class QuotationForm(forms.ModelForm):
    class Meta:
        model = Quotation
        fields = '__all__'
        
        widgets = {
            'customer_id': forms.Select(attrs={
                'class': 'form-select',
                'placeholder': 'Select Customer',
                'id': 'formCustomerName',
            }),
            'chalan_no': forms.TextInput(attrs={
                'class': 'form-control', 
                'placeholder': 'Enter Chalan', 
                'id': 'formChalan', 
            }),
        }
        

class QuotationJobForm(forms.ModelForm):
    class Meta:
        model = QuotationJob
        exclude = ('id', 'quotation_id',)
        
        widgets = {
            'length': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'length',
                'id': 'formLength', 
            }),
            'width': forms.NumberInput(attrs={
                'class': 'form-control', 
                'placeholder': 'width', 
                'id': 'formWidth', 
            }),
            'height': forms.NumberInput(attrs={
                'class': 'form-control', 
                'placeholder': 'height', 
                'id': 'formHeight', 
            }),
            'remarks': forms.Textarea(attrs={
                'class': 'form-control', 
                'placeholder': 'remarks', 
                'id': 'formRemarks',
                'rows': '1',
            }),
            'quantity': forms.NumberInput(attrs={
                'class': 'form-control', 
                'placeholder': 'quantity', 
                'id': 'formQuantity', 
            }),
            'attachment': forms.FileInput(attrs={
                'class': 'form-control', 
                'placeholder': 'attachment', 
                'id': 'formAttachment', 
            }),
        }
        
QuotationJobFormSet = modelformset_factory(
    QuotationJob,
    form = QuotationJobForm,
    extra = 0,
    # can_delete = True,
)


class JobAssignForm(forms.ModelForm):
    class Meta:
        model = JobAssign
        fields = ['employee_id']
        
        widgets = {
            'employee_id': forms.Select(attrs={
                'class': 'form-select',
                'id': 'formAssignEmployee',
            }),
            # 'job_id': forms.Select(attrs={
            #     'class': 'form-select',
            #     'id': 'formAssignJob',
            # }),
        }
        