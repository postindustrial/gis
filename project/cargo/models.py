#-*- coding: utf-8 -*-
from django.db import models

class Cargo(models.Model):
    class Meta:
        verbose_name_plural=u'Груз'
    name = models.CharField(verbose_name=u'Название', max_length=30)
    weight = models.IntegerField(verbose_name=u'Вес')

    def __unicode__(self):
        return self.name