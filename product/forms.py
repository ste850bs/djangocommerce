from __future__ import unicode_literals
from django.db import models
from image_cropping import ImageRatioField, ImageCropField
from datetime import datetime, timedelta, time, date
from django.utils.timesince import timesince
from filer.fields.image import FilerImageField
from filer.fields.file import FilerFileField
from filer.fields.folder import FilerFolderField
from taggit.managers import TaggableManager
from tinymce.models import HTMLField
from django.utils import timezone
from product.models import *
from django import forms



class ProductForm(forms.Form):
	nome = forms.CharField(label='Nome', max_length=100)
	quantity = forms.IntegerField(label='Quantita')
	color = forms.ModelChoiceField(queryset=Color.objects.all().order_by('-id'))