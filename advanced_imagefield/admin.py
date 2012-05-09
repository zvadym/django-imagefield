# -*- coding: utf-8 -*-
from django.contrib.contenttypes import generic
from .models import AdvancedImage

class AdvancedImageInline(generic.GenericTabularInline):
    model = AdvancedImage


