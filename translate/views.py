from django.db.models import fields
from django.shortcuts import render
from django.views.generic import CreateView
from django.urls import reverse_lazy
from account.forms import FieldFormAll,FieldForm
from .models import Translate
from account.mixins import FieldMixin, FormValidMixin,FormValidProMixin,FormValidEditorMixin,UserAccessMixin
 
# from backend.translate.models import Translate
# Create your views here.

# class TranslateCreate(CreateView):
#     model=Translate
#     # form_class=FieldFormAll
#     fields=['language', 'title','author','customer', 'filesend','filerisive','price','type','is_finished' ]
#     success_url=reverse_lazy('account:profile')
#     template_name='main/سفارش ترجمه مقاله.html'
#     fields=['customer','filesend','type','title','language']  
class TranslateCreate(UserAccessMixin,FieldMixin,FormValidMixin,CreateView):
    model=Translate
    template_name='main/سفارش ترجمه مقاله.html'
    
class TranslateProCreate(UserAccessMixin,FieldMixin,FormValidProMixin,CreateView):
    model=Translate
    template_name='main/سفارش ترجمه تخصصی.html'
class EditorCreate(UserAccessMixin,FieldMixin,FormValidEditorMixin,CreateView):
    model=Translate
    template_name='main/سفارش ویراستاری.html'

def Home(request):
    context={}
    return render(request,'main/index.html',context)
def Translate(request):
    context={}
    return render(request,'main/ترجمه تخصصی متون.html',context)
def edit(request):
    context={}
    return render(request,'main/ویراستاری تخصصی متون.html',context)
def uni(request):
    context={}
    return render(request,'main/ترجمه مقالات دانشگاهی.html',context)
# ارتباط