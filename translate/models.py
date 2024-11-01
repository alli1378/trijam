from django.db import models
from django.utils.regex_helper import Choice
from account.models import User
from django.utils import  timezone
from extentions.utils import jalali_converter
from django.urls.base import reverse

# Create your models here.
class Translate(models.Model):
    lng=(
          ('english','انکلیسی'),
          ('french','فرانسوی'),
      )
    STATUS_CHOICES=(
                ('t','ترجمه'),       #draft
                ('e','ویراستاری'),      #publish
                ('pt','ترجمه تخصصی'),    #investigation
                # ('b','برگشت داده شده'), #back
            )
    publish=models.DateTimeField(default=timezone.now,verbose_name='زمان')
    created=models.DateTimeField(auto_now_add=True,verbose_name='زمان ساخت')
    updated=models.DateTimeField(auto_now=True,verbose_name='زمان آپدیت')
    language=models.CharField(max_length=7,choices=lng,verbose_name="زبان")
    type=models.CharField(max_length=2,choices=STATUS_CHOICES,verbose_name='نوع',default='t')
    title=models.CharField(max_length=200,verbose_name='عوان')
    author=models.ForeignKey(User,blank=True,on_delete=models.SET_NULL,related_name='translate',null=True,verbose_name='مترجم')
    customer=models.ForeignKey(User,null=True,on_delete=models.SET_NULL,related_name='customer',verbose_name='مشتری')
    price=models.DecimalField(default=0,max_digits=10,decimal_places=0,verbose_name='قیمت',null=True,blank=True)
    filesend = models.FileField(upload_to='files', max_length=300 ,verbose_name='فایل')
    filerisive = models.FileField(upload_to='files', max_length=300 ,verbose_name='فایل',null=True,blank=True)
    is_finished=models.BooleanField(default=False,verbose_name='تمام شده')
    class Meta:
        verbose_name="ترجمه"
        verbose_name_plural="ترجمه ها"
        ordering=['-publish']
    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return reverse('translate:home')
    def jpublish(self):
        return jalali_converter(self.publish)
    jpublish.short_description='زمان انتشار'
    # def category_to_str(self):
    #     return ' و'.join([category.title for category in self.category.status_true()])
    # category_to_str.short_description='دسته بندی ها'
 
# 