from django.urls import path

from app_users.views import AuthLoginView, AuthLogoutView, RegistrationView

app_name = "users"

urlpatterns = [
    path('login/', AuthLoginView.as_view(), name='login'),
    path('logout/', AuthLogoutView.as_view(), name='logout'),
    path('registration/', RegistrationView.as_view(), name='registration'),
]
