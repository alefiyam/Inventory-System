# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.core.urlresolvers import reverse
from django.db import models

# Create your models here.


class Vendor(models.Model):
    name = models.CharField(max_length=64)
    url = models.CharField(max_length=64, blank=True, null=True)
    lookup_url = models.CharField(max_length=128, blank=True, null=True,
                                  help_text="url pattern to look up catalog number")
    phone = models.CharField(max_length=16, blank=True, null=True)
    rep = models.CharField(max_length=45, blank=True, null=True)
    rep_phone = models.CharField(max_length=16, blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']



class Category(models.Model):
    name = models.CharField(max_length=45)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "categories"
        ordering = ['name']

class Item(models.Model):
    name = models.CharField(max_length=128)
    vendor = models.ForeignKey(Vendor, on_delete=models.PROTECT)
    catalog = models.CharField('Catalog number', max_length=45,
                               blank=True, null=True)
    size = models.DecimalField('Size of unit',
                               max_digits=10, decimal_places=2,
                               blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    date_added = models.DateField(auto_now_add=True)
    comments = models.TextField(blank=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

    def vendor_url(self):
        try:
            return self.vendor.lookup_url % self.catalog
        except (AttributeError, TypeError):
            return None

    def get_absolute_url(self):
        return reverse("inventory:item-detail", kwargs={'pk': self.pk})
