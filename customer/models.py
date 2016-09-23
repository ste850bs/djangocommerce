# coding=utf-8
from __future__ import unicode_literals
from django.db import models
from django.utils import timezone
from django.utils.timezone import datetime

from django import forms

from product.models import *

from django.contrib.auth.models import User


# Create your models here.
class Customer(models.Model):
    user = models.OneToOneField(User, related_name='profile')
    discount = models.IntegerField(blank=True, null=True, default=0, verbose_name="sconto percentuale")
    pub_date = models.DateTimeField('date published')
    active = models.BooleanField('attiva', default=False)

    def __unicode__(self):
        return self.user.username

    class Meta:
        verbose_name_plural = "Cliente"
        ordering = ['id']



class Fatturazione(models.Model):
    user = models.ForeignKey(User, null=True, blank=True)
    denominazione = models.CharField('denominazione', max_length=250, null=True, blank=True)
    piva = models.CharField('Piva', max_length=250, null=True, blank=True)
    codfisc = models.CharField('codice fiscale', max_length=250, null=True, blank=True)
    indirizzo = models.CharField('indirizzo', max_length=250, null=True, blank=True)
    cap = models.CharField('Cap', max_length=250, null=True, blank=True)
    citta = models.CharField('Citta', max_length=250, null=True, blank=True)
    nazione = models.CharField('nazione', max_length=250, null=True, blank=True)
    telefono = models.CharField('Telefono', max_length=250, null=True, blank=True)
    fax = models.CharField('Fax', max_length=250, null=True, blank=True)
    e_mail = models.CharField('email', max_length=250, null=True, blank=True)
    pec = models.CharField('pec', max_length=250, null=True, blank=True)
    indirizzo_spedizione = models.BooleanField('è anche indirizzo di spedizione', default=False)

    def __unicode__(self):
        self.user.username

    class Meta:
        verbose_name_plural = "Dati di Fatturazione"

        

class IndirizzoSpedizione(models.Model):
    user = models.ForeignKey(User, null=True, blank=True)
    denominazione = models.CharField('denominazione', max_length=250, null=True, blank=True)
    indirizzo = models.CharField('indirizzo', max_length=250, null=True, blank=True)
    cap = models.CharField('Cap', max_length=250, null=True, blank=True)
    citta = models.CharField('Citta', max_length=250, null=True, blank=True)
    nazione = models.CharField('nazione', max_length=250, null=True, blank=True)
    telefono = models.CharField('Telefono', max_length=250, null=True, blank=True)
    fax = models.CharField('Fax', max_length=250, null=True, blank=True)
    e_mail = models.CharField('email', max_length=250, null=True, blank=True)

    def __unicode__(self):
        self.user.username

    class Meta:
        verbose_name_plural = "Indirizzo di Spedizione"
