# Generated by Django 3.1.7 on 2021-03-17 16:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='reviews',
            field=models.TextField(blank=True, null=True, verbose_name='Отзывы'),
        ),
    ]
