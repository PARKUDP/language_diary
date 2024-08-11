from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User

class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['account_id', 'email', 'password1', 'password2']
        labels = {
            'account_id': 'アカウントID',
            'email': 'メールアドレス',
            'password': 'パスワード',
        }
        error_messages = {
            'account_id': {
                'required': 'アカウントIDを入力してください。',
            },
            'email': {
                'required': 'メールアドレスを入力してください。',
                'invalid': '有効なメールアドレスを入力してください。',
            },
        }