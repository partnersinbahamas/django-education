from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.shortcuts import redirect

# Create your views here.

def register(request):
    if (request.method == 'POST'):
        form = UserCreationForm(request.POST)

        if form.is_valid():
            form.save()

            # to create notification about log
            """
            methods: 
              .success, .info, .add_message
              .warning, .error, .debug
            """
            messages.success(request, 'Registration success.')
            return redirect('login')
        else:
            messages.error(request, 'Registration failed.')
    else:
        form = UserCreationForm()

    data = {
        'form': form,
    }
    return render(request, 'users/register.html', data)

def login(request):
    return render(request, 'users/login.html')