# Generated by Django 3.2.9 on 2021-12-09 05:27

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Translate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('publish', models.DateTimeField(default=django.utils.timezone.now, verbose_name='زمان')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='زمان ساخت')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='زمان آپدیت')),
                ('status', models.CharField(choices=[('d', 'پیش نویس'), ('p', 'منتشر شده')], max_length=1, verbose_name='وضعیت')),
                ('language', models.CharField(choices=[('english', 'انکلیسی'), ('french', 'فرانسوی')], max_length=7, verbose_name='زبان')),
                ('title', models.CharField(max_length=200, verbose_name='عوان')),
                ('file', models.FileField(max_length=300, upload_to='files', verbose_name='فایل')),
                ('author', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='translate', to=settings.AUTH_USER_MODEL, verbose_name='مترجم')),
            ],
            options={
                'verbose_name': 'ترجمه',
                'verbose_name_plural': 'ترجمه ها',
                'ordering': ['-publish'],
            },
        ),
    ]
