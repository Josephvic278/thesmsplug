from django.shortcuts import render, redirect
from users.models import UserModel
from django.contrib import messages
from django.contrib.auth import authenticate, login

# Create your views here.
def signup(request):
    if request.method == 'POST':
        full_name = request.POST['full_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POSt['password']

        if UserModel.objects.filter(username=username).exists() or UserModel.objects.filter(email=email).exists():
            messages.error(request, "User already exists... Try a different username or email")
            return redirect('signup')
        else:
            user = UserModel.objects.create(
                full_name =full_name, username =username, email=email, password=password
            )
            user.save()
    
    if request.user.is_authenticated:
        return redirect('app:dashboard')

    return render(request, 'signup.html')

def login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']

        user = authenticate(request, email=email, password=password)

        if user is not None:
            login(user)
        
        else:
            messages.error(request, 'Invalid Credentials')
            return('login')
        
    if request.user.is_authenticated:
        return redirect('app:dashboard')
    
    return render(request, 'signin.html')

def logout(request):
    None