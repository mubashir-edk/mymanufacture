from django.shortcuts import render,redirect
from customuser.forms import UserForm, LoginForm
from customuser.backends import CustomUserBackend
from django.contrib.auth import login as login_custom_user, logout as logout_user
from django.contrib.auth.decorators import login_required


# Create your views here.

def create_user(request):
    form = UserForm()
    if request.method=='POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
    return render(request, 'create_user.html',{"form": form})


def login(request):
    form = LoginForm()
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = CustomUserBackend().authenticate(request, username=username, password=password)
        if user is not None:
            login_custom_user(request, user)
            return redirect('dashboard')
        else:
            return render(request, 'login.html', {'error': 'Invalid login credentials. Please try again.'})
    return render(request, 'login.html',{'form':form })


@login_required
def dashboard(request):
    return render(request,'index.html')

def logout(request):
    logout_user(request)
    return redirect(login)