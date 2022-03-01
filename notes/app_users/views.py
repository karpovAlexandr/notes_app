from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView, LogoutView
from django.http import HttpResponseRedirect
from django.views.generic import CreateView

from app_users.forms import RegistrationForm


class RegistrationView(CreateView):
    form_class = RegistrationForm
    template_name = 'registration/registration.html'

    def form_valid(self, form):
        form.save()
        new_user = authenticate(
            username=form.cleaned_data['email'],
            password=form.cleaned_data['password1'],
        )
        login(self.request, new_user)
        return HttpResponseRedirect('/')


class AuthLoginView(LoginView):
    authentication_form = AuthenticationForm


class AuthLogoutView(LogoutView):
    pass

