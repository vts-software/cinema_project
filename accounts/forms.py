from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LogoutView
from django.urls import reverse_lazy
from accounts.models import User


class RegisterForm(UserCreationForm):
    """Форма регистрации пользователя"""

    email = forms.EmailField(
        required=True,
        label="Email",
        widget=forms.EmailInput(attrs={"placeholder": "Введите ваш email"})
    )
    avatar = forms.ImageField(
        required=False,
        label="Аватар"
    )
    bio = forms.CharField(
        required=False,
        label="О себе",
        widget=forms.Textarea(attrs={"rows": 3, "placeholder": "Пару слов о себе"})
    )

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2", "avatar", "bio")

    def clean_email(self):
        """Проверяем уникальность email"""
       
        email = self.cleaned_data.get("email").lower()
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("Пользователь с таким email уже существует.")
        return email
    
    def clean_password2(self):
        """Проверяем совпадение паролей"""
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Пароли не совпадают.")
        return password2

    def save(self, commit=True):
        """Сохраняем пользователя и возвращаем экземпляр"""
        user = super().save(commit=False)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user
    

from django.contrib.auth.forms import AuthenticationForm
from django import forms


class LoginForm(AuthenticationForm):
    """Форма входа пользователя"""

    username = forms.CharField(
        label="Имя пользователя",
        widget=forms.TextInput(attrs={
            "placeholder": "Введите имя пользователя",
            "class": "form-control"
        })
    )
    password = forms.CharField(
        label="Пароль",
        widget=forms.PasswordInput(attrs={
            "placeholder": "Введите пароль",
            "class": "form-control"
        })
    )


class CustomLogoutView(LogoutView):
    next_page = reverse_lazy('home')