from django.shortcuts import render
from django.contrib import messages
from django.shortcuts import redirect
from .forms import UserForm, UserLoginForm
from django.contrib.auth import login, logout

# Create your views here.

def register(request):
    if (request.method == 'POST'):
        form = UserForm(request.POST)

        if form.is_valid():
            user = form.save()

            login(request, user)

            # to create notification about log
            """
            methods: 
              .success, .info, .add_message
              .warning, .error, .debug
            """
            messages.success(request, 'Registration success.')
            return redirect('news')
        else:
            messages.error(request, 'Registration failed.')
    else:
        form = UserForm()

    data = {
        'form': form,
    }
    return render(request, 'users/register.html', data)

def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)

        if form.is_valid():
            user = form.get_user()
            login(request, user)

            messages.success(request, 'Login success.')
            return redirect('news')
        else:
            messages.error(request, 'Login failed.')
    else:
        form = UserLoginForm()

    data = {
        'form': form
    }
    return render(request, 'users/login.html', data)


def user_logout(requset):
    logout(requset)
    return redirect('login')