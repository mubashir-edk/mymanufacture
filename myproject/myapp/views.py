from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.shortcuts import get_object_or_404
from myapp.models import *
from myapp.forms import *
from django.urls import reverse
from django.contrib import messages
from django.forms import inlineformset_factory
# Create your views here.

def home(request):
    return render(request, 'home.html')

def createCustomer(request):
    
    customer_form = CustomerForm()
    if request.method=='POST':
        form = CustomerForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('view_customers')
    return render(request, 'customer/customer.html',{'customer_form': customer_form})

def updateCustomer(request, customer_id):
    customer = get_object_or_404(Customer, pk=customer_id)
    
    customer_form = CustomerForm(instance=customer)
    
    if request.method == 'POST':
        customer_form = CustomerForm(request.POST, request.FILES, instance=customer)
        
        if customer_form.is_valid():
            
            customer_form.save()
            
            return redirect(reverse('update_customer', kwargs={'customer_id': customer_id}))
    
    return render(request, 'customer/customer.html', {'customer_form': customer_form, 'customer': customer})

def viewCustomers(request):
    
    customers = Customer.objects.all()
    customers_exist = customers.exists()
    return render(request, 'customer/view_customers.html',{'customers': customers, 'customers_exist': customers_exist})


# def createQuotation(request):
#     quotation_form = QuotationForm()
#     job_formset = QuotationJobFormSet(queryset=QuotationJob.objects.none())
    
#     if request.method == 'POST':
#         quotation_form = QuotationForm(request.POST)
#         job_formset = QuotationJobFormSet(request.POST, request.FILES)

#         if quotation_form.is_valid() and job_formset.is_valid():
#             quotation = quotation_form.save()
            
#             # Loop through job fields and associate them with the quotation
#             for key, value in request.POST.items():
#                 if key.startswith("form-") and key.endswith("-length"):
#                     job_index = key.split("-")[1]
#                     job = QuotationJob(
#                         quotation_id=quotation,
#                         length=request.POST[f"form-{job_index}-length"],
#                         width=request.POST[f"form-{job_index}-width"],
#                         height=request.POST[f"form-{job_index}-height"],
#                         remarks=request.POST[f"form-{job_index}-remarks"],
#                         quantity=request.POST[f"form-{job_index}-quantity"],
#                         attachment=request.FILES.get(f"form-{job_index}-attachment"),
#                     )
#                     job.save()
            
            
            
#             return redirect(reverse('update_quotation', kwargs={'quotation_id': quotation.id}))

#     return render(request, 'quotation/quotation.html', {'quotation_form': quotation_form, 'job_formset': job_formset})


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

# def updateQuotation(request, quotation_id):
#     quotation = get_object_or_404(Quotation, pk=quotation_id)

#     quotation_form = QuotationForm(instance=quotation)
#     job_formset = QuotationJobFormSet(queryset=QuotationJob.objects.filter(quotation_id=quotation))
    
#     if request.method == 'POST':
        
#         quotation_form = QuotationForm(request.POST, instance=quotation)
#         job_formset = QuotationJobFormSet(request.POST, request.FILES, queryset=QuotationJob.objects.filter(quotation_id=quotation))
        
#         if quotation_form.is_valid() and job_formset.is_valid():
            
#             quotation = quotation_form.save()
            
#             for job_index, job_form in enumerate(job_formset):
#                 if job_form.has_changed():
#                     job = job_formset[job_index]
#                     job.length = job_form.cleaned_data['length']
#                     job.width = job_form.cleaned_data['width']
#                     job.height = job_form.cleaned_data['height']
#                     job.remarks = job_form.cleaned_data['remarks']
#                     job.quantity = job_form.cleaned_data['quantity']
#                     if 'attachment' in job_form.changed_data:
#                         job.attachment = job_form.cleaned_data['attachment']
#                     job.save()

#             return redirect(reverse('update_quotation', kwargs={'quotation_id': quotation_id}))

#     return render(request, 'quotation/quotation.html', {'quotation_form': quotation_form, 'job_formset': job_formset, 'quotation': quotation})


# def updateQuotation(request, quotation_id):
#     quotation = get_object_or_404(Quotation, pk=quotation_id)
#     QuotationJobFormSet = inlineformset_factory(Quotation, QuotationJob, form=QuotationJobForm, extra=1)

#     if request.method == 'POST':
#         quotation_form = QuotationForm(request.POST, instance=quotation)
#         job_formset = QuotationJobFormSet(request.POST, request.FILES, instance=quotation)

#         if quotation_form.is_valid() and job_formset.is_valid():
#             quotation = quotation_form.save()

#             # Save the job entries using the formset
#             job_formset.save()

#             return redirect(reverse('update_quotation', kwargs={'quotation_id': quotation_id}))
#     else:
#         quotation_form = QuotationForm(instance=quotation)
#         job_formset = QuotationJobFormSet(instance=quotation)

#     return render(request, 'quotation/quotation.html', {'quotation_form': quotation_form, 'job_formset': job_formset, 'quotation': quotation})


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


def viewQuotations(request):
    
    quotations = Quotation.objects.all()
    quotations_exist = quotations.exists()
    return render(request, "quotation/view_quotations.html", {'quotations': quotations, 'quotations_exist': quotations_exist})


def viewQuotationJobs(request):
    
    quotation_jobs = QuotationJob.objects.all()
    quotation_jobs_exist = quotation_jobs.exists()
    return render(request, "quotation_job/view_quotation_jobs.html", {'quotation_jobs': quotation_jobs, 'quotation_jobs_exist': quotation_jobs_exist})



    
