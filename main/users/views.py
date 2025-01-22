from django.shortcuts import render
from django.contrib import messages
from django.shortcuts import redirect
from .forms import UserForm, UserLoginForm, ContactForm
from django.contrib.auth import login, logout
from django.core.mail import send_mail

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

def user_contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)

        if form.is_valid():
            mail = send_mail(
              form.cleaned_data['subject'],
              form.cleaned_data['content'],
              'devsonley@gmail.com',
              [request.user.email],
              fail_silently=True,
              auth_password="HACH1703"
            )

            if mail:
                messages.success(request, 'Mail send successfuly.')
            else:
                messages.error(request, 'Email sending failed.')
        else:
            messages.error(request, 'Something went wrong.')

    else:
        form = ContactForm()

    data = {
        'form': form
    }

    return render(request, 'users/contact.html', data)