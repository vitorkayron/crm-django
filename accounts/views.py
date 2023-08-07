from django.shortcuts import render
from .forms import LoginForm, UserRegistrationForm
from django.http import HttpResponse

from django.contrib.auth import authenticate, login


# Create your views here.
def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request, username=cd['username'], password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponse('Authenticated '\
                                    'successfully')
                else:
                    return HttpResponse('Disabled account')
            else:
                return HttpResponse('Invalid login')
    else:
        form = LoginForm()
        return render(request, 'accounts/login.html', {'form': form})
    

def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            newuser = user_form.save(commit=False)
            newuser.set_password(user_form.cleaned_data['password'])  # Correção: set_password, não set_passoetd
            newuser.save()
            return render(request, 'registration/register_done.html', {'new_user': newuser})
    else:
        user_form = UserRegistrationForm()  # 
    return render(request, 'registration/register.html', {'user_form': user_form})  