from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth import get_user_model, login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages

from .forms import RegisterForm, LoginForm

User = get_user_model()


class RegisterView(CreateView):
    """Регистрация нового пользователя"""
    model = User
    form_class = RegisterForm
    template_name = "accounts/register.html"
    success_url = reverse_lazy("accounts:login")

    def form_valid(self, form):
        """Сохраняем пользователя и показываем сообщение"""
        response = super().form_valid(form)
        messages.success(self.request, "Регистрация прошла успешно! Теперь войдите в систему.")
        return response


class CustomLoginView(LoginView):
    """Вход пользователя"""
    template_name = "accounts/login.html"
    authentication_form = LoginForm
    redirect_authenticated_user = True

    def get_success_url(self):
        """После входа — на главную страницу"""
        messages.success(self.request, f"Добро пожаловать, {self.request.user.username}")
        return reverse_lazy("home")


class CustomLogoutView(LogoutView):
    """Выход пользователя"""
    next_page = reverse_lazy("home")

    def dispatch(self, request, *args, **kwargs):
        messages.info(request, "Вы успешно вышли из аккаунта")
        return super().dispatch(request, *args, **kwargs)


class ProfileView(LoginRequiredMixin, DetailView):
    """Просмотр профиля"""
    model = User
    template_name = "accounts/profile.html"
    context_object_name = "user_profile"

    def get_object(self, queryset=None):
        return self.request.user
