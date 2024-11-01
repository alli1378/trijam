from django.http.response import Http404
from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView,PasswordChangeView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .mixins import TranslatorAccessMixin,SuperUserAccessMixin
from django.views.generic import (ListView,
                                 CreateView,
                                 UpdateView,
                                 DeleteView)
from .forms import (ProfileForm,SignupForm,FieldForm)
# Create your views here.
# auth
from translate.models import Translate
from .models import User
class Login(LoginView):
    def get_success_url(self):
        user=self.request.user
        # if user.is_superuser :
        #     return reverse_lazy('account:product-list')
        # if user.is_translator:
        #     return reverse_lazy('account:home')
        # else:
        return reverse_lazy('account:profile')
class Profile(LoginRequiredMixin,UpdateView):
    model=User
    form_class=ProfileForm
    template_name='registration/profile.html'
    success_url=reverse_lazy('account:profile')
    def get_object(self):
        return User.objects.get(pk=self.request.user.pk)
    def get_form_kwargs(self):
        kwargs=super(Profile,self).get_form_kwargs()
        kwargs.update({
            'user':self.request.user,
        })
        return kwargs
class TranslateList(LoginRequiredMixin,ListView):
    template_name='registration/translate-list.html'
    context_object_name='translates'
    def get_queryset(self):
        if self.request.user.is_superuser:
            return Translate.objects.all()
        elif self.request.user.is_superuser:
            return Translate.objects.filter(author=self.request.user)
        return Translate.objects.filter(customer=self.request.user)
class TranslatorCreate(SuperUserAccessMixin,CreateView):
    model=Translate
    form_class=FieldForm
    template_name='registration/translate-crate-update.html'
    def get_form_kwargs(self):
            kwargs=super(TranslatorCreate,self).get_form_kwargs()
            kwargs.update({
                'user':self.request.user,
            })
            return kwargs

class TranslatorUpdate(TranslatorAccessMixin,UpdateView):
    model=Translate
    form_class=FieldForm

    template_name='registration/translate-crate-update.html'
    def get_form_kwargs(self):
            kwargs=super(TranslatorUpdate,self).get_form_kwargs()
            kwargs.update({
                'user':self.request.user,
            })
            return kwargs

# # Brand
# class BrandList(SuperUserMixin,ListView):
#     context_object_name='brands'
#     template_name='registration/brand.html'
#     def get_queryset(self):
#         return Brand.objects.all()
# class BrandCreate(SuperUserMixin,CreateView):
#     model=Brand
#     template_name='registration/brand-create-update.html'
#     fields=['description','title','employe','slug']

from django.http import HttpResponse
from .forms import SignupForm
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from .tokens import account_activation_token
from django.core.mail import EmailMessage


class Register(CreateView):
    form_class=SignupForm
    template_name='registration/register.html'
    def form_valid(self,form):
        user = form.save(commit=False)
        user.is_active = False
        user.save()
        current_site = get_current_site(self.request)
        mail_subject = 'فعال سازی اکانت'
        message = render_to_string('registration/activate_account.html', {
            'user': user,
            'domain': current_site.domain,
            'uid':urlsafe_base64_encode(force_bytes(user.pk)),
            'token':account_activation_token.make_token(user),
        })
        to_email = form.cleaned_data.get('email')
        email = EmailMessage(
                    mail_subject, message, to=[to_email]
        )
        email.send()
        return HttpResponse('لینک فعال سازی به ایمیل شما ارسال شد<a href="/login">ورود</a>')

def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        # login(request, user)
        # return redirect('home')
        # context={
        #         'uidb64':uidb64,
        #         'token':token,
        #         }
        return HttpResponse('اکانت شما با موفقیت فعال شد برای ورود کلیک کنید<a href="/login">کلیک</a>کنید.')
    else:
        user.delete()
        return HttpResponse('لینک فعال سازی منقضی شده است <a href="/register">دوباره تلاش کنید.</a>')
