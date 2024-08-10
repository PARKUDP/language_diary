from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth import login
from django.http import HttpResponse
from .forms import SignUpForm

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
        return HttpResponse('Logged out successfully')

    def get(self, request, *args, **kwargs):
        # GETリクエストの場合、メッセージを表示する
        return HttpResponse('This page should be accessed via POST method.')
