# -*- coding: utf-8 -*-
import os
from django.contrib.contenttypes import generic
from django.contrib.contenttypes.models import ContentType
from django.db import models

from .fields import AdvancedImageField

class AdvancedImage(models.Model):
    
    def _make_upload_path(self, filename):
        return os.path.join('content/image', self.content_type.model, str(self.object_id), filename)

    alt = models.CharField(u'Подпись', max_length=255, blank=True)
    image = AdvancedImageField(u'Изображение', upload_to=_make_upload_path,)

    content_type = models.ForeignKey(ContentType)
    object_id = models.PositiveIntegerField()
    content_object = generic.GenericForeignKey("content_type", "object_id")

    def __unicode__(self):
        return u'%s' % self.alt

    class Meta:
        verbose_name = u'Изображение'
        verbose_name_plural = u'Галерея'