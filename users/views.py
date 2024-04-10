from django.shortcuts import render, redirect
from .forms import RegForm, UserUpdate
from django.contrib import messages
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required

def registration(request):
    if request.method == 'POST':
        regform = RegForm(request.POST)
        if regform.is_valid():
            regform.save()
            username = regform.cleaned_data.get('username')
            messages.success(request, f'Пользователь {username} зарегистрирован')
            return redirect('home')
    else:
        regform = RegForm()

    return render(request, 'users/registration.html', {'regform': regform})


def logout_view(request):
    return render(logout(request), 'users/exit.html')

@login_required
def profile(request):
    if request.method == 'POST':
        user_update = UserUpdate(request.POST, instance=request.user)

        if user_update.is_valid():
            user_update.save()
            #messages.success(request, f'Аккаунт обновлен')
            return redirect('profile')
            
    else:
        user_update = UserUpdate(instance=request.user)

    return render(request, 'users/profile.html', {'user_update': user_update})
