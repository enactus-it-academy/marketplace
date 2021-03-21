from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from phonenumber_field.modelfields import PhoneNumberField


class User(AbstractUser):
    is_supplier = models.BooleanField('supplier status', default=False)


class Supplier(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField('Изображение',
                              upload_to='suppliers/%Y/%m/%d',
                              blank=True)
    description = models.TextField('Описание', blank=True)
    phone_number = PhoneNumberField('Номер телефона', blank=True)
    social_networks = models.CharField('Социальные сети', max_length=255, blank=True)

    def __str__(self):
        return self.user.get_full_name()


@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    """
    Определение сигналов, чтобы модель Supplier
    автоматически обновлялась при создании/изменении данных модели User.
    """
    if instance.is_supplier:
        if created:
            Supplier.objects.create(user=instance)

        instance.supplier.save()
