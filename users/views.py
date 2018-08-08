from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic.edit import FormView
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect
from django.views.generic.base import View
from django.contrib.auth import logout

# Create your views here.
class MainView(TemplateView):
    template_name = 'mainApp/homepage.html'
    def get(self,request):
        if request.user.is_authenticated:
            return render(request , self.template_name, ctx)
        else:
            return render(request , self.template_name, {})
class RegisterFormView(FormView):
    from_class = UserCreationForm
    success_url = "/login/"
    template_name = "users/register.html"

    def form_valid(self,form):
        form.save()
        return super(RegisterFormView, self).form_valid(form)
