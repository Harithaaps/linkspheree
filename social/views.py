from django.shortcuts import render

from django.views.generic import FormView,CreateView

from social.forms import RegistrationForm
from django.urls import reverse


class SignUpView(CreateView):
    template_name="register.html"
    form_class=RegistrationForm

    def get_success_url(self):
        return reverse("sign_up")

    #def post(self,request,*args,**kwargs):
    #    form=RegistrationForm(request.POST)
    #    if form.is_valid():
    #        form.save()
    #        return redirect("sign_up")
    #    else:
    #        return render(request,"register.html",{"form":form})

    