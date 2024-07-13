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

        if User.objects.filter(username=username).exists() or UserModel.objects.filter(email=email).exists():
            messages.error(request, "User already exists... Try a different username or email")
            return redirect('signup')
        else:
            user = UserModel.objects.create_user(
                full_name =full_name, username =username, email=email, password=password
            )
            user.save()
    
    if request.user.is_authenticated:
        return redirect('app:dashboard')

    return render(request, 'signup.html')

def login(request):
    if request.method == 'POST':
        username = request.POST["username"]
        password = request.POST['password']
        credentials = (username or password)
        
        if not credentials:
            user = authenticate(request, username=username, password=password)

        if user is not None:
            login(user)
            return redirect("app:dashboard")
        else:
            messages.error(request, 'Invalid Credentials')
            return('users:login')
        
    if request.user.is_authenticated:
        return redirect('app:dashboard')
    
    return render(request, 'signin.html')

def logout(request):
    None