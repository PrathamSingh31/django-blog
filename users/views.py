from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm,Userupdateform,Profileupdateform
# Create your views here.
def register(request):
    if request.method=="POST":
        form=UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username=form.cleaned_data.get('username')
            messages.success(request,f'Accout created for {username}')
            return redirect('login')
    else:
        form=UserRegisterForm()
    return render(request,'users/register.html',{'form':form})

@login_required
def profile(request):
    if request.method=="POST":
        u_form=Userupdateform(request.POST,instance=request.user)
        p_form=Profileupdateform(request.POST,request.FILES,instance=request.user.profile)
        if u_form.is_valid() and  p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request,f'Accout has been Updated')
            return redirect('profile')

    else:
        u_form=Userupdateform(instance=request.user)
        p_form=Profileupdateform(instance=request.user.profile)
        
    return render(request,'users/profile.html', {'u_form':u_form,'p_form':p_form})