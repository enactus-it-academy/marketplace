from django.db import models

from user_account.models import Supplier, User


class Feedback(models.Model):
    supplier = models.ForeignKey(Supplier,
                                 on_delete=models.CASCADE,
                                 null=True, blank=True,
                                 related_name='feedbacks',
                                 verbose_name='Поставщик')
    name = models.CharField('Ваше имя', max_length=125, blank=True)
    email = models.EmailField(User.get_email_field_name(), null=True)
    image = models.ImageField('Изображение(необязательно)',
                              upload_to='feedbacks/%Y/%m/%d',
                              blank=True)
    message = models.TextField('Подробнее')
    date = models.DateTimeField('Дата обращения', auto_now_add=True)
