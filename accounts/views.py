from django.shortcuts import render, redirect
from .forms import LoginForm, UserRegistrationForm


from django.contrib.auth import authenticate, login


# Create your views here.



def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            newuser = user_form.save(commit=False)
            newuser.set_password(user_form.cleaned_data['password'])
            newuser.save()

            user = authenticate(username=user_form.cleaned_data['username'], password=user_form.cleaned_data['password'])
            
            if user is not None:
                login(request, user)
                return redirect('home') 
    else:
        user_form = UserRegistrationForm()  
    return render(request, 'registration/register.html', {'user_form': user_form})  
    