from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth import login
from django.http import HttpResponse
from .forms import SignUpForm
from django.contrib.auth import logout
from django.views import View
class CustomLoginView(LoginView):
    template_name = 'accounts/login.html'

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('entry_list')
    else:
        form = SignUpForm()
    return render(request, 'accounts/signup.html', {'form': form})


class CustomLogoutView(LogoutView):
    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)
        return redirect('login')  

    def get(self, request, *args, **kwargs):
        return redirect('login')  
