from django.shortcuts import render
from django.views.generic import FormView, UpdateView
from .forms import UserRegistrationForm
from django.http import HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from django.contrib.auth import authenticate, login
from .models import CustomUser
from django.contrib import messages


def home_view(request):
    return render(request, 'accounts/dashboard.html', {})


class RegisterUser(FormView):
    template_name = 'accounts/register.html'
    form_class = UserRegistrationForm
    success_url = 'home'

    def form_valid(self, form):
        # perform a action here
        user_obj = form.save(commit=False)
        user_obj.staff = False
        user_obj.admin = False
        user_obj.is_customer = True
        user_obj.save()
        messages.add_message(self.request, messages.INFO, 'You have successfully registered, Please login to continue!')
        return HttpResponseRedirect(reverse('accounts:login'))


class LoginView(View):

    def post(self, request):
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            messages.add_message(self.request, messages.INFO,
                                 'You have successfully logged in! Please continue to your dashboard!')
            login(request, user)
            return HttpResponseRedirect(reverse('accounts:dashboard'))
        else:
            messages.add_message(self.request, messages.ERROR, 'Failed to Login, please try again!')
            return HttpResponseRedirect(self.request.path_info)

    def get(self, request):
        return render(request, 'accounts/login.html', {})


class DashboardView(LoginRequiredMixin, View):

    def get(self, request):
        profile_data = CustomUser.objects.get(id=request.user.id)
        return render(request, 'accounts/dashboard.html', {
            'profile_data': profile_data
        })


class UpdateAccountSettings(LoginRequiredMixin, UpdateView):
    model = CustomUser
    form_class = UserRegistrationForm
    template_name = 'accounts/update_settings.html'

    def get_object(self, queryset=None):
        return CustomUser.objects.get(id=self.request.user.id)

    def form_valid(self, form):
        # perform a action here
        user_obj = form.save(commit=False)
        user_obj.staff = False
        user_obj.admin = False
        user_obj.save()
        messages.add_message(self.request, messages.INFO, 'You have successfully updated your account settings')
        return HttpResponseRedirect(reverse('home'))

