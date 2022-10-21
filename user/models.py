from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from django.db.models.signals import post_save
from django.dispatch import receiver

import uuid


class Users(AbstractUser):
    uid = models.UUIDField(unique=True, default=uuid.uuid4)
    email = models.EmailField(_('email address'), unique=True)
    username = models.CharField(_('username'), max_length=50, null=True, blank=True, unique=True)
    name = models.CharField(max_length=100, unique=False, null=True, blank=True)
    password = models.CharField(_('password'), max_length=50, null=True, blank=True, unique=True)

    class Meta:
        verbose_name_plural = "Users"

    def __str__(self):
        return str(self.email)


@receiver(post_save,sender=Users)
def generate_user_details(sender,instance=None,created=False,**kwargs):
    if created:
        UserDetails.objects.create(email=instance.email, full_name=instance.name, 
        first_name=instance.name.split(' ')[0], last_name=instance.name.split(' ')[1:])
    else:
        pass


class UserDetails(models.Model):
    uid = models.UUIDField(default=uuid.uuid4, unique=True)
    user = models.ForeignKey(Users, on_delete=models.CASCADE, null=True, blank=True, related_name='user_dtl')
    first_name = models.CharField(max_length=100, unique=False, null=True, blank=True)
    last_name = models.CharField(max_length=100, unique=False, null=True, blank=True)
    full_name = models.CharField(max_length=100, unique=False, null=True, blank=True)
    email = models.EmailField(unique=True, null=True, blank=True)

    address =  models.TextField(max_length=250, null=True, blank=True)
    place =  models.CharField(max_length=100, unique=False, null=True, blank=True)
    city =  models.CharField(max_length=100, unique=False, null=True, blank=True)
    state =  models.CharField(max_length=100, unique=False, null=True, blank=True)
    zipcode =  models.CharField(max_length=100, unique=False, null=True, blank=True)
    
    phone =  models.CharField(max_length=100, unique=False, null=True, blank=True)
    alternative_phone =  models.CharField(max_length=100, unique=False, null=True, blank=True)
    
    alternative_email =  models.CharField(max_length=100, unique=False, null=True, blank=True)
    alternative_contact_person = models.CharField(max_length=100, unique=False, null=True, blank=True)

    job_profile = models.CharField(max_length=100, unique=False, null=True, blank=True)
    job_role = models.CharField(max_length=100, unique=False, null=True, blank=True)

    about = models.TextField(max_length=500, null=True, blank=True)

    join_date = models.DateTimeField(auto_now_add=True)

    role = models.CharField(null=True, blank=True, max_length=50)


    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name_plural = 'User Details'

    def save(self, *args, **kwargs):
        self.full_name = f"{self.first_name} {self.last_name}"
        self.role = 'admin' if self.user.is_superuser == True else 'user'
        super(UserDetails,self).save(*args,**kwargs)


class UserProfileDetails(models.Model):
    uid = models.UUIDField(default=uuid.uuid4,unique=True)
    user = models.ForeignKey(UserDetails, on_delete=models.CASCADE, null=True, blank=True, related_name='user_profile_img')
    profile_image = models.ImageField(upload_to='user/profile/profile-image/', null=True, blank=True)

    def __str__(self):
        return self.user.full_name

    class Meta:
        verbose_name_plural = 'User Profile Details'

    
class GuestUsers(models.Model):
    uid = models.UUIDField(default=uuid.uuid4, unique=True)
    email = models.EmailField(null=True, blank=True, max_length=100, unique=False)
    full_name = models.CharField(max_length=100, unique=False, null=True, blank=True)
    phone = models.CharField(max_length=20, unique=False, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Guest Users'

    def __str__(self):
        return self.full_name