from django.forms import models
from django.shortcuts  import get_object_or_404, redirect
from django.http import Http404

from translate.models import Translate

from .models import User
class TranslatorAccessMixin():
    def dispatch(self,request,pk,*args,**kwargs):
        # article=get_object_or_404(Article,pk=pk)
        if request.user.is_authenticated:
            trans=get_object_or_404(Translate,pk=pk)
            if trans.author ==request.user or request.user.is_superuser:
                return super().dispatch(request,*args,**kwargs)
            else:
                return redirect('account:home')
        else:
            return redirect('login')
class SuperUserAccessMixin():
    def dispatch(self,request,*args,**kwargs):
        if request.user.is_authenticated:
            if request.user.is_superuser :
                return super().dispatch(request,args,kwargs)
            else:
                return redirect('account:home')
        else:
            return redirect('login')
class UserAccessMixin():
    def dispatch(self,request,*args,**kwargs):
        if request.user.is_authenticated:
                return super().dispatch(request,args,kwargs)
        else:
            return redirect('login')

class FormValidMixin():
    def form_valid(self,form):

        self.obj=form.save(commit=False)
        self.obj.customer=self.request.user
        self.obj.type='t'
        return super().form_valid(form)
    
class FormValidEditorMixin():
    def form_valid(self,form):
        self.obj=form.save(commit=False)
        self.obj.type='e'
        self.obj.author= self.request.user
        return super().form_valid(form)
class FormValidProMixin():
    def form_valid(self,form):
        self.obj=form.save(commit=False)
        self.obj.type='pt'
        self.obj.author= User.objects.filter(is_superuser=True)
        return super().form_valid(form)
class FieldMixin():
    def dispatch(self,request,*args,**kwargs):
        if request.user.is_authenticated:
            self.fields=['language', 'title', 'price', 'filesend'  ,'author', 'is_finished']
        else:
            raise Http404
        return super().dispatch(request,*args,**kwargs)
# class SellerAccessMixin():
#     def dispatch(self,request,*args,**kwargs):
#         if request.user.is_authenticated:
#             if request.user.is_superuser or request.user.is_seller:
#                 return super().dispatch(request,args,kwargs)
#             else:
#                 return redirect('account:profile')
#         else:
#             return redirect('login')
# class FieldMixin():
#     def dispatch(self,request,*args,**kwargs):
#         if request.user.is_superuser:
#             self.fields=('category','thumbnail','title','description','slug','price','publish','type','status','brand','seller','color')
#         elif request.user.is_seller:
#             self.fields=('category','thumbnail','title','description','slug','price','publish','type','status','brand','color')
#         else:
#             raise Http404
#         return super().dispatch(request,*args,**kwargs)
