# Generated by Django 3.1.7 on 2021-03-21 09:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('user_account', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=125, verbose_name='Ваше имя')),
                ('email', models.EmailField(max_length=254, null=True, verbose_name='email')),
                ('image', models.ImageField(blank=True, upload_to='feedbacks/%Y/%m/%d', verbose_name='Изображение(необязательно)')),
                ('message', models.TextField(verbose_name='Подробнее')),
                ('date', models.DateTimeField(auto_now_add=True, verbose_name='Дата обращения')),
                ('supplier', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='feedbacks', to='user_account.supplier', verbose_name='Поставщик')),
            ],
        ),
    ]
