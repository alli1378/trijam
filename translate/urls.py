from django.urls import path
from .views import (Home
                    ,TranslateCreate
                    ,Translate
                    ,TranslateProCreate
                    ,EditorCreate
                    ,uni
                    ,edit
                    )
app_name='translate'
urlpatterns = [
    path('', Home,name='home'),
    path('translates/',Translate,name='trans'),
    path('uni/',uni,name='uni'),
    path('edit/',edit,name='edit'),
    path('translates/translate',TranslateCreate.as_view(),name='translate'),
    path('translates/translate-pro',TranslateProCreate.as_view(),name='translate-pro'),
    path('translates/editor',EditorCreate.as_view(),name='editor'),

]