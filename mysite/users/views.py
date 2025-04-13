from django.shortcuts import render,redirect
#from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import RegisterForm
from django.contrib.auth import logout

# Create your views here.

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request,f'Hello {username} Your Account Has Been Successfully Created...')
            return redirect('login')
            
    else:        
        form = RegisterForm()
    return render(request,'users/register.html',{'form':form} ) 

def MyLogOut(request):
    logout(request)
    return render(request, 'users/logout.html')

@login_required
def profilepage(request):
    return render(request, 'users/profile.html')
