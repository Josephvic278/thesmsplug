from django.shortcuts import render, redirect
from users.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login

# Create your views here.
def signup(request):
    if request.method == 'POST':
        full_name = request.POST['full_name']
        username = request.POST['username']
        phone_number = request.POST["phone_number"]
        email = request.POST['email']
        password = request.POST['password']

        if User.objects.filter(username=username).exists() or User.objects.filter(email=email).exists():
            messages.error(request, "User already exists... Try a different username or email")
            return redirect('signup')
        else:
            user = User.objects.create_user(
                full_name =full_name, username =username, email=email, password=password
            )
            user.save()
            return redirect("app:dashboard")
    
    if request.user.is_authenticated:
        return redirect('app:dashboard')

    return render(request, 'signup.html')

def login_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            return redirect("app:dashboard")
        else:
            messages.error(request, 'Invalid Credentials')
            return redirect('users:login')
        
    if request.user.is_authenticated:
        return redirect('app:dashboard')
    
    return render(request, 'signin.html')

def logout(request):
    None