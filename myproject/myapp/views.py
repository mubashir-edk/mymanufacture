from django.shortcuts import render, redirect
from django.http import JsonResponse
import json
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
    number_of_employees = len(employees)
    employees_exists = employees.exists()
    return render(request, 'employee/view_employees.html',{'employees': employees, 'employees_exist': employees_exists, 'number_of_employees': number_of_employees})


# HRM Functions -------------------------------------------------------------------------------------------------------------------------
@login_required
def createCompanyPosition(request):
    
    designation_form = DesignationForm()
    if request.method=='POST':
        designation_form = DesignationForm(request.POST)
        if designation_form.is_valid():
            designation_form.save()
            return redirect('view_company_positions')
    return render(request, 'hrm/company_positions/company_positions.html', {'designation_form': designation_form})

@login_required
def viewCompanyPositions(request):
    
    designations = EmployeeDesignation.objects.all().order_by('designation')
    number_of_designations = len(designations)
    designations_exists = designations.exists()
    return render(request, 'hrm/company_positions/company_positions.html',{'designations': designations, 'designations_exists': designations_exists, 'number_of_designations': number_of_designations}) 


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
    number_of_customers = len(customers)
    customers_exist = customers.exists()
    return render(request, 'customer/view_customers.html',{'customers': customers, 'customers_exist': customers_exist, 'number_of_customers': number_of_customers})


# Quotation Functions -------------------------------------------------------------------------------------------------------------------
@login_required
def createQuotation(request):
    
    quotation_form = QuotationForm()
    
    # Initialize the QuotationJobFormSet without the queryset parameter.
    QuotationJobFormSet = inlineformset_factory(Quotation, QuotationJob, form=QuotationJobForm, extra=0)
    
    # Generating Quotation Sequential Code
    quotation_codes = SequentialCode.objects.filter(code_of="quotation")
    for quotation_code in quotation_codes:
        code_prefix = quotation_code.code_prefix
        code_size = quotation_code.code_size
        code_suffix = quotation_code.code_suffix  
    
    codes_only = Quotation.objects.values_list('sequential_code', flat=True)
    
    loop = True
    sequence_number = 1
    
    while loop:
        
        if not code_suffix:
            
            leading_zeros = code_size - len(str(sequence_number))
            
            code = "0" * leading_zeros + str(sequence_number)
            
            quotation_sequence = code_prefix + code
        
            if quotation_sequence in codes_only:
                sequence_number += 1
            else:
                break
            
        if code_suffix:
            
            leading_zeros = code_size - len(str(sequence_number))
            
            code = "0" * leading_zeros + str(sequence_number)
            
            quotation_sequence = code_prefix + code + code_suffix
        
            if quotation_sequence in codes_only:
                sequence_number += 1
            else:
                break

    if request.method == 'POST':
        
        quotation_form = QuotationForm(request.POST)
        
        # Create an empty formset instance
        job_formset = QuotationJobFormSet()

        if quotation_form.is_valid():
            
            # Save the quotation
            quotation = quotation_form.save()
            
            quotation.sequential_code = quotation_sequence
            
            quotation.save()

            # Loop through job fields and associate them with the quotation
            for key, value in request.POST.items():
                
                # Generating QuotationJob Sequential Code
                quotationjob_codes = SequentialCode.objects.filter(code_of="quotation_job")
                for quotationjob_code in quotationjob_codes:
                    job_code_prefix = quotationjob_code.code_prefix
                    job_code_size = quotationjob_code.code_size
                    job_code_suffix = quotationjob_code.code_suffix
              
                job_codes_only = QuotationJob.objects.values_list('sequential_code', flat=True)
                
                job_loop = True
                job_sequence_number = 1
                
                while job_loop:
                    
                    if not job_code_suffix:
                        
                        job_leading_zeros = job_code_size - len(str(job_sequence_number))
                        
                        job_code = "0" * job_leading_zeros + str(job_sequence_number)
                        
                        job_sequence = job_code_prefix + job_code
                    
                        if job_sequence in job_codes_only:
                            job_sequence_number += 1
                        else:
                            break
                        
                    if job_code_suffix:
                        
                        job_leading_zeros = job_code_size - len(str(job_sequence_number))
                        
                        job_code = "0" * job_leading_zeros + str(job_sequence_number)
                        
                        job_sequence = job_code_prefix + job_code + job_code_suffix
                    
                        if job_sequence in job_codes_only:
                            job_sequence_number += 1
                        else:
                            break
                
                #Saving each Job Data
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
                    QuotationJob.objects.create(**job_data, sequential_code=job_sequence)
                    
            
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
    
    draft_quotation = len(Quotation.objects.filter(status = 'draft'))
    in_process_quotation = len(Quotation.objects.filter(status = 'in_process'))
    ready_to_deliver_quotation = len(Quotation.objects.filter(status = 'ready_to_deliver'))
    
    quotations_exist = quotations.exists()
    return render(request, "quotation/view_quotations.html", {'quotations': quotations, 'quotations_exist': quotations_exist, 'draft_quotation': draft_quotation, 'in_process_quotation': in_process_quotation, 'ready_to_deliver_quotation': ready_to_deliver_quotation})

@login_required
def deleteQuotation(request, quotation_id):
    
    quotation = Quotation.objects.get(id=quotation_id)
    quotation.delete()
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
    
    job_task = Task.objects.filter(job_id=job_id).first()
    
    job_operator = JobAssign.objects.filter(job_id=job_id).first()
    
    if request.method == 'POST':
        job_form = QuotationJobForm(request.POST, request.FILES, instance=quotation_job)
        
        if job_form.is_valid():
            
            job_form.save()
            
        return redirect(reverse('each_quotation_job', kwargs={'job_id': job_id}))
        
    return render(request, 'quotation_job/quotation_job.html', {'job_form': job_form, 'job_id': quotation_job, 'job_task': job_task, 'job_operator': job_operator})

@login_required
def deleteAttachment(request, job_id):
    quotation_job = get_object_or_404(QuotationJob, pk=job_id)
    
    # Check if the job has an attachment
    if quotation_job.attachment:
        quotation_job.attachment.delete()  # Delete the attachment file
        quotation_job.save()  # Save the changes
    
    return redirect(reverse('each_quotation_job', kwargs={'job_id': job_id}))


# JobAssign Functions -------------------------------------------------------------------------------------------------------------------
@login_required
def jobAssigning(request):
        
    employees_to_assign = Employee.objects.filter(designation__designation = "Operator")
    
    employees_data = [{'id': employee.id, 'name': employee.name} for employee in employees_to_assign]
    
    if request.method == "GET":
        
        json_data = {'employees_to_assign': employees_data}
        return  JsonResponse(json_data)
    
    if request.method == 'POST':
        
        try:

            # Parse the JSON data from the request
            data = json.loads(request.body.decode('utf-8'))

            selected_employee_id = data.get('employee_id')
            job_id = data.get('job_id')

            # Retrieve the Employee and Job objects
            selected_employee = get_object_or_404(Employee, id=selected_employee_id)
            job = get_object_or_404(QuotationJob, id=job_id)

            # Create a new JobAssign instance with the associated Employee and Job
            job_assignment = JobAssign(employee_id=selected_employee, job_id=job)
            job_assignment.save()
            
            # Generating Task Sequential Code
            task_codes = SequentialCode.objects.filter(code_of="task")
            for task_code in task_codes:
                task_code_prefix = task_code.code_prefix
                task_code_size = task_code.code_size
                task_code_suffix = task_code.code_suffix
                
                print(f"{task_code} is Already there")
            
            task_codes_only = Task.objects.values_list('sequential_code', flat=True)
            
            task_loop = True
            task_sequence_number = 1
            
            while task_loop:
                
                if not task_code_suffix:
                    
                    task_leading_zeros = task_code_size - len(str(task_sequence_number))
                    
                    task_code = "0" * task_leading_zeros + str(task_sequence_number)
                    
                    task_sequence = task_code_prefix + task_code
                
                    if task_sequence in task_codes_only:
                        task_sequence_number += 1
                    else:
                        break
                    
                if task_code_suffix:
                    
                    task_leading_zeros = task_code_size - len(str(task_sequence_number))
                    
                    task_code = "0" * task_leading_zeros + str(task_sequence_number)
                    
                    task_sequence = task_code_prefix + task_code + task_code_suffix
                
                    if task_sequence in task_codes_only:
                        task_sequence_number += 1
                    else:
                        break
            
            # After assigning job create task corresponding to the job with employee
            print(task_sequence)
            task_create = Task(job_id=job, operator_id=selected_employee, sequential_code=task_sequence)
            task_create.save()
        

            redirect_url = reverse('each_quotation_job', kwargs={'job_id': job.id})
            return JsonResponse({'redirect_url': redirect_url})

        except json.JSONDecodeError as e:
            return JsonResponse({'error': 'Invalid JSON data'}, status=400)
            
    return JsonResponse({'error': 'Form is not valid'})

@login_required
def unAssignJob(request, job_task_id):
    
    unassign_job_task = Task.objects.get(id=job_task_id)
    unassign_job_operator = JobAssign.objects.get(job_id=unassign_job_task.job_id)
    unassign_job_operator.delete()
    unassign_job_task.delete()
    return redirect('view_tasks')


# SequentialCode Functions --------------------------------------------------------------------------------------------------------------
@login_required
def sequentialCode(request):
    
    quotation_code = SequentialCode.objects.filter(code_of="quotation").first()
    quotation_job_code = SequentialCode.objects.filter(code_of="quotation_job").first()
    task_code = SequentialCode.objects.filter(code_of="task").first()
    
    quotation_code_object = get_object_or_404(SequentialCode, pk=quotation_code.id)
    quotation_job_code_object = get_object_or_404(SequentialCode, pk=quotation_job_code.id)
    task_code_object = get_object_or_404(SequentialCode, pk=task_code.id)
    
    quotation_code_form = QuotationSequentialCodeForm(instance=quotation_code_object)
    quotationjob_code_form = QuotationJobSequentialCodeForm(instance=quotation_job_code_object)
    task_code_form = TaskSequentialCodeForm(instance=task_code_object)
    
    # Getting data from html via ajax
    if request.method == 'POST':
    
        try:
            # Parse the JSON data from the request
            data = json.loads(request.body.decode('utf-8'))

            quotation_prefix = data.get('quotation_prefix')
            quotation_size = data.get('quotation_size')
            quotation_suffix = data.get('quotation_suffix')
            
            # Updating Quotation Sequential Code
            quotation_code_object.code_prefix = quotation_prefix
            quotation_code_object.code_size = quotation_size
            quotation_code_object.code_suffix = quotation_suffix
            quotation_code_object.save()
            
            quotation_job_prefix = data.get('quotation_job_prefix')
            quotation_job_size = data.get('quotation_job_size')
            quotation_job_suffix = data.get('quotation_job_suffix')

            # Updating QuotationJob Sequential Code
            quotation_job_code_object.code_prefix = quotation_job_prefix
            quotation_job_code_object.code_size = quotation_job_size
            quotation_job_code_object.code_suffix = quotation_job_suffix
            quotation_job_code_object.save()
            
            task_prefix = data.get('task_prefix')
            task_size = data.get('task_size')
            task_suffix = data.get('task_suffix')
            
            # Updating QuotationJob Sequential Code
            task_code_object.code_prefix = task_prefix
            task_code_object.code_size = task_size
            task_code_object.code_suffix = task_suffix
            task_code_object.save()

            redirect_url = reverse('sequential_code')
            return JsonResponse({'redirect_url': redirect_url})

        except json.JSONDecodeError as e:
            return JsonResponse({'error': 'Invalid JSON data'}, status=400)
    
    context = {
        'quotation_code_form': quotation_code_form,
        'quotationjob_code_form': quotationjob_code_form,
        'task_code_form': task_code_form,
        'quotation_code': quotation_code,
        'quotation_job_code': quotation_job_code,
        'task_code': task_code
    }
    return render(request, 'sequential_code/sequential_code.html', context)


# Task Functions ------------------------------------------------------------------------------------------------------------------
@login_required
def viewTasks(request):
    
    # Getting Tasks from db
    tasks = Task.objects.all()
    tasks_exist = tasks.exists()
    number_of_tasks = tasks.count()

    return render(request, 'task/view_tasks.html', {'tasks': tasks, 'tasks_exist': tasks_exist, 'number_of_tasks': number_of_tasks})


# Machine Functions ---------------------------------------------------------------------------------------------------------------------
@login_required
def machineSettings(request):
    
    machine_form = MachineForm()
    
    if request.method == 'POST':
        
        machine_form = MachineForm(request.POST)
        
        if machine_form.is_valid():
            
            machine_form.save()
            return redirect('machines')
        
    return render(request)