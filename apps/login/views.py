from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from django.views import View


from apps.login.forms import CreatUserForm


class RegisterView(View):
    template = 'register.html'
    def get(self, request):
        register_form = CreatUserForm
        return render(request, self.template, dict(register_form=register_form))

    def post(self, request):
        register_form = UserCreationForm(request.POST)
        if register_form.is_valid():
            register_form.save()
            messages.info(request, 'Cuenta creada!')
            return redirect('book:home')
        else:
            for msg in register_form.error_messages:
                messages.error(request, register_form.error_messages[msg])
            return render(request, self.template, dict(register_form=register_form))


class AccederView(LoginView):
    template_name = 'login.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

