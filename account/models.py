from django.db import models
from django.contrib.auth.models import AbstractUser,UserManager

# Create your models here.
class User(AbstractUser):
       
    email    =models.EmailField(unique=True ,null=True,verbose_name='ایمیل')
    is_translator=models.BooleanField(default=False,verbose_name='وضعیت نویسنده')
    # is_seller=models.BooleanField(default=False,verbose_name='وضعیت فروشنده')
