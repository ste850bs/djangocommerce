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
from django import forms




class Slider(models.Model):
    name = models.CharField(max_length=100, verbose_name="Titolo")
    image = models.ImageField(blank=True, null=True, upload_to='slider')
    scritta = models.TextField(null=True, blank=True)
    body = models.TextField(null=True, blank=True)
    link = models.TextField(null=True, blank=True)
    slider = ImageRatioField('image', '1170x600', verbose_name="Revolution Gallery")
    slider_azienda = ImageRatioField('image', '1170x431', verbose_name="Slider Azienda")
    thumb = ImageRatioField('image', '595x335', verbose_name="Miniatura")
    croplibero = ImageRatioField('image', '595x335', free_crop=True, verbose_name="Ritaglio Libero")
    pub_date = models.DateTimeField('date published')
    active = models.BooleanField('attiva',
                                    default=False)

    def image_img(self):
        if self.image:
            return u'<img src="%s" style="width:300px"/>' % self.image.url
        else:
            return '(Sin imagen)'
    image_img.short_description = 'Thumb'
    image_img.allow_tags = True

    def __unicode__(self):
        return self.titolo

    class Meta:
        verbose_name_plural = "Slider"
        ordering = ['id']