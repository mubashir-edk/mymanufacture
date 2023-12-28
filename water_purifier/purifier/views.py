from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from .models import *
from .forms import *
from django.urls import reverse
from django.shortcuts import get_object_or_404

# Create your views here.

def index(request):
    return render(request, 'index.html')


# Employee Functions --------------------------------------------------------------------------------------------------------------------------------
def createEmployee(request):
    
    employee_form = EmployeeForm()
    
    if request.method == 'POST':
        
        print("Inside POST Submission")
        print(request.POST)

        employee_form = EmployeeForm(request.POST, request.FILES)
        
        # Generating Employee Code
        employee_codes_only = Employee.objects.values_list('employee_code', flat=True)
        
        max_employee_code = ''
        
        if employee_codes_only.exists():
            max_employee_code = max(employee_codes_only)
            print(max_employee_code)
            
        print(employee_codes_only)
        
        employee_code_loop = True
        employee_code_number = 1
        
        while employee_code_loop:

            employee_code_leading_zeros = 5 - len(str(employee_code_number))
            
            employee_code = "0" * employee_code_leading_zeros + str(employee_code_number)
            
            generated_employee_code = "EMP_" + employee_code
        
            if generated_employee_code in employee_codes_only or generated_employee_code < max_employee_code:
                employee_code_number += 1
            else:
                break
        
        if employee_form.is_valid():
            
            print("Inside validating")
            
            employee = employee_form.save(commit=False)
            employee.employee_code = generated_employee_code
            employee.save()
            return redirect('purifier:view_employees')
    
    context = {'employee_form': employee_form}
            
    return render(request, 'employee/employee.html', context)

def viewEmployees(request):
    
    employees = Employee.objects.all()
    print(employees)
    employees_exists = employees.exists()
    
    context = {'employees': employees, 'employees_exists': employees_exists}
    
    return render(request, 'employee/view_employees.html', context)

def eachEmployee(request, id):
    
    employee = get_object_or_404(Employee, pk=id)
    
    print(employee.id)
    
    context = {'employee': employee}
    
    return render(request, 'employee/each_employee.html', context)

def updateEmployee(request, id):
    
    employee = get_object_or_404(Employee, pk=id)
    
    employee_form = EmployeeForm(instance=employee)
    
    employee_code_stored = employee.employee_code

    if request.method == 'POST':
        
        employee_form = EmployeeForm(request.POST, request.FILES, instance=employee)
        
        if employee_form.is_valid():
            
            employee_save = employee_form.save(commit=False)
            
            employee_save.employee_code = employee_code_stored
            
            employee_save.save()
            
            return redirect(reverse('purifier:each_employee', kwargs={'id': employee.id}))
        
    context = {'employee_form': employee_form, 'employee': employee}
        
    return render(request, 'employee/employee.html', context)

def deleteEmployee(request, id):
    
    employee = get_object_or_404(Employee, pk=id)
    employee.delete()
    return redirect('purifier:view_employees')

# Customer Functions --------------------------------------------------------------------------------------------------------------------------------
def createCustomer(request):
    
    customer_form = CustomerForm()
    
    if request.method == 'POST':
        
        customer_form = CustomerForm(request.POST, request.FILES)
        
        # Generating Customer Code
        customer_codes_only = Customer.objects.values_list('customer_code', flat=True)
        
        max_customer_code = ''
        
        if customer_codes_only.exists():
            max_customer_code = max(customer_codes_only)
            print(max_customer_code)
            
        print(customer_codes_only)
        
        customer_code_loop = True
        customer_code_number = 1
        
        while customer_code_loop:

            customer_code_leading_zeros = 5 - len(str(customer_code_number))
            
            customer_code = "0" * customer_code_leading_zeros + str(customer_code_number)
            
            generated_customer_code = "CUS_" + customer_code
        
            if generated_customer_code in customer_codes_only or generated_customer_code < max_customer_code:
                customer_code_number += 1
            else:
                break
            
        if customer_form.is_valid():
            
            print(request.POST.get('installed_product'))
            print(request.POST.getlist('installed_product'))
            # print(request.POST)
            
            customer = customer_form.save(commit=False)
            customer.customer_code = generated_customer_code

            customer.save()
            
            return redirect('purifier:view_customers')
        
    context = {'customer_form': customer_form}
            
    return render(request, 'customer/customer.html', context)

def viewCustomers(request):
    
    customers = Customer.objects.all()
    customers_exists = customers.exists()
    
    context = {'customers': customers, 'customers_exists': customers_exists}
    
    return render(request, 'customer/view_customers.html', context)

def eachCustomer(request , id):
    
    customer = get_object_or_404(Customer, pk=id)
    context = {'customer': customer}
    return render(request, 'customer/each_customer.html', context)

def updateCustomer(request , id):
    
    customer = get_object_or_404(Customer, pk=id)
    
    customer_form = CustomerForm(instance=customer)
    
    customer_code_stored = customer.customer_code
    
    if request.method == 'POST':
        
        customer_form = CustomerForm(request.POST, request.FILES, instance=customer)
        
        if customer_form.is_valid():
            
            customer_save = customer_form.save(commit=False)
            customer_save.customer_code = customer_code_stored
            customer_save.save() 
            
            return redirect(reverse('purifier:each_customer', kwargs={'id': customer.id}))
        
    context = {'customer_form': customer_form, 'customer': customer}
    
    return render(request, 'customer/customer.html', context)

def deleteCustomer(request, id):
    
    customer = get_object_or_404(Customer, pk=id)
    customer.delete()
    return redirect('purifier:view_customers')


# Product Functions ---------------------------------------------------------------------------------------------------------------------------------
def viewCategories(request):
    
    categories = Category.objects.all()
    
    categories_exists = categories.exists()
    
    category_form = CategoryForm()
    
    context = {'categories': categories, 'categories_exists': categories_exists, 'category_form': category_form}
    
    return render(request, 'product/category.html', context)

def createCategory(request):
    
    if request.method == 'POST':
        
        category_form = CategoryForm(request.POST, request.FILES)
        
        if category_form.is_valid():
            
            category_form.save()
            
        return redirect('purifier:view_categories')

def updateCategory(request, id):
    
    category = get_object_or_404(Category, pk=id)
    
    category_form = CategoryForm(instance=category)
    
    if request.method == 'GET':
        
        print(category)
        
        if category.image:
            category_data = {
            'image': category.image.url,
            'name': category.name,
            }
        else:
            category_data = {
            'name': category.name,
            }
            

        return JsonResponse({'category': category_data})
    
    if request.method == 'POST':
        
        category_form = CategoryForm(request.POST, request.FILES, instance=category)
        
        if category_form.is_valid():
            
            category_form.save()
            
            return redirect('purifier:view_categories')
        
    context = {'category': category, 'category_form': category_form}
        
    return render(request, 'product/category_update_modal.html',context)

def deleteCategory(request, id):
    
    category = get_object_or_404(Category, pk=id)
    category.delete()
    return redirect('purifier:view_categories')

def createProduct(request):
    
    if request.method == 'POST':
        
        product_form = ProductForm(request.POST, request.FILES)
        
        if product_form.is_valid():
            
            product_form.save()
            
            return redirect('purifier:view_products')   
    
    return render(request, 'product/product.html')

def viewProducts(request):
    
    category_form = CategoryForm()
    
    product_form = ProductForm()
    
    products = Product.objects.all()
    
    products_exists = products.exists()
    
    context = {'category_form': category_form, 'product_form': product_form, 'products': products, 'products_exists': products_exists}
    
    return render(request, 'product/product.html', context)


# Service Functions --------------------------------------------------------------------------------------------------------------------------------
def viewAndCreateServices(request):
    
    services = Service.objects.all()
    services_exists = services.exists()
    
    service_form = ServiceForm()
    
    if request.method == 'POST':
        
        service_form = ServiceForm(request.POST)
        
        if service_form.is_valid():
            
            service_form.save()
            
            return redirect('purifier:view_services')
    
    context = {'services': services, 'services_exists': services_exists, 'service_form': service_form}
    return render(request, 'service/view_services.html', context)

def deleteService(request, id):
    
    print(id)
    service = get_object_or_404(Service, pk=id)
    print(service)
    service.delete()
    return redirect('purifier:view_services')

# def updateService(request, id):
    
#     service = get_object_or_404(Service, pk=id)
    
#     service_form = ServiceForm(instance=service)
    
#     if request.method == 'POST':
        
#         service_form = ServiceForm(request.POST, instance=service)
        
#         if service_form.is_valid():
            
#             service_form.save()
            
#             return redirect('purifier:view_services')
        
#     context = {'service_form': service_form,  'service_id': service}
    
#     return render(request, 'service/view_services.html', context)


# Servicer Functions --------------------------------------------------------------------------------------------------------------------------------
def viewServicers(request):
    
    servicers = Servicer.objects.all()
    
    servicers_exists = servicers.exists()
    
    servicer_form = ServicerForm()
    
    context = {'servicers': servicers, 'servicers_exists': servicers_exists, 'servicer_form': servicer_form}
    
    return render(request, 'servicer/view_servicers.html', context)

def createServicer(request):
    
    if request.method == 'POST':
        
        servicer_form = ServicerForm(request.POST)
        
        if servicer_form.is_valid():
            
            servicer_form.save()
            
            return redirect('purifier:view_servicers')
        
    return render(request, 'servicer/view_servicers.html')

def fetchServicer(request, selected_employee):
    
    print("Fetching")
    
    if request.method == 'GET':
    
        try:
            employee = Employee.objects.get(pk=selected_employee)
            data = {'employee': {
                'employee_code': employee.employee_code,
                'mobile': employee.mobile,
                # Add other fields as needed
            }}
            print(employee)
            return JsonResponse(data)
        except Employee.DoesNotExist:
            return JsonResponse({'error': 'Employee not found'}, status=404)
        

# Service Work Functions ----------------------------------------------------------------------------------------------------------------------------
def viewServiceWorks(request):
    
    service_works = ServiceWork.objects.all()
    
    service_works_exists = service_works.exists()
    
    service_work_form = ServiceWorkForm()
    
    
    if request.method == 'GET':
        
        selected_customer = request.GET.get('selectedCustomer')
        
        selected_product = request.GET.get('selectedProduct')
        
        print(selected_customer)
        
        if selected_customer:
    
            try:
                
                # selected_customer = request.GET.get('selectedCustomer')
                    
                customer = get_object_or_404(Customer, pk=selected_customer)
                installed_products = customer.installed_product.all()

                products = Product.objects.filter(id__in=installed_products)
                
                products_data = [{'id': product.id, 'name': product.name} for product in products]
                
                print(products)
                print('----------------------------------------------')
                print(products_data)
                
                data = {
                    'products': products_data,
                }
                return JsonResponse(data)
            except Customer.DoesNotExist:
                return JsonResponse({'error': 'Customer not found'}, status=404)
            
            
        if selected_product:
            
            try:
                
                # selected_product = request.GET.get('selected
                
                product = get_object_or_404(Product, pk=selected_product)
                product_services = product.services.all()
                
                services = Service.objects.filter(id__in=product_services)
                
                services_data = [{'id': service.id, 'name': service.name} for service in services]
                
                print(services)
                print('----------------------------------------------')
                print(services_data)
                
                data = {
                    'services': services_data,
                }
                
                return JsonResponse(data)
            except Product.DoesNotExist:
                return JsonResponse({'error': 'Product not found'}, status=404)
                
        
    
    context = {'service_works': service_works, 'service_works_exists': service_works_exists, 'service_work_form': service_work_form}
    
    return render(request, 'servicework/view_serviceworks.html', context)

def createServiceWork(request):
    
    if request.method == 'POST':
        
        service_work_form = ServiceWorkForm(request.POST)
        
        # Generating Service Work Code
        servicework_codes_only = ServiceWork.objects.values_list('service_work_code', flat=True)
        
        max_servicework_code = ''
        
        if servicework_codes_only.exists():
            max_servicework_code = max(servicework_codes_only)
            print(max_servicework_code)
            
        print(servicework_codes_only)
        
        servicework_code_loop = True
        servicework_code_number = 1
        
        while servicework_code_loop:

            servicework_code_leading_zeros = 5 - len(str(servicework_code_number))
            
            servicework_code = "0" * servicework_code_leading_zeros + str(servicework_code_number)
            
            generated_servicework_code = "SR_" + servicework_code
        
            if generated_servicework_code in servicework_codes_only or generated_servicework_code < max_servicework_code:
                servicework_code_number += 1
            else:
                break
        
        if service_work_form.is_valid():
            
            servicework = service_work_form.save(commit=False)
            
            servicework.service_work_code = generated_servicework_code
            
            servicework.save()
            
            return redirect('purifier:view_serviceworks')
    
# Test or Quality check Functions -------------------------------------------------------------------------------------------------------------------
def viewTests(request):
    
    tests = Test.objects.all()
    
    tests_exists = tests.exists()
    
    context = {'tests': tests, 'tests_exists': tests_exists}
    
    return render(request, 'test/view_tests.html', context)

def createTest(request):
    
    test_form = TestForm()
    
    if request.method == 'POST':
        
        test_form = TestForm(request.POST)
        
        if test_form.is_valid():
            
            test_form.save()
            
            return redirect('purifier:view_tests')
        
    context = {'test_form': test_form}
        
    return render(request, 'test/test.html', context)