from django.contrib.auth import authenticate, login
from django.contrib.auth.views import LoginView
from django.http import HttpResponse
from django.shortcuts import render
from .forms import AuthForm


def auth(request):
    if request.method == 'POST':
        auth_form = AuthForm(request.POST)
        if auth_form.is_valid():
            username = auth_form.cleaned_data.get('login')
            password = auth_form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user:
                if user.is_active:  # нерабочая хрень
                    print('active')
                    login(request, user)
                    return HttpResponse('ok')
                else:
                    auth_form.add_error('__all__', 'Пользователь не активен')
            else:
                auth_form.add_error('__all__', 'нет такого пользователя с таким паролем')
            return render(request, 'user/auth.html', {'auth_form': auth_form})
    else:
        auth_form = AuthForm()
        return render(request, 'user/auth.html', {'auth_form': auth_form})


class Auth2(LoginView):
    template_name = 'user/auth.html'
