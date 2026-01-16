from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm 
from django.contrib import messages
from .forms import userRegisterForm
from django.contrib.auth.decorators import login_required

def register(request):
    if request.method=='POST':
        form=userRegisterForm(request.POST) #if post req the get data from form
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request,f'your account has been created please Login!')
            return redirect('login')

    else:
        form=userRegisterForm() #anything thats not a post , give blank form 
    return render(request,'users/register.html',{'form': form})

@login_required
def profile(request):
    return render(request,'users/profile.html')

