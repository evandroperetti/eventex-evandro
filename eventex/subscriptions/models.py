﻿# coding: utf-8
from django.db import models
from django.utils.translation import ugettext_lazy as _

class Subscription(models.Model):
    name = models.CharField(_('Nome'), max_length=100)
    cpf = models.CharField(_('CPF'), max_length=11, unique=True)
    email = models.EmailField(_('Email'), unique=True)
    phone = models.CharField(_('Telefone'), max_length=20, blank=True)
    created_at = models.DateTimeField(_('Criado em'), auto_now_add=True)
    
    class Meta:
        ordering = ['created_at']
        verbose_name = _(u'incrição')
        verbose_name_plural = _(u'inscrições')
    
    def __unicode__(self):
        return self.name