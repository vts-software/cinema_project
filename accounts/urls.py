from django.urls import path
from django.shortcuts import redirect
from .views import RegisterView, CustomLoginView, CustomLogoutView, ProfileView

app_name = "accounts"

urlpatterns = [
    # Перенаправляем с /accounts/ на /accounts/login/
    path("", lambda request: redirect("accounts:login"), name="accounts_root"),

    # Регистрация и аутентификация
    path("register/", RegisterView.as_view(), name="register"),
    path("login/", CustomLoginView.as_view(), name="login"),
    path("logout/", CustomLogoutView.as_view(), name="logout"),

    # Профиль пользователя
    path("profile/", ProfileView.as_view(), name="profile"),
]