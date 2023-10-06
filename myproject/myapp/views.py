from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from myapp.models import *
from myapp.forms import *
from django.urls import reverse
from django.forms import inlineformset_factory
# Create your views here.

def home(request):
    return render(request, 'home.html')


# Employee Functions --------------------------------------------------------------------------------------------------------------------
@login_required
def createEmployee(request):
    
    employee_form = EmployeeForm()
    if request.method == 'POST':
        employee_form = EmployeeForm(request.POST, request.FILES)
        if employee_form.is_valid():
            employee_form.save()
            return redirect('view_employees')
    return render(request, 'employee/employee.html', {'employee_form': employee_form})

@login_required
def updateEmployee(request, employee_id):
    employee = get_object_or_404(Employee, pk=employee_id)
    
    employee_form = EmployeeForm(instance=employee)
    
    if request.method == 'POST':
        employee_form = EmployeeForm(request.POST, request.FILES, instance=employee)
        
        if employee_form.is_valid():
            
            employee_form.save()
            
            return redirect(reverse('update_employee', kwargs={'employee_id': employee_id}))
    
    return render(request, 'employee/employee.html', {'employee_form': employee_form, 'employee': employee})

@login_required
def viewEmployees(request):
    
    employees = Employee.objects.all()
    employees_exists = employees.exists()
    return render(request, 'employee/view_employees.html',{'employees': employees, 'employees_exist': employees_exists})


# Customer Functions --------------------------------------------------------------------------------------------------------------------
@login_required
def createCustomer(request):
    
    customer_form = CustomerForm()
    if request.method=='POST':
        customer_form = CustomerForm(request.POST, request.FILES)
        if customer_form.is_valid():
            customer_form.save()
            return redirect('view_customers')
    return render(request, 'customer/customer.html',{'customer_form': customer_form})

@login_required
def updateCustomer(request, customer_id):
    customer = get_object_or_404(Customer, pk=customer_id)
    
    customer_form = CustomerForm(instance=customer)
    
    if request.method == 'POST':
        customer_form = CustomerForm(request.POST, request.FILES, instance=customer)
        
        if customer_form.is_valid():
            
            customer_form.save()
            
            return redirect(reverse('update_customer', kwargs={'customer_id': customer_id}))
    
    return render(request, 'customer/customer.html', {'customer_form': customer_form, 'customer': customer})

@login_required
def viewCustomers(request):
    
    customers = Customer.objects.all()
    customers_exist = customers.exists()
    return render(request, 'customer/view_customers.html',{'customers': customers, 'customers_exist': customers_exist})


# Quotation Functions -------------------------------------------------------------------------------------------------------------------
@login_required
def createQuotation(request):
    
    quotation_form = QuotationForm()
    
    # Initialize the QuotationJobFormSet without the queryset parameter.
    QuotationJobFormSet = inlineformset_factory(Quotation, QuotationJob, form=QuotationJobForm, extra=0)

    if request.method == 'POST':
        quotation_form = QuotationForm(request.POST)
        
        # Create an empty formset instance
        job_formset = QuotationJobFormSet()

        if quotation_form.is_valid():
            # Save the quotation
            quotation = quotation_form.save()

            # Loop through job fields and associate them with the quotation
            for key, value in request.POST.items():
                if key.startswith("form-") and key.endswith("-length"):
                    job_index = key.split("-")[1]
                    job_data = {
                        'quotation_id': quotation,
                        'length': request.POST[f"form-{job_index}-length"],
                        'width': request.POST[f"form-{job_index}-width"],
                        'height': request.POST[f"form-{job_index}-height"],
                        'remarks': request.POST[f"form-{job_index}-remarks"],
                        'quantity': request.POST[f"form-{job_index}-quantity"],
                        'attachment': request.FILES.get(f"form-{job_index}-attachment"),
                    }
                    QuotationJob.objects.create(**job_data)
            
            return redirect(reverse('update_quotation', kwargs={'quotation_id': quotation.id}))

    return render(request, 'quotation/quotation.html', {'quotation_form': quotation_form})

@login_required
def updateQuotation(request, quotation_id):
    quotation = get_object_or_404(Quotation, pk=quotation_id)
    
    # Initialize the QuotationJobFormSet without the extra parameter.
    QuotationJobFormSet = inlineformset_factory(Quotation, QuotationJob, form=QuotationJobForm, extra=0)

    if request.method == 'POST':
        quotation_form = QuotationForm(request.POST, instance=quotation)
        job_formset = QuotationJobFormSet(request.POST, request.FILES, instance=quotation)

        if quotation_form.is_valid() and job_formset.is_valid():
            quotation = quotation_form.save()
            
            # Save the job entries using the formset
            job_formset.save()

            # Process the data from dynamically added rows
            for key, value in request.POST.items():
                if key.startswith("form-") and key.endswith("-length"):
                    job_data = {
                        'quotation_id': quotation,
                        'length': request.POST[key],
                        'width': request.POST[key.replace("-length", "-width")],
                        'height': request.POST[key.replace("-length", "-height")],
                        'remarks': request.POST[key.replace("-length", "-remarks")],
                        'quantity': request.POST[key.replace("-length", "-quantity")],
                        'attachment': request.FILES.get(key.replace("-length", "-attachment")),
                    }
                    QuotationJob.objects.create(**job_data)

            return redirect(reverse('update_quotation', kwargs={'quotation_id': quotation_id}))
    else:
        quotation_form = QuotationForm(instance=quotation)
        job_formset = QuotationJobFormSet(instance=quotation)

    return render(request, 'quotation/quotation.html', {'quotation_form': quotation_form, 'job_formset': job_formset, 'quotation': quotation})

@login_required
def viewQuotations(request):
    
    quotations = Quotation.objects.all()
    quotations_exist = quotations.exists()
    return render(request, "quotation/view_quotations.html", {'quotations': quotations, 'quotations_exist': quotations_exist})

@login_required
def deleteQuotation(request, quotation_id):
    
    quotation = Quotation.objects.get(id=quotation_id)
    quotation.delete()
    print(quotation.customer_id.name)
    return redirect('view_quotations')


@login_required
def viewQuotationJobs(request):
    
    quotation_jobs = QuotationJob.objects.all()
    quotation_jobs_exist = quotation_jobs.exists()
    return render(request, "quotation_job/view_quotation_jobs.html", {'quotation_jobs': quotation_jobs, 'quotation_jobs_exist': quotation_jobs_exist})

@login_required
def eachQuotationJob(request, job_id):
    
    quotation_job = get_object_or_404(QuotationJob, pk=job_id)
    
    job_form = QuotationJobForm(instance=quotation_job)
    
    operators = Employee.objects.filter(designation__designation = 'Operator')
    
    if request.method == 'POST':
        job_form = QuotationJobForm(request.POST, request.FILES, instance=quotation_job)
        
        if job_form.is_valid():
            
            job_form.save()
            
            return redirect(reverse('each_quotation_job', kwargs={'job_id': job_id}))
        
    return render(request, 'quotation_job/quotation_job.html', {'job_form': job_form, 'job_id': quotation_job, 'operators': operators})

@login_required
def deleteAttachment(request, job_id):
    quotation_job = get_object_or_404(QuotationJob, pk=job_id)
    
    # Check if the job has an attachment
    if quotation_job.attachment:
        quotation_job.attachment.delete()  # Delete the attachment file
        quotation_job.save()  # Save the changes
    
    return redirect(reverse('each_quotation_job', kwargs={'job_id': job_id}))
    
