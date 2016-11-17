# coding=utf-8
from __future__ import unicode_literals
from django.db import models
from django.utils import timezone
from django.utils.timezone import datetime

from django import forms
from django.forms import ModelForm

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
    myemail = models.CharField('email', max_length=250, null=True, blank=True)
    pec = models.CharField('pec', max_length=250, null=True, blank=True)
    indirizzo_spedizione = models.BooleanField('è anche indirizzo di spedizione', default=False)
    pub_date = models.DateTimeField('date published', null=True, blank=True, editable=False)

    def save(self, *args, **kwargs):
        self.pub_date = datetime.now()
        super(Fatturazione, self).save(*args, **kwargs)

    def __unicode__(self):
        return unicode(self.user.username) or u''

    class Meta:
        verbose_name_plural = "Dati di Fatturazione"



class AddFormFatturazione(ModelForm):
    class Meta:
        model = Fatturazione
        fields = ['user', 'denominazione', 'piva', 'codfisc', 'indirizzo', 'cap', 'citta', 'nazione',
                'telefono', 'fax', 'myemail', 'pec', 'indirizzo_spedizione']

        

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
    pub_date = models.DateTimeField('date published', null=True, blank=True, editable=False)

    def save(self, *args, **kwargs):
        self.pub_date = datetime.now()
        super(IndirizzoSpedizione, self).save(*args, **kwargs)

    def __unicode__(self):
        return unicode(self.user.username) or u''

    class Meta:
        verbose_name_plural = "Indirizzo di Spedizione"



class AddFormIndirizzoSpredizione(ModelForm):
    class Meta:
        model = IndirizzoSpedizione
        fields = ['user', 'denominazione', 'indirizzo', 'cap', 'citta', 'nazione',
                'telefono', 'fax', 'e_mail']
