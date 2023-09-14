from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.shortcuts import get_object_or_404
from myapp.models import *
from myapp.forms import *
from django.contrib import messages

# Create your views here.

def home(request):
    return render(request, 'home.html')

def createCustomer(request):
    
    form = CustomerForm()
    if request.method=='POST':
        form = CustomerForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('view_customers')
    return render(request, 'customer/customer.html',{"form": form})

def viewCustomers(request):
    
    customers = Customer.objects.all()
    return render(request, 'customer/view_customers.html',{'customers': customers})


def createQuotation(request):
    quotation_form = QuotationForm()
    job_formset = QuotationJobFormSet(queryset=QuotationJob.objects.none())
    
    if request.method == 'POST':
        quotation_form = QuotationForm(request.POST)
        job_formset = QuotationJobFormSet(request.POST, request.FILES)

        if quotation_form.is_valid() and job_formset.is_valid():
            quotation = quotation_form.save()
            
            # Loop through job fields and associate them with the quotation
            for key, value in request.POST.items():
                if key.startswith("form-") and key.endswith("-length"):
                    job_index = key.split("-")[1]
                    job = QuotationJob(
                        quotation_id=quotation,
                        length=request.POST[f"form-{job_index}-length"],
                        width=request.POST[f"form-{job_index}-width"],
                        height=request.POST[f"form-{job_index}-height"],
                        remarks=request.POST[f"form-{job_index}-remarks"],
                        quantity=request.POST[f"form-{job_index}-quantity"],
                        attachment=request.FILES.get(f"form-{job_index}-attachment"),
                    )
                    job.save()
            
            return redirect('view_quotations')

    return render(request, 'quotation/quotation.html', {'quotation_form': quotation_form, 'job_formset': job_formset})

def updateQuotation(request, quotation_id):
    quotation = get_object_or_404(Quotation, pk=quotation_id)
    print(quotation_id)
    print(quotation.id)
    quotation_form = QuotationForm(instance=quotation)
    job_formset = QuotationJobFormSet(queryset=QuotationJob.objects.filter(quotation_id=quotation))
    
    if request.method == 'POST':
        print(request.POST)
        quotation_form = QuotationForm(request.POST, instance=quotation)
        job_formset = QuotationJobFormSet(request.POST, request.FILES, queryset=QuotationJob.objects.filter(quotation_id=quotation))
        print("Before form validation")
        if quotation_form.is_valid() and job_formset.is_valid():
            print("Inside form validation")
            quotation = quotation_form.save()
            
            # Loop through job fields and update them
            # for job_form in job_formset:
                
            #     job = job_form.save(commit=False)
            #     job.quotation_id = quotation
            #     job.save()
            for key, value in request.POST.items():
                if key.startswith("form-") and key.endswith("-length"):
                    job_index = key.split("-")[1]
                    job = QuotationJob(
                        quotation_id=quotation,
                        length=request.POST[f"form-{job_index}-length"],
                        width=request.POST[f"form-{job_index}-width"],
                        height=request.POST[f"form-{job_index}-height"],
                        remarks=request.POST[f"form-{job_index}-remarks"],
                        quantity=request.POST[f"form-{job_index}-quantity"],
                        attachment=request.FILES.get(f"form-{job_index}-attachment"),
                    )
                    job.save()
            
            return redirect('view_quotations')
        
        print("After form validation")

    return render(request, 'quotation/quotation.html', {'quotation_form': quotation_form, 'job_formset': job_formset, 'quotation': quotation})


def viewQuotations(request):
    
    quotations = Quotation.objects.all()
    return render(request, "quotation/view_quotations.html", {'quotations': quotations})



    
