from __future__ import unicode_literals
from django.db import models
from django.utils import timezone
from django.utils.timezone import datetime

from django import forms

from django.contrib.auth.models import User


# Create your models here.
class Customer(models.Model):
    user = models.OneToOneField(User, related_name='profile')
    discount = models.IntegerField(blank=True, null=True, verbose_name="sconto percentuale")
    pub_date = models.DateTimeField('date published')
    active = models.BooleanField('attiva', default=False)

    def __unicode__(self):
        return self.user.username

    class Meta:
        verbose_name_plural = "Cliente"
        ordering = ['id']
