from django.shortcuts import render , redirect
from django.contrib.auth.models import User 
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from core.models import Profile
from django.contrib.auth.decorators import login_required


# Create your views here.

@login_required(login_url='signin.html')
def index(request):
    return render(request, 'index.html')



# def signup(request):
#     if request.method == 'POST':
#     return render(request, 'signup.html')



def signup(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        username = request.POST['username']
        password = request.POST['password']
        password2 = request.POST['password2']
        
        
        if password ==  password2:
            if User.objects.filter(username=username).exists():
                messages.error(request, 'username already exists')
                return redirect('signup')

            else:
                if User.objects.filter(email=email).exists():
                    messages.error(request, 'email already exists')
                    return redirect('signup')

                else:
                    form = User.objects.create_user(first_name=first_name, last_name=last_name, email=email, username=username, password=password)
                    form.save()

                    user_model = User.objects.get(username=username)
                    new_profile = Profile.objects.create(user=user_model,id_user=user_model.id)
                    new_profile.save()
                    messages.success(request, 'Account created successfully')
                    return redirect('signin')


        else:
            messages.error(request, 'password does not exist')
            return redirect('signup')

    return render(request,'signup.html') 




def signin(request):
    
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']


        user = authenticate(username=username, password=password)
        if user is not None:
          login(request,user)
          messages.success(request, 'login successful')
          return redirect('setting')
    else:
        messages.info(request, 'invalid login')

    return render(request, 'signin.html')


@login_required(login_url='signin.html')
def profile(request):
    return render(request, 'profile.html')


def setting(request):
    return render(request, 'setting.html')
