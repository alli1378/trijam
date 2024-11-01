# from django.contrib import admin
from django.urls import path
from .views import Profile,TranslatorUpdate,TranslatorCreate,TranslateList
app_name='account'
urlpatterns = [
    # path('admin/', admin.site.urls),
    path('profile/',Profile.as_view(),name='home'),
    path('translate-update/<int:pk>',TranslatorUpdate.as_view(),name='update-translate'),
    path('create-translate/',TranslatorCreate.as_view(),name='create-translate'),
    path('list-translate/',TranslateList.as_view(),name='list-translate'),

]