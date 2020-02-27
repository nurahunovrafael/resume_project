from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Person(models.Model):
    user_id = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True,) 
    first_name = models.CharField(max_length=30, null=True, blank=True)
    last_name = models.CharField(max_length=30, null=True, blank=True)
    middle_name = models.CharField(max_length=30, null=True, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    email = models.CharField(max_length=30, null=True, blank=True)
    SEX_CHOICES = ( ('male', 'Male'), ('female', 'Female'),)
    sex = models.CharField(max_length=10, choices=SEX_CHOICES, default='male') 
    MARITAL_STATUS_CHOICES = ( ('married', 'Married'), ('single', 'Single'),)
    marital_status = models.CharField(max_length=10, choices=MARITAL_STATUS_CHOICES, default='married')
    phone = models.CharField(max_length=14, null=True, blank=True)
    citizenship = models.CharField(max_length=30, null=True, blank=True)
    city = models.CharField(max_length=30, null=True, blank=True)

    def __str__(self):
        return self.first_name

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Person.objects.create(user_id=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    username =  User.objects.get(pk=instance.pk)
    instance.person.first_name = username.username
    instance.person.save()