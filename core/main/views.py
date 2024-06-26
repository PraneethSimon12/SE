from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login , logout
from django.contrib.auth.decorators import login_required

# Create your views here.

def index_page(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        remember = request.POST.get('remember')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            # Redirect to a success page or homepage
            return redirect('home')
        else:
            # Return an invalid login error message
            return render(request, 'index.html', {'error': 'Invalid username or password'})
    else:
        return render(request, 'index.html')

def register_page(request):
    if request.method == 'POST':
        first_name = request.POST['firstname']
        last_name = request.POST['lastname']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
        
        # Check if passwords match
        if password != confirm_password:
            return render(request, 'register.html', {'error': 'Passwords do not match'})
        
        # Create user
        user = User.objects.create_user(username=email, email=email, password=password, first_name=first_name, last_name=last_name)
        user.save()
        messages.info(request,'Account created successfully')
        # You may add additional logic here like redirecting to a login page or rendering a success page
        return redirect('index')  # Redirect to login page after successful signup
    else:
        return render(request, 'register.html')

@login_required(login_url="/index/")
def home_page(request):
    return render(request,'home.html')

@login_required(login_url="/index/")
def language_page(request):
    return render(request,'languages.html')

@login_required(login_url="/index/")
def text_page(request):
    return render(request,'text.html')

@login_required(login_url="/index/")
def t_s(request):
    return render(request,'t_s.html')